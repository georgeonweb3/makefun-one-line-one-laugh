#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

The line is the blind-tournament winner (candidate B, 5/5): a three-beat
boat story — Grandad's last words, the sale, the sinking — ending on the
mundane, haunting image of his ghost rowing past the house every Tuesday.
"""
import os

LINE = (
    "Grandad's last words were 'don't sell the boat.' "
    "We sold it. The buyer sank it. "
    "His ghost rows past our house every Tuesday."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate (from the competition rules): 1-140 UTF-8 chars, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    if not (1 <= len(LINE) <= 140) or not LINE.strip():
        raise SystemExit(f"entry violates the 1-140 char gate: {len(LINE)} chars")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
