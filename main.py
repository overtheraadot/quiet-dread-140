#!/usr/bin/env python3
"""Writes the entry: one code-review comment approving a PR with quiet dread."""
import os

LINE = (
    "Approved. Clean diff, green tests, and the quiet certainty "
    "that a stranger will delete all of this one day without reading it."
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
