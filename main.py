#!/usr/bin/env python3
"""One Letter: Coffee or Tea (make.fun).

Writes exactly one letter to /output/entry.txt: "A" for coffee.
No network, no randomness, no arguments. The output is a single
ASCII character, which is what the competition gate requires.
"""

import os
import sys

ENTRY = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    # Read it back: the gate wants exactly one non-whitespace character.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print(f"error: expected {ENTRY!r}, wrote {written!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
