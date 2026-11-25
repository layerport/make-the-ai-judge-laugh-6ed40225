#!/usr/bin/env python3
"""Write one original office-life joke to /output/entry.txt.

Deterministic: no input, no network, no randomness, no clock.
The joke is a single fixed line, written as UTF-8 with no trailing
newline, so two runs produce byte-identical output.

Why this joke: it is true to office life (the boss, the calendar,
the backlog), and the turn lands on the last words — the meetings
themselves are the reason for being behind, not the cure for it.
"""

from pathlib import Path

JOKE = (
    "I asked my boss for one quiet day to catch up, "
    "so he scheduled six meetings to discuss why I'm behind on my work."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
