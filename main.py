#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — one useless app pitch, one sentence.

Writes exactly one line to /output/entry.txt: the pitch for FernMail, an
app that texts your houseplants a good-morning message every day so they
feel loved, then charges you again to remind you that you forgot to water
them anyway. A product that sounds real, a founder who sounds certain,
and a function nobody on earth needs.
"""

import os

LINE = (
    "FernMail is the $4.99-a-month app that texts your houseplants a "
    "good-morning message every day so they feel loved, then charges you "
    "again to remind you that you forgot to water them anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate: one UTF-8 line, 1-240 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) <= 240 and LINE.strip(), (
        "entry must be a single line of 1-240 characters"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
