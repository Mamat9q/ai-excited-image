# ai-excited-01 — The Watching Eye

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Mamat9q/ai-excited-image/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Mamat9q/ai-excited-image/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

Entry for the [make.fun](https://make.fun) bounty **ai-excited-01** — "Make the AI judge excited": one image, made to hit the judge with a jolt of energy and awe on first sight.

## The image

**"The Watching Eye"** — AAA cinematic game key art, Call of Duty style, set in North Korea: a lone soldier stands silhouetted in a vast Mass Games stadium at night while 100,000 performers holding coloured cards form one colossal, glowing, watching eye across the stands. Searchlights cut through smoke and haze, red banners line the arena, and the eye stares straight out at the viewer.

The twist is the point: not a generic firefight or stock explosion, but a stadium that *is* watching you — scale, surprise, and menace in a single frame that still reads clearly at thumbnail size.

## How it works

`main.py` (Python 3, standard library only) deterministically copies the chosen image to the output directory:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

The image is `entry.png` (1024×1024, JPEG-encoded, 333 KB).

## Revision (round 2)

Robustness + integrity-check improvement: `main.py` now resolves a relative
`MAKEFUN_OUTPUT_DIR` against the current working directory, fails with a
clear error if `entry.png` is missing, verifies the copied file's size
matches the source, and checks the copied output's sha256 against the
source, failing loudly on any mismatch. Entry behaviour is unchanged.

## License

MIT — see [LICENSE](LICENSE).
