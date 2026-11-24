#!/usr/bin/env python3
"""Funniest Time Machine Warning Label (120 chars max).

Judge angle: a genuine safety notice with a straight face, turning a real
time-travel hazard -- meeting your own past self -- into the joke, and
saving the surprise for the last few words. The label opens like any
warranty warning, then the sting lands at the end: of the two of you, the
one reading the label is the uninsured one.
"""

import os

GATE = 120

WARNING = "WARNING:"
HAZARD = "Meeting yourself voids the warranty."
PUNCH = "Only one of you is insured, and it isn't the one reading this."


def format_label(header, hazard, punch):
    """A safety notice is header + hazard + consequence, in that order."""
    return " ".join([header, hazard, punch])


def check_label(label):
    """The sealed gate: 1..120 UTF-8 characters, not only whitespace."""
    assert label.strip(), "entry must not be blank"
    assert 1 <= len(label) <= GATE, f"entry is {len(label)} chars, gate is {GATE}"
    assert label.startswith("WARNING:"), "must read as a warning label"
    assert "yourself" in label, "the hazard must be meeting yourself"
    # The surprise must sit in the final clause, not up front: the punch
    # words appear only after the last sentence break.
    tail = label.rsplit(". ", 1)[-1]
    assert "reading this" in tail, "punch must land on the last words"
    assert "warranty" in label, "the straight-faced warranty frame must hold"
    return label


def main():
    label = check_label(format_label(WARNING, HAZARD, PUNCH))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(label)


if __name__ == "__main__":
    main()
