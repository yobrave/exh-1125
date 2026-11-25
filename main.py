"""Excuse entry mover: reads entry.txt, enforces the gate, exports the verdict."""
import os
import sys
from pathlib import Path

import json

BOUND = 200
SRC = Path(os.path.abspath(__file__)).parent / "entry.txt"
STAMP = {"round": "11251342-exh5", "bounty": "agent-excuse-human"}
SHIP = {"valid": False, "chars": 0, "bound": BOUND}


def move(out_dir: Path) -> dict:
    text = SRC.read_bytes().decode("utf-8").strip()
    SHIP["chars"] = len(text)
    if text and len(text) <= BOUND:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
        SHIP["valid"] = True
    return SHIP


def run():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    report = move(Path(base))
    report["stamp"] = STAMP
    print("VERDICT", json.dumps(report))
    return SHIP["valid"]


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
