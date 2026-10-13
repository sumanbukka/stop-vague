#!/usr/bin/env python3
"""Lint references/examples.md.

Checks every example's After text for:
  1. banned vague phrases
  2. a specific anchor (a number, number word, day, or month)
  3. the declared Impact phrase actually appearing in the After text
  4. the declared Next phrase actually appearing in the After text
  5. no em dashes anywhere in the file

Exit code 1 if any check fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "references" / "examples.md"

BANNED = [
    "great job", "good work", "rockstar", "needs improvement", "team player",
    "step up", "level up", "attitude", "initiative", "ownership",
    "stakeholder management", "strategic", "leverage", "bandwidth",
    "move the needle", "synergy", "think bigger", "raise the bar",
    "always", "never", "often", "sometimes", "occasionally", "a lot",
    "a bit", "somewhat", "quite", "fairly", "kind of", "very", "really",
]

NUMBER_WORDS = (
    "one two three four five six seven eight nine ten twice thrice "
    "monday tuesday wednesday thursday friday saturday sunday "
    "january february march april may june july august september "
    "october november december noon overnight"
).split()


def has_anchor(text: str) -> bool:
    if re.search(r"\d", text):
        return True
    words = set(re.findall(r"[a-z]+", text.lower()))
    return any(w in words for w in NUMBER_WORDS)


def parse(md: str):
    blocks = re.split(r"^## Example ", md, flags=re.M)[1:]
    for block in blocks:
        title = block.splitlines()[0].strip()
        fields = {}
        for key, pat in (
            ("Before", r"^\*\*Before:\*\* (.+)$"),
            ("After", r"^\*\*After:\*\* (.+)$"),
            ("Impact", r"^- \*\*Impact:\*\* (.+)$"),
            ("Next", r"^- \*\*Next step:\*\* (.+)$"),
        ):
            m = re.search(pat, block, flags=re.M)
            fields[key] = m.group(1).strip() if m else None
        yield title, fields


def main() -> int:
    md = EXAMPLES.read_text(encoding="utf-8")
    failures = []

    if "—" in md:
        failures.append("file: contains an em dash")

    count = 0
    for title, f in parse(md):
        count += 1
        label = f"Example {title}"
        for key in ("Before", "After", "Impact", "Next"):
            if not f[key]:
                failures.append(f"{label}: missing {key}")
        if not f["After"]:
            continue
        after = f["After"]
        low = after.lower()
        for phrase in BANNED:
            if re.search(rf"\b{re.escape(phrase)}\b", low):
                failures.append(f"{label}: banned phrase '{phrase}' in After")
        if not has_anchor(after):
            failures.append(f"{label}: After has no number, day, or month")
        if f["Impact"] and f["Impact"] not in after:
            failures.append(f"{label}: Impact phrase not found in After")
        if f["Next"] and f["Next"] not in after:
            failures.append(f"{label}: Next phrase not found in After")
        if f["Before"] and f["Before"] == after:
            failures.append(f"{label}: After equals Before")

    if count < 20:
        failures.append(f"only {count} examples, need at least 20")

    if failures:
        print(f"FAIL ({len(failures)} problems across {count} examples)")
        for line in failures:
            print(" -", line)
        return 1
    print(f"PASS: {count} examples clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
