#!/usr/bin/env python3
"""Entry for make.fun bounty "The joke the reviewer laughs at".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (the directory is created if needed). The output
directory can be overridden with the OUTPUT_DIR environment variable,
which is only used for local test runs.
"""

import os
from pathlib import Path

JOKE = (
    "I asked it to fix one typo in the README; it rewrote the codebase "
    "in Rust and kept the typo for historical accuracy."
)


def main() -> None:
    text = JOKE + "\n"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
