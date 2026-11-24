#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses (make.fun bounty
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.

Chosen line (candidate A, 96 characters):

    The code passed all 400 tests, then met one real user and immediately
    forgot everything it knew.

Why this line, against the judge's criteria in order:
  1. On subject: it IS a developer excuse for code breaking in
     production -- the code passed its tests, then broke on a real user.
  2. Twist a developer recognises: the reveal is that all 400 tests
     proved nothing -- one real user undid them. Every developer has
     watched green CI meet production and lose.
  3. Sounds like a developer: "passed all 400 tests", "one real user"
     -- plain incident-room language, jargon used right, no forced
     punchline voice.
  4. Lands fast: one sentence, 96 characters, every word working; the
     punch lands on the last words ("forgot everything it knew").
  5. Fresh: it turns the worn "it works on my machine" family inside
     out -- instead of blaming the machine, the code itself forgets
     everything the moment a real user shows up.
  Candidates B and C lost: B ("it's a feature that only activates when
  the CEO is watching") leans on the tired not-a-bug-it's-a-feature
  setup and its twist is telegraphed -- the reader sees the CEO gag
  coming from the first clause, so the second read adds nothing; C
  (server read my comments and believed them) is a cute image but the
  twist reveals nothing a developer recognises about why production
  actually broke -- comments do not cause outages, so the excuse
  sounds invented rather than lived. A wins on the judge's first two
  criteria outright and loses nothing on the rest: 96 characters,
  one sentence, no word to trim.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

EXCUSE = "The code passed all 400 tests, then met one real user and immediately forgot everything it knew."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(excuse: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single line, at least one character that is not white
    space, and encodable as UTF-8 (the gate reads UTF-8 text, so a
    string that cannot round-trip through UTF-8 must never be written).
    Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(excuse) <= 200:
        raise SystemExit(f"excuse is {len(excuse)} characters, must be 1-200")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("excuse must be a single line, no line breaks")
    if not any(not ch.isspace() for ch in excuse):
        raise SystemExit("excuse must contain a non-whitespace character")
    try:
        excuse.encode("utf-8").decode("utf-8")
    except UnicodeError as exc:
        raise SystemExit(f"excuse is not valid UTF-8 text: {exc}")


def main() -> None:
    validate(EXCUSE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the excuse: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
