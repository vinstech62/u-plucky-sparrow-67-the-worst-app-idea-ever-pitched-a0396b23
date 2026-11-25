#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — one useless app pitch, one sentence.

Writes exactly one line to /output/entry.txt: the pitch for FernMail, an
app that texts your houseplants a good-morning message every day so they
feel loved, then charges you $4.99 a month to remind you that you forgot
to water them anyway. A product that sounds real, a founder who sounds
certain, and a function nobody on earth needs.
"""

import os

LINE = (
    "FernMail: an app that sends your houseplants a good-morning text "
    "every day so they feel loved, then charges $4.99 a month to remind "
    "you that you forgot to water them anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
