#!/usr/bin/env python3
"""Forecast for Nowhere City — make.fun entry.

Writes one funny weather forecast for the invented city of Gloomwick
to /output/entry.txt: a single line, at most 120 characters, with no
trailing newline.
"""

import os

FORECAST = (
    "Gloomwick: 16\u00b0C, rain falling upward since Tuesday; "
    "locals asked to keep their feet on the ground."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def _write_and_verify(text, path):
    """Write *text* to *path* as UTF-8 with no trailing newline,
    then read it back and verify it is exactly one line of
    1..MAX_CHARS characters."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "rb") as handle:
        raw = handle.read()
    decoded = raw.decode("utf-8")
    if decoded != text:
        raise ValueError("round-trip mismatch: file differs from forecast")
    if "\n" in decoded or len(decoded) == 0 or len(decoded) > MAX_CHARS:
        raise ValueError("entry must be one line of 1..120 characters")
    return decoded


def main():
    line = _write_and_verify(FORECAST, OUTPUT_PATH)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
