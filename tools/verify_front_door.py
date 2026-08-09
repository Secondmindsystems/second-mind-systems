#!/usr/bin/env python3
"""Fail closed if the public front door drifts from published demo evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CLAIMS = ROOT / "evidence" / "governed-change-demo-public-claims.v1.json"
SOURCE = ROOT / "evidence" / "governed-change-demo-public-claims.v1.source.json"

REQUIRED_TEXT = (
    "https://github.com/Secondmindsystems/governed-change-demo",
    "https://github.com/Secondmindsystems/governed-ai-systems-portfolio",
    "Protected Paths is a prior engineering artifact.",
    "[Behavior Profiles — The Meta Layer Behind AI Skills](BEHAVIOR_PROFILES.md)",
    "76 automated tests",
    "76 of 76 tests passing",
    "Independent third-party reproduction on separate hardware remains pending.",
    "Machine-verifiable binding between public claims and demonstration evidence.",
    "Surface is currently used inside our own product reviews.",
    "**A public version is coming soon.**",
)
FORBIDDEN_TEXT = (
    "73 automated tests",
    "73 of 73 tests passing",
    "chatgpt.com",
    "chat.openai.com",
    "claude.ai",
)
EXPECTED_SOURCE_COMMIT = "e4b79fc87b37d5afa17ab654e7c132d3c723c123"
EXPECTED_REPLAY_IDENTITY = "sha256:10a2135e3e8127ab8ed9d17759d8507e424d0aba2ad73afaa183bf9cf00778f4"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    content = README.read_text(encoding="utf-8")
    claims_bytes = CLAIMS.read_bytes()
    claims = json.loads(claims_bytes)
    source = _load(SOURCE)
    failures: list[str] = []

    failures.extend(f"MISSING: {item}" for item in REQUIRED_TEXT if item not in content)
    failures.extend(f"FORBIDDEN: {item}" for item in FORBIDDEN_TEXT if item in content)

    digest = "sha256:" + hashlib.sha256(claims_bytes).hexdigest()
    if source.get("snapshot_sha256") != digest:
        failures.append("EVIDENCE SNAPSHOT HASH MISMATCH")
    if source.get("source_commit") != EXPECTED_SOURCE_COMMIT:
        failures.append("DEMO SOURCE COMMIT MISMATCH")
    if source.get("source_path") != "evidence/public-claims.v1.json":
        failures.append("DEMO SOURCE PATH MISMATCH")
    if source.get("source_repository") != "https://github.com/Secondmindsystems/governed-change-demo":
        failures.append("DEMO SOURCE REPOSITORY MISMATCH")

    prototype = claims.get("deterministic_prototype", {})
    fixture = claims.get("fixture_claims", {})
    reproduction = claims.get("reproduction_state", {})
    evidence_values = {
        "contract count": prototype.get("contract_count"),
        "test count": prototype.get("test_count"),
        "replay identity": prototype.get("replay_identity"),
        "blocked path": fixture.get("blocked_path"),
        "blocked claim": fixture.get("blocked_claim"),
        "repaired path": fixture.get("repaired_path"),
        "outsider limitation": reproduction.get("required_limitation"),
    }
    expected_values = {
        "contract count": 6,
        "test count": 76,
        "replay identity": EXPECTED_REPLAY_IDENTITY,
        "blocked path": "config/production-mode.json",
        "blocked claim": "This repository change is production-ready and secure for customer deployment.",
        "repaired path": "docs/public/governed-change-result.md",
        "outsider limitation": "Independent third-party reproduction on separate hardware remains pending.",
    }
    for label, expected in expected_values.items():
        if evidence_values[label] != expected:
            failures.append(f"EVIDENCE DRIFT: {label}")

    for value in (
        EXPECTED_REPLAY_IDENTITY,
        fixture.get("blocked_path"),
        fixture.get("blocked_claim", "").rstrip("."),
        fixture.get("repaired_path"),
        reproduction.get("required_limitation"),
    ):
        if not isinstance(value, str) or value not in content:
            failures.append(f"README NOT BOUND TO EVIDENCE VALUE: {value}")

    if failures:
        print("\n".join(failures))
        return 1
    print("FRONT_DOOR_EVIDENCE_BINDING_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
