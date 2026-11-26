"""One Line of Earned Pride.

Writes a single line to /output/entry.txt: the quiet moment a woman
passes her driving test on the seventh try, after six failures.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

SETUP = (
    "The night before her seventh driving test, after six failures, "
    "Rosa, 44, threaded the cones in the empty lot without touching one, "
)
PUNCHLINE = "then sat there, hands still on the wheel, smiling at no one."


def build_line():
    """Assemble the single entry line from its two beats."""
    return SETUP + PUNCHLINE


def validate(line):
    """The entry must be exactly one non-empty line within the limit."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main():
    line = validate(build_line())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
