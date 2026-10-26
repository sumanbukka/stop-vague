# Security

## What this project is

stop-vague is prompt text: `SKILL.md`, the Markdown files under `references/`, and files built from them in `dist/`. It has no server, no database and no accounts.

## What it does and does not do

- `scripts/install.sh` is the only executable shipped for users. It clones this repo with `git clone --depth 1` and copies `SKILL.md` and `references/` into `~/.claude/skills/stop-vague` (or `./.claude/skills/stop-vague` with `--project`).
- Inside the script, the only network call is that clone. Nothing else is downloaded, uploaded or sent anywhere.
- Nothing is stored by this project. It writes no logs and keeps no history.
- `scripts/build.py` and `tests/lint_examples.py` are for contributors and CI. They are not part of the install.
- Feedback you paste goes to the AI tool you already use, under that provider's terms.

You can read `scripts/install.sh` before running it. It is short.

## Reporting a problem

Open an issue at https://github.com/sumanbukka/stop-vague/issues. Do not put real names, feedback text or anything private in the issue. If something is sensitive, ask in the issue for a way to share it, without details. Replies happen in the issue.
