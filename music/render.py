import json, numpy as np, wave
th = json.load(open('theme.json'))
SR = 32000
e8 = 60 / th['bpm'] / 2; s16 = e8 / 2; N8 = th['eighths']; loop = N8 * e8
LOOPS = 2
out = np.zeros(int((loop * LOOPS + 2.5) * SR))
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
    return np.where((np.cumsum(fm) / SR % 1) < duty, 1.0, -1.0)
def tri(f, dur):
    ph = (np.arange(int(dur * SR)) / SR * f) % 1
    return 4 * np.abs(ph - 0.5) - 1
noise = np.random.default_rng(3).uniform(-1, 1, SR * 2)
def chord_at(e):
    c = th['chords'][0][1]
    for at, name in th['chords']:
        if at <= e: c = name
    return c
def section_at(e):
    s = th['sections'][0][1]
    for at, name in th['sections']:
        if at <= e: s = name
    return s
def drum(kind, t, vol=1.0):
    if kind == 'kick':
        n = int(0.12 * SR); tk = np.arange(n) / SR; f = 120 * np.exp(-tk * 25) + 40
        add(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-tk * 30) * 0.22 * vol, t)
    elif kind == 'snare':
        n = int(0.14 * SR); add(noise[:n] * np.exp(-np.arange(n) / SR * 28) * 0.13 * vol, t)
    elif kind == 'hat':
        n = int(0.03 * SR); add(np.diff(noise[:n + 1]) * np.exp(-np.arange(n) / SR * 120) * 0.05 * vol, t)
    elif kind == 'crash':
        n = int(1.6 * SR); add(np.diff(noise[:n + 1]) * np.exp(-np.arange(n) / SR * 2.2) * 0.07 * vol, t)
for L in range(LOOPS):
    t0 = L * loop
    for s, d, m in th['lead']:
        dur = d * e8 * 0.92
        add(pulse(hz(m), dur, 0.25, vib=0.006 if d >= 3 else 0) * env(int(dur * SR)) * 0.16, t0 + s * e8)
    for e in range(N8):
        root, tones = th['voicings'][chord_at(e)]
        sec = section_at(e)
        tt = t0 + e * e8
        add(tri(hz(root + (12 if e % 2 else 0)), e8 * 0.85) * env(int(e8 * 0.85 * SR), d=0.05, s=0.8) * 0.28, tt)
        for j in range(2):
            m = tones[(e * 2 + j) % 4] + 12
            add(pulse(hz(m), s16 * 0.7, 0.125) * env(int(s16 * 0.7 * SR), d=0.03, s=0.4) * (0.03 if sec in ('intro', 'verse1') else 0.045), tt + j * s16)
        k8 = e % 8
        if sec == 'intro':
            if k8 == 0: drum('kick', tt, 0.7)
            if k8 % 2 == 0: drum('hat', tt, 0.7)
        elif sec == 'verse1':
            if k8 in (0, 4): drum('kick', tt)
            if k8 == 6: drum('snare', tt, 0.7)
            drum('hat', tt, 0.8)
        else:
            if k8 in (0, 4) or (sec == 'bridge' and k8 == 5): drum('kick', tt)
            if k8 in (2, 6): drum('snare', tt)
            drum('hat', tt); 
            if sec == 'bridge': drum('hat', tt + s16, 0.6)
        if e in (78, 79, 110, 111, 142, 143):
            drum('snare', tt, 0.8); drum('snare', tt + s16, 0.8)
        if e in (16, 80, 156) or (e == 0 and L > 0): drum('crash', tt)
out = out / np.max(np.abs(out)) * 0.9
fade = int(2.0 * SR); out[-fade:] *= np.linspace(1, 0, fade)
q = np.round(out * 127) / 127
with wave.open('theme.wav', 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((q * 32767).astype('<i2').tobytes())
print('rendered', round(len(out) / SR, 1), 's; loop', round(loop, 1), 's')
