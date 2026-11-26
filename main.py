"""Fortune Cookie Funnies for Engineers.

Writes a single original fortune cookie message for a software
engineer to /output/entry.txt.

The line is a fortune-cookie prophecy that is really a production
curse in disguise: one specific engineering fate, stated as a
fortune, with the punchline in the last words.
"""

from __future__ import annotations

import os

FORTUNE = "You will delete the one line of dead code holding production together."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 120


def validate(text: str) -> str:
    """Enforce the competition gate in code.

    The entry must be UTF-8 text of 1 to 120 characters, a single
    line, and not only whitespace. Raises ValueError otherwise.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 120 characters, got %d" % len(text)
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def main() -> None:
    """Validate the fortune and write exactly that one line."""
    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
