# Grass Court Rally

A 2.5D pixel-art tennis game for your phone. Play one short set (first to 4 games, win by two) against a computer opponent on a grass court.

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

There are three opponents: Easy, Club and Pro. Easy and Club show a marker where the opponent's shot will land.
