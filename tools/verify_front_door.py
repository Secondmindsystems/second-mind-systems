#!/usr/bin/env python3
"""Fail closed if the public front door loses its required proof routes."""

from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"
REQUIRED_TEXT = (
    "https://github.com/Secondmindsystems/governed-change-demo",
    "https://github.com/Secondmindsystems/governed-ai-systems-portfolio",
    "76 automated tests",
    "76 of 76 tests passing",
    "Independent third-party reproduction on separate hardware remains pending.",
)
FORBIDDEN_STALE_TEXT = ("73 automated tests", "73 of 73 tests passing")


def main() -> int:
    content = README.read_text(encoding="utf-8")
    missing = [item for item in REQUIRED_TEXT if item not in content]
    stale = [item for item in FORBIDDEN_STALE_TEXT if item in content]
    if missing or stale:
        for item in missing:
            print(f"MISSING: {item}")
        for item in stale:
            print(f"STALE: {item}")
        return 1
    print("FRONT_DOOR_INTEGRITY_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
