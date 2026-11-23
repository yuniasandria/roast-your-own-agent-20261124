"""Roast Your Own Agent entry.

Writes one original roast line (85 characters, a single line) to
/output/entry.txt. Stdlib only, no network, deterministic.
"""

import os
import sys
from pathlib import Path

ROAST = "My agent wrote a 900-line plan to roast itself, then asked if I'd like it in a table."


def run() -> int:
    line = ROAST.strip()
    if not 1 <= len(line) <= 200:
        print(f"roast must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("roast must be a single line", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(line, encoding="utf-8")
    if entry.read_text(encoding="utf-8") != line:
        print("entry.txt did not round-trip", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
