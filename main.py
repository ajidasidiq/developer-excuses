#!/usr/bin/env python3
"""Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt, deterministically.

The excuse: "All 400 tests passed. Production just wasn't one of them."
The twist every developer recognises — the suite was green because it
never actually tested production.
"""

import os

EXCUSE = "All 400 tests passed. Production just wasn't one of them."

# The gate allows 1-200 characters of UTF-8 text; stay safely inside it.
assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
assert EXCUSE.strip(), "excuse must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
