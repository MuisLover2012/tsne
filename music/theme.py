# Grass Court Rally theme, arranged in 8-bit from the creator's guitar recording.
# Analysis: 92 BPM, guitar tuned ~half a semitone flat (corrected to concert pitch here).
# Song: intro on E (B-C# hammer-on), verse G# - A - F# - E with a top line C - C# - B,
# bridge G# - A - Am - D - E with a picked riff, ending ringing on F#.
# Times are in eighth notes; the loop is 20 bars of 8 eighths. Lead = guitar top line one octave up.
import json
LEAD = []
def add(off, notes):
    for s, d, m in notes: LEAD.append((off + s, d, m))
INTRO = [(0, 2, 76), (2, 2, 76), (4, 1, 73), (5, 1, 71), (6, 1, 71), (7, 1, 71),
         (8, 4, 76), (12, 1, 76), (13, 1, 71), (14, 1, 71), (15, 1, 71)]
VERSE = [(0, 2, 72), (2, 2, 72), (4, 1, 72), (5, 1, 71), (6, 2, 72),
         (8, 2, 73), (10, 2, 73), (12, 3, 73), (15, 1, 73),
         (16, 2, 73), (18, 2, 73), (20, 1, 73), (21, 1, 71), (22, 1, 71), (23, 2, 71),
         (25, 3, 71), (28, 1, 71), (29, 2, 71), (31, 1, 71)]
BRIDGE = [(0, 1, 75), (1, 1, 72), (2, 1, 76), (3, 2, 69), (5, 1, 72), (6, 1, 74), (7, 1, 72),
          (8, 1, 69), (9, 1, 72), (10, 1, 78), (11, 2, 71), (13, 1, 71), (14, 1, 75), (15, 1, 75),
          (16, 1, 75), (17, 1, 76), (18, 3, 76), (21, 1, 72), (22, 1, 70), (23, 1, 72),
          (24, 1, 69), (25, 1, 73), (26, 1, 72), (27, 1, 74), (28, 2, 71), (30, 2, 71)]
ENDING = [(0, 2, 75), (2, 2, 75), (4, 1, 72), (5, 1, 68), (6, 2, 72), (8, 2, 73), (10, 2, 73), (12, 4, 78)]
add(0, INTRO); add(16, VERSE); add(48, VERSE); add(80, BRIDGE); add(112, VERSE); add(144, ENDING)
CHORDS = [(0, 'E')]
for o in (16, 48, 112): CHORDS += [(o, 'G#'), (o + 8, 'A'), (o + 12, 'F#'), (o + 16, 'E')]
CHORDS += [(80, 'G#'), (82, 'A'), (85, 'Am'), (90, 'D'), (91, 'E'), (96, 'G#'), (97, 'A'), (101, 'Am'), (107, 'D'), (108, 'E')]
CHORDS += [(144, 'G#'), (152, 'A'), (156, 'F#')]
CHORDS.sort()
# guitar voicings from the recording: [bass root, chord tones]
VOICINGS = {'E': (40, [52, 56, 59, 64]), 'G#': (44, [51, 56, 60, 63]), 'A': (45, [52, 57, 61, 64]),
            'F#': (42, [49, 54, 58, 61]), 'Am': (45, [52, 57, 60, 64]), 'D': (38, [50, 54, 57, 62])}
# section map for drums: intro, verse1 (softer), verse2, bridge, verse3, ending
SECTIONS = [(0, 'intro'), (16, 'verse1'), (48, 'verse'), (80, 'bridge'), (112, 'verse'), (144, 'ending')]
theme = {'bpm': 92, 'eighths': 160, 'lead': sorted(LEAD), 'chords': CHORDS, 'voicings': VOICINGS, 'sections': SECTIONS}
json.dump(theme, open('theme.json', 'w'))
print('lead notes', len(LEAD), 'chord changes', len(CHORDS), 'length', round(160 * 60 / 92 / 2, 1), 's')
