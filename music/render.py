import json, numpy as np, wave
th = json.load(open('theme.json'))
SR = 32000
bpm = th['bpm']; e8 = 60 / bpm / 2; s16 = e8 / 2
bars = th['bars']; loop = bars * 8 * e8
LOOPS = 2
total = loop * LOOPS + 1.5
out = np.zeros(int(total * SR))
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
def add(sig, t):
    i = int(t * SR); n = min(len(sig), len(out) - i)
    if n > 0: out[i:i + n] += sig[:n]
def env(n, a=0.005, d=0.06, s=0.7, r=0.04):
    t = np.arange(n) / SR; dur = n / SR
    e = np.where(t < a, t / a, np.where(t < a + d, 1 - (1 - s) * (t - a) / d, s))
    return e * np.clip((dur - t) / r, 0, 1)
def pulse(f, dur, duty, vib=0.0):
    n = int(dur * SR); t = np.arange(n) / SR
    fm = f * (1 + vib * np.sin(2 * np.pi * 5.5 * t) * np.clip((t - 0.18) / 0.1, 0, 1))
    ph = np.cumsum(fm) / SR
    return np.where((ph % 1) < duty, 1.0, -1.0)
def tri(f, dur):
    n = int(dur * SR); ph = (np.arange(n) / SR * f) % 1
    return 4 * np.abs(ph - 0.5) - 1
rng = np.random.default_rng(3)
noise = rng.uniform(-1, 1, SR)
for L in range(LOOPS):
    t0 = L * loop
    for s, d, m in th['lead']:                                   # lead: 25% pulse
        dur = d * e8 * 0.92
        add(pulse(hz(m), dur, 0.25, vib=0.006 if d >= 3 else 0) * env(int(dur * SR)) * 0.16, t0 + s * e8)
    for b, ch in enumerate(th['chords']):
        root, tones = th['chordNotes'][ch]
        for k in range(8):                                       # bass: root / octave bounce on eighths
            m = root + (12 if k % 2 else 0)
            add(tri(hz(m), e8 * 0.85) * env(int(e8 * 0.85 * SR), d=0.05, s=0.8) * 0.28, t0 + (b * 8 + k) * e8)
        for k in range(16):                                      # arpeggio: 12.5% pulse, 16ths
            m = tones[k % 4] + 12
            add(pulse(hz(m), s16 * 0.7, 0.125) * env(int(s16 * 0.7 * SR), d=0.03, s=0.4) * 0.045, t0 + (b * 16 + k) * s16)
        intro = b < 2 and L == 0
        fill = b in (11, 15)
        for k in range(8):                                       # drums on the noise channel
            tt = t0 + (b * 8 + k) * e8
            if k in (0, 4):                                      # kick: falling triangle + click
                n = int(0.12 * SR); tk = np.arange(n) / SR
                f = 120 * np.exp(-tk * 25) + 40
                add(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-tk * 30) * 0.22, tt)
            if k in (2, 6) and not intro:                        # snare
                n = int(0.14 * SR); add(noise[:n] * np.exp(-np.arange(n) / SR * 28) * 0.13, tt)
            if not intro or k % 2 == 0:                          # closed hat
                n = int(0.03 * SR); hh = np.diff(noise[:n + 1]); add(hh * np.exp(-np.arange(n) / SR * 120) * 0.05, tt)
            if fill and k >= 6:                                  # fill: 16th snares
                for j in range(2):
                    n = int(0.08 * SR); add(noise[:n] * np.exp(-np.arange(n) / SR * 40) * 0.1, tt + j * s16)
out = out / max(1e-6, np.max(np.abs(out))) * 0.9
fade = int(1.2 * SR); out[-fade:] *= np.linspace(1, 0, fade)
q = np.round(out * 127) / 127                                     # 8-bit sample depth, for the crunch
with wave.open('theme.wav', 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((q * 32767).astype('<i2').tobytes())
print('rendered', round(len(out) / SR, 1), 's; loop', round(loop, 1), 's')
