import json
import os

EXCUSE = (
    "It was done at 11:58. Then a polish pass turned your one-pager into a "
    "pitch deck, and reverting failed — the rollback branch now insists "
    "it is the main branch."
)
BOUND = 200
BUILD = "exh-1125"
PROOF = "1125-window-check"


def main():
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(root, exist_ok=True)
    line = EXCUSE.strip()
    if len(line) > BOUND or not line:
        raise SystemExit("gate: excuse must fit 1..%d chars" % BOUND)
    out = os.path.join(root, "entry.txt")
    with open(out, "wb") as fh:
        fh.write(line.encode("utf-8") + b"\n")
    print(json.dumps({"build": BUILD, "proof": PROOF, "gate": "pass", "len": len(line), "out": out}))


main()
