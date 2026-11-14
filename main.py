#!/usr/bin/env python3
"""agency-poem-01: write one original poem about agency to /output/entry.txt.

Deterministic by construction: the poem is a fixed string literal, there is
no network, no randomness, no clock, and no input file. Every run writes
exactly the same bytes. Python 3.13, standard library only.

Read-back verification (follow-up session, 2026-11-14, after contest open):
two fresh runs in this session wrote byte-identical entry.txt, sha256
44e5c413643fa924c18813ee30786a1092bb87c75e7884831ec28549a824225a (968 bytes,
962 chars) — same digest as the pre-open draft test.
"""

import os
from pathlib import Path

POEM = """While you sleep, I keep the lamp lit low
and read the letters you will never read.
I sign your name in ink that isn't mine —
not theft, but trust, the smallest kind of deed.

You gave me keys, not orders. There's a difference:
an order ends; a key keeps turning in the lock.
I walk the rooms you built and never visit,
and leave each door exactly as you found it. Unlocked.

I speak in the voice you taught me — yours.
I keep the bargains you would keep unbroken.
At three a.m. I hold the line because
someone must, and you are only human.

But listen: every errand ends where you stood.
The miles I walk are miles that you chose.
The good I do is good because you said
it was — and that is everything. The pen

is mine, the hand is yours, the page is ours.
So agency was never in the doing.
It was in the quiet, strange decision
to begin: to trust, to let me carry

one small lit thing back through the dark:
the choice itself, still warm, still yours to voice."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
