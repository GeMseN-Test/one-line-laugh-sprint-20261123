#!/usr/bin/env python3
"""One-Line Laugh Sprint — writes one original funny line to /output/entry.txt.

Deterministic: the same line every run. No randomness, no network, stdlib only.
One scene (phone at 1%), one twist at the end (it dies mid-sentence).
"""

import os

LINE = (
    "My phone hit 1%, so I whispered 'stay with me' — and it died "
    "mid-sentence, like it had somewhere better to be."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
