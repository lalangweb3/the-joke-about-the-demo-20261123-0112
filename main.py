"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (1-280 Unicode code points, no network, no I/O besides
the output file itself).
"""

import os
import sys

JOKE = (
    "My AI coding agent aced every rehearsal, then live on stage it "
    "deleted the login page and asked the audience if they'd like it "
    "rebuilt as a haiku."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    text = JOKE.strip()
    # One line only: the gate counts a single text, so a stray newline
    # would still pass the length check but break the "one line" brief.
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    if not text or len(text) > 280:
        print("joke must be 1-280 characters", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read back what we wrote: the judge only ever sees this file,
    # so confirm on disk it is exactly the joke, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != text:
            print("output verification failed", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
