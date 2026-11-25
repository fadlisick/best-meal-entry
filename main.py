"""Best Meal entry: one sentence about the best meal ever had.

Writes the sentence to /output/entry.txt for the make.fun judge.
The sentence is a single memory: a ramen counter in Osaka.
"""

import os
from pathlib import Path

# The entry: one sentence, 183 chars, about the best meal ever had.
MEAL_SENTENCE = (
    "My grandmother's burnt-edge skillet cornbread eaten over the sink at midnight—crisp lard crust, cold salted butter, and the quiet mercy of someone who loved me without ever saying it."
)


def output_path() -> Path:
    """Where the entry text goes: the harness output dir, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main() -> None:
    sentence = MEAL_SENTENCE.strip()
    if not sentence or len(sentence) > 200:
        raise SystemExit("entry sentence must be 1-200 chars")
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in sentence):
        raise SystemExit("entry sentence must not hold control chars")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(sentence, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
