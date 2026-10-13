#!/usr/bin/env bash
# Install stop-vague as a Claude Code skill.
#
#   curl -fsSL https://raw.githubusercontent.com/sumanbukka/stop-vague/main/scripts/install.sh | bash
#   curl -fsSL .../install.sh | bash -s -- --project     # install into ./.claude/skills
#
# Override the source repo with STOP_VAGUE_REPO (any git URL or local path).
set -euo pipefail

REPO="${STOP_VAGUE_REPO:-https://github.com/sumanbukka/stop-vague.git}"
MODE="user"

for arg in "$@"; do
  case "$arg" in
    --project) MODE="project" ;;
    --user) MODE="user" ;;
    -h|--help)
      echo "Usage: install.sh [--user | --project]"
      echo "  --user     install to ~/.claude/skills/stop-vague (default)"
      echo "  --project  install to ./.claude/skills/stop-vague"
      exit 0
      ;;
    *) echo "Unknown option: $arg" >&2; exit 1 ;;
  esac
done

if ! command -v git >/dev/null 2>&1; then
  echo "git is required. Install git, or download dist/stop-vague.zip from the repo instead." >&2
  exit 1
fi

if [ "$MODE" = "project" ]; then
  DEST="$PWD/.claude/skills/stop-vague"
else
  DEST="$HOME/.claude/skills/stop-vague"
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone --quiet --depth 1 "$REPO" "$TMP/src"

if [ ! -f "$TMP/src/SKILL.md" ]; then
  echo "SKILL.md not found in $REPO" >&2
  exit 1
fi

mkdir -p "$DEST"
cp "$TMP/src/SKILL.md" "$DEST/SKILL.md"
rm -rf "$DEST/references"
cp -R "$TMP/src/references" "$DEST/references"

echo "Installed stop-vague to $DEST"
echo "Try it: ask Claude Code to \"use stop-vague on this feedback: <paste feedback>\""
