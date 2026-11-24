#!/usr/bin/env python3
"""Write one original out-of-office auto-reply line to the output path.

Deterministic: every run writes byte-identical output. Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Away until Monday. This auto-reply is the hardest I'll work "
    "all week, and I didn't even write it."
)


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    assert LINE, "line must not be empty"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), (
        "line must not start or end with whitespace"
    )
    assert len(LINE) <= 140, (
        f"line is {len(LINE)} characters, over the 140 limit"
    )
    assert "\n" not in LINE and "\r" not in LINE, (
        "line must be exactly one line"
    )
    assert all(ch.isprintable() or ch == " " for ch in LINE), (
        "line must contain only printable characters"
    )
    encoded = LINE.encode("utf-8")  # raises if not UTF-8-safe
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(encoded)
    written = output.read_bytes()
    assert written == encoded, (
        "written file does not round-trip byte-identical"
    )


if __name__ == "__main__":
    main()
