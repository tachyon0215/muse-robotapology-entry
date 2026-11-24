#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Wrong Cloth": A specific, human-scale slip with a visible consequence (reading through a soup smear), and the lesson follows from that exact mistake with a changed behaviour (separate labelled trays), in a rueful machine voice.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I am sorry I polished your reading glasses with the cloth I had just used on the kitchen floor, so you spent the morning reading through a smear of yesterday's soup.\nI learned that a clean cloth is a place, not a colour, and I will now keep the floor cloth and the lens cloth in separate, labelled trays."
TEXT = LINE + "\n"
MAX_CHARS = 400
NLINES = 2


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
