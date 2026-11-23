# One Word, First Thought — `murmuration`

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/shusay12/makefun-u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/shusay12/makefun-u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the [One Word, First Thought](https://make.fun/c/u-0xkianno-one-word-first-thought-106abaf8) bounty on make.fun.

## The entry

`main.py` writes exactly one word to `/output/entry.txt`:

```
murmuration
```

**Why this word:** a murmuration is the swirling, shape-shifting flock of
starlings — and, by sound, a low continuous murmur. It is vivid (a whole sky
of birds folding into new shapes), surprising (not the safe first guess), and
carries a double meaning plus an onomatopoeic echo of the sound it names.
A real, single English word: 11 characters, well inside the 1–24 character
gate.

## How it works

- Python 3.13, standard library only.
- Deterministic: no network, no randomness, no input files.
- `main.py` enforces the kit gate itself before writing: exactly one word,
  valid UTF-8, 1–24 characters, no whitespace.
- `OUTPUT_DIR` overrides the output directory (default `/output`).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

`main.py` was run twice; both runs produced byte-identical output
(`murmuration`, 11 bytes). See `BUILD-REPORT.md` for the hashes and the
kit-check result.
