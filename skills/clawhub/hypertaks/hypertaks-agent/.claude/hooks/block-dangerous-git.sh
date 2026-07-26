#!/bin/bash
# PreToolUse guardrail for hypertaks-agent.
# Blocks:
#   1. git reset --hard
#   2. git clean (any force/dir variant)
#   3. Recursive/any deletes (Remove-Item, rm, rmdir, rd, del) that touch a
#      .skills junction path: .claude/skills, .openclaw/skills,
#      .copilot/skills, .kilocode/skills
# Works without jq: falls back to matching the raw JSON payload.

INPUT=$(cat)

if command -v jq >/dev/null 2>&1; then
  COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')
else
  # No jq: match against the raw JSON. Path separators may appear as
  # JSON-escaped backslashes (\\), which the regexes below account for.
  COMMAND=$INPUT
fi

block() {
  echo "BLOCKED: command matches guarded pattern '$1'. The user has prevented you from doing this. If it is truly needed, ask the user to run it manually." >&2
  exit 2
}

# --- destructive git commands ---
printf '%s' "$COMMAND" | grep -qiE 'reset[[:space:]]+--hard' && block "git reset --hard"
printf '%s' "$COMMAND" | grep -qiE 'git[[:space:]]+clean([[:space:]"'"'"']|$)|git[[:space:]][^;|&]*[[:space:]]clean[[:space:]]+-' && block "git clean"

# --- deletes touching a .skills junction path ---
# Separator matches /, \ and JSON-escaped \\.
SKILLS_RE='\.(claude|openclaw|copilot|kilocode)[/\\]+skills'
DELETE_RE='remove-item|-recurse|rmdir|(^|[;&|[:space:]"'"'"'(])(rm|rd|ri|del)[[:space:]]'

if printf '%s' "$COMMAND" | grep -qiE "$SKILLS_RE"; then
  printf '%s' "$COMMAND" | grep -qiE "$DELETE_RE" && block "delete touching a .skills junction"
fi

exit 0
