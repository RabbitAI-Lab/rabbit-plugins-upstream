#!/usr/bin/env bash
# daily-digest helper: validate a SKILL.md frontmatter
set -euo pipefail

SKILL_FILE="${1:-SKILL.md}"
if [ ! -f "$SKILL_FILE" ]; then
  echo "ERROR: $SKILL_FILE not found"
  exit 1
fi

# Check YAML frontmatter
FIRST_LINE=$(head -1 "$SKILL_FILE")
if [ "$FIRST_LINE" != "---" ]; then
  echo "ERROR: Missing YAML frontmatter delimiter (---)"
  exit 1
fi

# Extract frontmatter
FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$SKILL_FILE" | sed '1d;$d')

# Validate required fields
for field in "name:" "description:" ; do
  if ! echo "$FRONTMATTER" | grep -q "$field"; then
    echo "ERROR: Missing required field: $field"
    exit 1
  fi
done

NAME=$(echo "$FRONTMATTER" | grep "^name:" | head -1 | sed 's/name: *//')
echo "✅ Skill validated: $NAME"
