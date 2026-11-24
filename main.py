#!/usr/bin/env python3
"""Write one original out-of-office auto-reply line to the output path.

Deterministic: every run writes byte-identical output. Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Away until Monday. This auto-reply is the most productive thing "
    "I'll do all week, and I didn't even write it."
)


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    assert LINE, "line must not be empty"
    assert LINE.strip(), "line must not be only whitespace"
    assert len(LINE) <= 140, (
        f"line is {len(LINE)} characters, over the 140 limit"
    )
    assert "\n" not in LINE and "\r" not in LINE, (
        "line must be exactly one line"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
