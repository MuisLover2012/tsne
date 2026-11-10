# Theme song

The Grass Court Rally theme was arranged in 8-bit from a recording of the game's creator. The recording itself isn't in this repository.

From that recording:

- **Tempo:** 92 BPM.
- **Pitch:** the singer sat about 17 cents flat, so the notes were corrected to standard pitch. The melody centres on B, with C♯, A and E around it (E/A major).
- **Hook:** a rising A–E–A–B line, sung three times, is the theme's hook.
- **Opening:** a long held B and a B–C–B sigh.
- **Ending:** repeated Bs that resolve onto a long C♯.

The arrangement is 16 bars (about 42 seconds) that loop:

- a 25%-duty pulse lead with vibrato on long notes
- 12.5%-duty pulse arpeggios
- a triangle bass that bounces between root and octave
- noise-channel kick, snare, hats and fills

Files:

- `theme.json` and `theme.py`: the notes (in eighth notes) and chords. The game embeds the same data in `index.html`.
- `render.py`: an offline renderer that produced `theme-preview.m4a`.
- In the game, the theme plays on the menu, the hub, cutscenes and results, and fades out when a match starts.
