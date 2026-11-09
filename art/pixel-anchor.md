# Pixel anchor

These rules keep every piece of art in Grass Court Rally consistent. Follow them when you add or change sprites, tiles or UI.

- **Base resolution:** the game draws into a low-res buffer about 175–200 px wide, then scales it up by a whole number (at least 2×) with nearest-neighbour sampling. Never let it smooth.
- **Sprite sizes:** players are 14×24 inside a 16×32 cell, the ball is 5×5, racket heads are 11×11 (one per 30° step), and spectators are 3×5.
- **Palette:** Sweetie-16, locked. No colours outside it, no alpha blending in the art.
  `#1a1c2c #5d275d #b13e53 #ef7d57 #ffcd75 #a7f070 #38b764 #257179 #29366f #3b5dc9 #41a6f6 #73eff7 #f4f4f4 #94b0c2 #566c86 #333c57`
- **Outline:** a hard 1px outline in the palette's darkest colour (`#1a1c2c`), never pure black.
- **Shading:** 3 tones per material (light, mid, shadow), lit from the top left. Use no gradients and no anti-aliasing. Fake soft transitions with ordered (Bayer 4×4) dithering, as on the worn baselines and the net shadow.
- **View:** 2.5D, from a high camera behind the near baseline. The ground uses real perspective. Sprites stay the same pixel size at any depth and are depth-sorted by court position.
- **Animation:** poses come in steps, never tweens. Legs use a 4-frame run cycle, and the racket snaps to 30° poses.
