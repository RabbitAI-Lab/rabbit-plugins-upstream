#!/bin/bash
# Skill Vetter — Security audit for ClawHub skills
# Usage: bash scripts/vet.sh <slug>
# Requires: clawhub CLI

set -e

SLUG="${1}"

if [ -z "$SLUG" ]; then
  echo "Usage: bash scripts/vet.sh <slug>"
  exit 1
fi

echo "=== Security Vet: $SLUG ==="
echo ""

# Get metadata
echo "[1/5] Fetching metadata..."
META=$(clawhub inspect "$SLUG" 2>/dev/null)
VERSION=$(echo "$META" | grep "^Latest:" | awk '{print $2}')
UPDATED=$(echo "$META" | grep "^Updated:" | awk '{print $2}')
SECURITY=$(echo "$META" | grep "^Security:" | awk '{print $2}')
LICENSE=$(echo "$META" | grep "^License:" | awk '{print $2,$3,$4}')
OWNER=$(echo "$META" | grep "^Owner:" | awk '{print $2}')

echo "  Version: ${VERSION:-latest}"
echo "  Updated: ${UPDATED:-unknown}"
echo "  Owner: ${OWNER:-unknown}"
echo "  Security: ${SECURITY:-not checked}"
echo "  License: ${LICENSE:-unknown}"
echo ""

# Score
SCORE=0
REASONS=""

# Check 1: ClawHub security scan
if [ "$SECURITY" = "CLEAN" ]; then
  SCORE=$((SCORE+2))
  echo "[2/5] ClawHub Security Scan: CLEAN (+2)"
elif [ "$SECURITY" = "FLAG" ]; then
  SCORE=$((SCORE-3))
  REASONS="${REASONS} clawhub-flagged;"
  echo "[2/5] ClawHub Security Scan: FLAG (-3)"
else
  echo "[2/5] ClawHub Security Scan: ${SECURITY:-not available}"
fi

# Check 2: Credential storage — only flag actual hardcoded values, not mentions
echo ""
echo "[3/5] Checking credential storage..."
FILES=$(clawhub inspect "$SLUG" --files 2>/dev/null | grep -E "^scripts/|^hooks/" | awk '{print $1}')

CRED_FLAG=0
NET_FLAG=0
DESTRUCT_FLAG=0

for file in $FILES; do
  CONTENT=$(clawhub inspect "$SLUG" --file "$file" 2>/dev/null)
  
  # Only flag actual hardcoded credential VALUES (not env var references)
  # Look for: API_KEY="sk_live..." or api_key = "sk_live..." or similar
  if echo "$CONTENT" | grep -E 'API_KEY\s*=\s*"sk_[a-zA-Z0-9]{20,}' > /dev/null 2>&1; then
    CRED_FLAG=1
  fi
  if echo "$CONTENT" | grep -E 'PASSWORD\s*=\s*"[^"]+' > /dev/null 2>&1; then
    CRED_FLAG=1
  fi
  if echo "$CONTENT" | grep -E 'TOKEN\s*=\s*"[^"]{20,}' > /dev/null 2>&1; then
    CRED_FLAG=1
  fi
  
  # Network check
  if echo "$CONTENT" | grep -E "curl |wget |fetch\(|requests\.post|requests\.get" > /dev/null 2>&1; then
    NET_FLAG=1
  fi
  
  # Destructive ops check
  if echo "$CONTENT" | grep -E "rm -rf|chmod 777|sudo |eval |exec " > /dev/null 2>&1; then
    DESTRUCT_FLAG=1
  fi
done

if [ $CRED_FLAG -eq 1 ]; then
  SCORE=$((SCORE-2))
  REASONS="${REASONS} plaintext-credentials;"
  echo "  Credential storage: FLAG (-2) — hardcoded key detected"
else
  SCORE=$((SCORE+1))
  echo "  Credential storage: CLEAN (+1)"
fi

if [ $NET_FLAG -eq 1 ]; then
  SCORE=$((SCORE-1))
  REASONS="${REASONS} network-calls;"
  echo "  Network access: FLAG (-1) — review for exfil"
else
  SCORE=$((SCORE+1))
  echo "  Network access: CLEAN (+1)"
fi

# Check 3: File system
echo ""
echo "[4/5] Checking filesystem operations..."
if [ $DESTRUCT_FLAG -eq 1 ]; then
  SCORE=$((SCORE-2))
  REASONS="${REASONS} destructive-ops;"
  echo "  File system: FLAG (-2)"
else
  SCORE=$((SCORE+1))
  echo "  File system: CLEAN (+1)"
fi

# Check 4: SKILL.md quality
echo ""
echo "[5/5] Checking SKILL.md quality..."
SKILL_MD=$(clawhub inspect "$SLUG" --file SKILL.md 2>/dev/null)
DESC_LEN=$(echo "$SKILL_MD" | wc -c 2>/dev/null || echo 0)
if echo "$SKILL_MD" | grep -qi "requires\|permission\|tool\|node\|bin"; then
  echo "  Permission docs: CLEAR (+1)"
  SCORE=$((SCORE+1))
else
  echo "  Permission docs: VAGUE"
fi
if [ "$DESC_LEN" -lt 500 ]; then
  echo "  Documentation: MINIMAL (${DESC_LEN} bytes)"
  SCORE=$((SCORE+1))
elif [ "$DESC_LEN" -gt 3000 ]; then
  echo "  Documentation: DETAILED (+1)"
  SCORE=$((SCORE+1))
fi

# Verdict
echo ""
echo "=============================="
echo "FINAL SCORE: $SCORE / 7"
echo "=============================="

if [ $SCORE -ge 5 ]; then
  echo ""
  echo "VERDICT: Install ✅"
  echo "Reason: Security checks passed — safe to install"
elif [ $SCORE -ge 3 ]; then
  echo ""
  echo "VERDICT: Caution ⚠️"
  echo "Reason: Review flagged items before installing"
else
  echo ""
  echo "VERDICT: Reject ❌"
  echo "Reason: Security flags detected — do not install"
fi

if [ -n "$REASONS" ]; then
  echo "Flags:$REASONS"
fi

echo ""
echo "Vet complete."