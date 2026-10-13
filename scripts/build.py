#!/usr/bin/env python3
"""Build distributable versions of the skill from SKILL.md and references/.

Outputs (written to dist/):
  PROMPT.md         one paste-in prompt for ChatGPT, Gemini, Grok, any chat tool
  stop-vague.mdc    Cursor rule
  stop-vague.zip    upload bundle for claude.ai and other skill uploaders

Usage:
  python3 scripts/build.py           write dist/
  python3 scripts/build.py --check   fail if dist/ is out of date (for CI)
"""
import re
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKILL = ROOT / "SKILL.md"
REFS = ROOT / "references"

# Examples inlined into the paste-in prompt (by example number).
INLINE_EXAMPLES = [1, 2, 3, 6, 11]

PROMPT_INTRO = (
    "You are a feedback editor. When I paste workplace feedback "
    "(performance reviews, 1:1 notes, peer feedback, promotion write-ups), "
    "follow the instructions below exactly.\n"
)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).lstrip("\n")


def description() -> str:
    m = re.search(r"^description: (.+)$", SKILL.read_text(encoding="utf-8"), flags=re.M)
    return m.group(1).strip() if m else "Sharpen vague workplace feedback"


def examples_block() -> str:
    md = (REFS / "examples.md").read_text(encoding="utf-8")
    out = []
    for n in INLINE_EXAMPLES:
        m = re.search(
            rf"^## Example {n}: .*?\nType: .*?\nBefore: (.+?)\nAfter: (.+?)\n",
            md,
            flags=re.M | re.S,
        )
        if m:
            out.append(f"Before: {m.group(1).strip()}\nAfter: {m.group(2).strip()}")
    return "\n\n".join(out)


def build_prompt() -> str:
    body = strip_frontmatter(SKILL.read_text(encoding="utf-8"))
    # The skill body points at reference files; in a single file they are inlined.
    body = re.sub(r"\n## References\n.*\Z", "\n", body, flags=re.S)
    phrases = strip_title((REFS / "phrases.md").read_text(encoding="utf-8"))
    structures = strip_title((REFS / "structures.md").read_text(encoding="utf-8"))
    return (
        PROMPT_INTRO
        + "\n"
        + body.rstrip()
        + "\n\n## Phrases to catch\n\n"
        + phrases.rstrip()
        + "\n\n## Structural patterns to avoid\n\n"
        + structures.rstrip()
        + "\n\n## Examples\n\n"
        + examples_block()
        + "\n"
    )


def strip_title(text: str) -> str:
    return re.sub(r"\A# .*\n+", "", text, count=1)


def build_mdc(prompt: str) -> str:
    return (
        "---\n"
        f"description: {description()}\n"
        "globs:\n"
        "alwaysApply: false\n"
        "---\n\n"
        + prompt
    )


def build_zip(path: Path) -> None:
    files = [SKILL] + sorted(REFS.glob("*.md"))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            rel = f.relative_to(ROOT)
            info = zipfile.ZipInfo(f"stop-vague/{rel.as_posix()}", (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes())


def build_all(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt()
    (out / "PROMPT.md").write_text(prompt, encoding="utf-8")
    (out / "stop-vague.mdc").write_text(build_mdc(prompt), encoding="utf-8")
    build_zip(out / "stop-vague.zip")


def main() -> int:
    if "--check" in sys.argv:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp)
            build_all(fresh)
            stale = []
            for f in sorted(fresh.iterdir()):
                cur = DIST / f.name
                if not cur.exists() or cur.read_bytes() != f.read_bytes():
                    stale.append(f.name)
            if stale:
                print("dist/ is out of date: " + ", ".join(stale))
                print("Run: python3 scripts/build.py")
                return 1
            print("dist/ is up to date")
            return 0
    build_all(DIST)
    print(f"Wrote {', '.join(sorted(p.name for p in DIST.iterdir()))} to {DIST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
