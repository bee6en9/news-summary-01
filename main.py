#!/usr/bin/env python3
"""news-summary-01 entry: write the baked-in summary to /output/entry.txt.

Reads summary.txt beside this file and copies it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable is
unset). Python 3.13, standard library only, no network, deterministic:
two runs write the same bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "summary.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    # Fail loudly if the summary ever leaves the gate (1-2000 code points,
    # at least one non-whitespace character) instead of submitting silently.
    text = open(dst, encoding="utf-8").read()
    if not 1 <= len(text) <= 2000 or not text.strip():
        raise SystemExit("summary outside the 1-2000 character gate")


if __name__ == "__main__":
    main()
