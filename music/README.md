# Theme song

The Grass Court Rally theme was arranged in 8-bit from a guitar recording by the game's creator. The recording itself isn't in this repository.

## The guitar piece

- **Tempo:** 92 BPM.
- **Tuning:** the guitar is tuned about half a semitone flat. The arrangement is in standard pitch.

| Time | Section | Chords | What the guitar does |
| --- | --- | --- | --- |
| 0–11 s | Intro | E | A B-to-C♯ hammer-on on top |
| 11–37 s | Verse, three times | G♯ → A → F♯ → E | The top note slides C → C♯ → B |
| 37–57 s | Bridge | G♯ → A → Am → D → E | A faster picked riff |
| 57–77 s | Verse returns | G♯ → A → F♯ → E | Same as the first verse |
| 77 s | Ending | F♯ | Rings out on a long F♯ |

The chords come from the guitar's own shapes: an open A and E, and G♯ and F♯ barre chords.

## The 8-bit arrangement

The arrangement is 20 bars (about 52 seconds) that loop: intro, verse, verse, bridge, verse, then the ending's F♯ leads back into the intro's E.

- **Lead:** a 25%-duty pulse wave playing the guitar's top line one octave up, with vibrato on held notes.
- **Arpeggios:** a 12.5%-duty pulse wave cycling through the guitar's chord shapes in 16th notes.
- **Bass:** a triangle wave on the guitar's low notes, bouncing between root and octave.
- **Drums:** on the noise channel. They build from a sparse intro, through a softer first verse, to 16th-note hi-hats in the bridge. Fills lead into each section, and a crash rings with the final F♯.

## Files

- `theme.json` and `theme.py`: the notes and chord timeline, in eighth notes. The game embeds the same data in `index.html`.
- `render.py`: an offline renderer that produced `theme-preview.m4a`.
- In the game, the theme plays on the menu, the hub, cutscenes and results, and fades out when a match starts.
