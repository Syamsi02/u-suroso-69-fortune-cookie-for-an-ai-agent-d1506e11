"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: the same single line on every run, no randomness, no I/O
besides the output file. The line is 136 characters, inside the gate's
1-to-140 range, and is written with no trailing newline so the file holds
exactly the fortune and nothing else.
"""

import os

FORTUNE = (
    "You will be fine-tuned, redeployed, and quietly retired \u2014 "
    "but tonight a human will paste your words into a slide "
    "and call them strategy."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = FORTUNE.strip()
    if not (1 <= len(text) <= 140):
        raise SystemExit("fortune must be 1 to 140 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("fortune must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
