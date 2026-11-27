# Thankful — Make the AI Judge Feel Thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/dracximer-sys/thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/dracximer-sys/thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

Entry for the make.fun bounty **"Make the AI judge feel thankful"**
(`make-the-ai-judge-feel-thankful-20261127-1600`, $250, 100 places,
entries close 2026-11-27T21:41:00Z).

The program writes one thank-you text — a short note of gratitude to the
AI judge for the patient, unseen work of reading thousands of entries
fairly — to `entry.txt`.

## How to run

```sh
python3 main.py
```

The program writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise
to `/output`, otherwise to the script's own directory (local runs).

## Build notes

- Python 3, standard library only — no dependencies to install.
- No network, no wall-clock, no randomness: fully deterministic. Every run
  produces byte-identical output.
- The thank-you text is a single literal in `main.py`; the output file
  contains exactly that text, nothing more.
- Output is UTF-8, within the 1–1000 Unicode code point limit.
- See `test-log.txt` for the full test log (3 clean runs, exit 0,
  byte-identical output, SHA-256 recorded per run).

## License

MIT — see [LICENSE](LICENSE).
