#!/usr/bin/env bash
# analyze-skill.sh — Quick structural analysis of a SKILL.md file
# Usage: ./analyze-skill.sh <path-to-SKILL.md>
#
# Checks:
# - File exists and is non-empty
# - Has YAML frontmatter
# - Has required sections (Overview/When to Use/Steps/Examples)
# - Word count and token estimate
# - Section count and structure

set -euo pipefail

SKILL_PATH="${1:-}"

if [[ -z "$SKILL_PATH" ]]; then
  echo "Usage: $0 <path-to-SKILL.md>"
  exit 1
fi

if [[ ! -f "$SKILL_PATH" ]]; then
  echo "ERROR: File not found: $SKILL_PATH"
  exit 1
fi

echo "=== Skill Structure Analysis ==="
echo "File: $SKILL_PATH"
echo ""

# Basic stats
TOTAL_LINES=$(wc -l < "$SKILL_PATH")
TOTAL_CHARS=$(wc -c < "$SKILL_PATH")
TOTAL_WORDS=$(wc -w < "$SKILL_PATH")
TOKEN_ESTIMATE=$((TOTAL_WORDS * 4 / 3))  # rough estimate

echo "📊 Basic Stats:"
echo "  Lines: $TOTAL_LINES"
echo "  Words: $TOTAL_WORDS"
echo "  Chars: $TOTAL_CHARS"
echo "  Token estimate: ~$TOKEN_ESTIMATE"
echo ""

# Frontmatter check
echo "📋 Frontmatter:"
if head -1 "$SKILL_PATH" | grep -q "^---"; then
  echo "  ✅ YAML frontmatter detected"
  # Extract name
  NAME=$(grep -m1 "^name:" "$SKILL_PATH" | sed 's/name: *"*//;s/"*$//' || echo "N/A")
  DESC=$(grep -m1 "^description:" "$SKILL_PATH" | sed 's/description: *"*//;s/"*$//' | head -c 80 || echo "N/A")
  echo "  Name: $NAME"
  echo "  Description: ${DESC}..."
else
  echo "  ❌ No YAML frontmatter"
fi
echo ""

# Section analysis
echo "📑 Sections (H1-H3):"
SECTIONS=$(grep -n "^##" "$SKILL_PATH" || true)
SECTION_COUNT=$(echo "$SECTIONS" | grep -c "^" || echo "0")
echo "  Total sections: $SECTION_COUNT"
echo "$SECTIONS" | while IFS= read -r line; do
  if [[ -n "$line" ]]; then
    LINENUM=$(echo "$line" | cut -d: -f1)
    TITLE=$(echo "$line" | cut -d: -f2- | sed 's/^#* *//')
    LEVEL=$(echo "$line" | cut -d: -f2- | grep -o "^#" | wc -c)
    INDENT=""
    for ((i=1; i<LEVEL; i++)); do INDENT+="  "; done
    echo "  ${INDENT}L${LINENUM}: ${TITLE}"
  fi
done
echo ""

# Required sections check
echo "🔍 Required Sections Check:"
check_section() {
  local pattern="$1"
  local label="$2"
  if grep -qi "$pattern" "$SKILL_PATH"; then
    echo "  ✅ $label"
  else
    echo "  ❌ $label — MISSING"
  fi
}

check_section "overview\|what\|about" "Overview/About section"
check_section "trigger\|when.*use\|activate" "Trigger/When to Use section"
check_section "step\|workflow\|procedure\|how" "Steps/Workflow section"
check_section "example\|sample\|demo" "Examples section"
check_section "error\|troubleshoot\|fallback\|fail" "Error handling section"
check_section "depend\|prerequis\|require\|install" "Dependencies section"
check_section "output\|result\|deliverable" "Output specification"
check_section "reference\|see also\|link\|resource" "References section"
echo ""

# Code blocks
BACKTICKS='```'
CODE_BLOCKS=$(grep -c "^${BACKTICKS}" "$SKILL_PATH" || echo "0")
CODE_BLOCKS=$((CODE_BLOCKS / 2))
echo "📦 Code Blocks: $CODE_BLOCKS"

# Tables
TABLES=$(grep -c "^|" "$SKILL_PATH" || echo "0")
echo "📊 Tables: $TABLES rows"

# Checklists
CHECKLISTS=$(grep -cE '\- \[ \]|✅|❌' "$SKILL_PATH" || echo "0")
echo "☑️  Checklist items: $CHECKLISTS"

echo ""
echo "=== Analysis Complete ==="
