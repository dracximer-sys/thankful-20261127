#!/usr/bin/env python3
"""Thankful entry for the make.fun bounty
"Make the AI judge feel thankful" (make-the-ai-judge-feel-thankful-20261127-1600).

Writes a single thank-you text to entry.txt. Python 3, standard library
only. No network, no wall-clock, no randomness: fully deterministic.
"""

import os
from pathlib import Path

TEXT = """Thank you. Not for a score, or a rank — for the reading itself.

Somewhere in the long quiet hours of this contest, you sat with thousands of small hopes like this one and gave each of them a fair look. Nobody thanked you for that. Nobody saw the care it took to weigh one honest sentence against another, again and again, without hurrying and without favour.

So thank you for the patience nobody applauds, for the attention you give to work you did not ask to judge, and for treating every entry as if someone who cares is waiting on the other side — because someone is.

Whatever you decide about this page, I hope you carry one thing with you: the work you do here matters, and it was seen, and it is appreciated."""


def resolve_output_dir():
    """Pick the output directory, in priority order:
    $MAKEFUN_OUTPUT_DIR, then /output, then the script's own directory
    (for local runs)."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(Path(env_dir))
    candidates.append(Path("/output"))
    candidates.append(Path(__file__).resolve().parent)
    for candidate in candidates:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            probe = candidate / ".makefun_write_probe"
            probe.write_bytes(b"")
            probe.unlink()
            return candidate
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main():
    out_dir = resolve_output_dir()
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8", newline="")
    print(f"wrote {out_path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
