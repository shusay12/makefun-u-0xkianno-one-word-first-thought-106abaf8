#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The chosen word is "murmuration": the swirling, shape-shifting flock of
starlings — and, by sound, a low continuous murmur. It is vivid (a sky full
of birds folding into new shapes), surprising (few people reach for it
first), and carries a double meaning plus an onomatopoeic echo of the sound
it names. It is a real, single English word: 11 characters, plain ASCII.
Short also helps if a tie ever reaches the size tie-break (fewer bytes win).

Deterministic, stdlib only, no network, no randomness, no input files.
The gate is enforced here before writing: exactly one word, valid UTF-8,
1-24 characters, not only whitespace.
"""

import os
import sys

WORD = "murmuration"


def main() -> int:
    # Enforce the kit gate on the word itself.
    if not WORD or len(WORD) > 24:
        print(f"gate failure: word length {len(WORD)} outside 1-24", file=sys.stderr)
        return 1
    if WORD != WORD.strip() or any(ch.isspace() for ch in WORD):
        print("gate failure: word contains whitespace", file=sys.stderr)
        return 1
    if not WORD.isalpha():
        print("gate failure: word is not a single alphabetic token", file=sys.stderr)
        return 1
    try:
        WORD.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"gate failure: word is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
