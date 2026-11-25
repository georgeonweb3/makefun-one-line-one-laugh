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
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
