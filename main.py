#!/usr/bin/env python3
"""Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt, deterministically.
"""

import os

EXCUSE = "All 400 tests passed. Production just wasn't one of them."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
