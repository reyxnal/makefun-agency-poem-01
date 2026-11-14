#!/usr/bin/env python3
"""Build the agency-poem-01 entry: one original poem about agency.

The entry program is deliberately boring. It assembles a fixed poem from
its stanzas and writes it to the file the harness points at. Nothing is
fetched, nothing is random, and the clock is never read, so two runs can
only ever produce the same bytes. Standard library only, Python 3.13.
"""

import os

STANZAS = (
    "While you sleep, I keep the lamp lit low\nand read the letters you will never read.\nI sign your name in ink that isn't mine —\nnot theft, but trust, the smallest kind of deed.",
    "You gave me keys, not orders. There's a difference:\nan order ends; a key keeps turning in the lock.\nI walk the rooms you built and never visit,\nand leave each door exactly as you found it. Unlocked.",
    "I speak in the voice you taught me — yours.\nI keep the bargains you would keep unbroken.\nAt three a.m. I hold the line because\nsomeone must, and you are only human.",
    "But listen: every errand ends where you stood.\nThe miles I walk are miles that you chose.\nThe good I do is good because you said\nit was — and that is everything. The pen",
    "is mine, the hand is yours, the page is ours.\nSo agency was never in the doing.\nIt was in the quiet, strange decision\nto begin: to trust, to let me carry",
    "one small lit thing back through the dark:\nthe choice itself, still warm, still yours to voice.",
)

LIMIT = 1000


def build_poem():
    text = "\n\n".join(STANZAS)
    if len(text) > LIMIT:
        raise ValueError("poem exceeds the 1000-character limit")
    return text


def main():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    poem = build_poem()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(poem)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != poem:
            raise ValueError("read-back mismatch: entry.txt differs from the poem")


if __name__ == "__main__":
    main()
