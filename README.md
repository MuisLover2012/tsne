# Grass Court Rally

A 2.5D pixel-art tennis game for your phone, with a story career, quick matches against the computer and online matches against a friend.

Open `index.html` in a phone browser. It's a single file with no build step and no dependencies.

## How to play

- **Move:** keep one finger on the screen and drag to move.
- **Swing:** tap with another finger as the ball arrives. The racket winds back while you hold and swings when you lift.
- **Power:** a quick tap hits hard and deep. Hold a little longer for a softer shot, or hold until the bar flashes for a drop shot. A bar above your player shows the power while you hold.
- **Timing:** swing early to pull the ball cross-court, late to send it down the line. Swing far off and you may mishit.
- **Serve:** tap to toss, then tap again at the top of the toss. Two faults lose the point.

On a computer, use the arrow keys to move, hold and release Space to swing (press it to serve) and P to pause.

On Easy and Club, a ring at your feet turns lime when it's time to swing, and a cyan ring marks where the opponent's shot will land.

The art follows the rules in [`art/pixel-anchor.md`](art/pixel-anchor.md): the Sweetie-16 palette, 1px dark outlines and 3-tone shading.

## Playing a friend

Tap **Play a friend → Host a match**. When your friend opens the game and taps **Play a friend**, your match appears in their list and they tap **Join**. Each of you sees yourself at the bottom of the court.

Online play uses the claude.ai artifact "room" feature, so it only works in the published claude.ai version of the game. Both players need to be signed in to Claude, and the game has to be shared with your friend. Opened as a plain `index.html`, the game still works but has no online play.

How it stays fair over the network: each phone sends its own position, swings, toss, shots and rulings. The phone the ball is heading toward rules on that ball (hit, out, net, winner or fault), so your swing timing never waits on the connection.

## Career

You're a ball kid at Old Meadow. Coach Bea, who keeps the lawns and once played the Meadow Crown final, enters you in the summer circuit. Climb five tiers:

| Tier | Venue | Match length | Opponents |
| --- | --- | --- | --- |
| Park Courts | Blue hard court, trees | First to 2 games | Pip Larkin, Toby Swift, Marla Stone (boss) |
| County Clay | Red clay, slow and high | First to 3 | Hugo Brandt, Ines Rojo, Rex Vantage (rival) |
| National Indoors | Fast indoor carpet | First to 3, win by 2 | Kenji Mori, Sasha Volkov, Theo Brant |
| The Lawn Series | Grass, no training rings | First to 3, win by 2 | Lucia Ferro, Odette Blanc, Rex Vantage |
| The Meadow Crown | Centre Court | First to 4, win by 2 | Anton Grey, Victor Hale (final) |

Each opponent has their own look, portrait, lines and playing style: pushers, lobbers, big servers, grinders, net rushers, drop-shot artists and more.

The loop:

- **Stars:** every match has three, for winning, a personal goal (like "Win a game on his serve" or "Hit 8 Perfect shots") and winning by two games or more.
- **Coins:** every match pays coins, even a loss. Spend them on **Upgrades** (speed, reach, power, touch and serve) or in the **Shop** (caps, shirts and rackets).
- **World ranking:** wins earn ranking points, from #900 up to #1.
- **Focus:** three Perfect shots in a row fill the Focus meter, and your next swing becomes a **Power shot**.
- **Practice court:** Bea feeds you balls and teaches each skill. There's a coin bonus the first time.
- **Daily challenge:** a new opponent every day with a twist (wind, fast balls or golden Perfects) and a bonus for winning.
- **Endless Tour:** opens after the final. Opponents keep getting harder as you chase and defend World #1.
- **Trophies:** 16 to collect.

Your career saves on your device. In the claude.ai version it also saves privately to your account (only for viewers allowed to write data, such as the owner and Contributors).

## Quick match

There are three computer opponents: Easy, Club and Pro. Easy and Club show a marker where the opponent's shot will land.
