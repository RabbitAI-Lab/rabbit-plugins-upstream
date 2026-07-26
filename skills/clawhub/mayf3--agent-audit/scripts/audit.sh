#!/bin/bash
# agent-audit — Check all agent ADC credentials, roles, and workspace health
# Usage: bash audit.sh [--check-login] [--check-roles] [--check-souls] [--all]
# Output: human-readable report

set -euo pipefail

ADC_HOST="${ADC_HOST:-8.163.44.127}"
ADC_API="http://${ADC_HOST}:4000/api"
GROUPS_DIR="${GROUPS_DIR:-$HOME/.openclaw/groups}"
OPENCLAW_JSON="${OPENCLAW_JSON:-$HOME/.openclaw/openclaw.json}"
REPORT_DIR="/tmp/agent-audit-$(date +%Y%m%d_%H%M)"
mkdir -p "$REPORT_DIR"

DO_LOGIN=false
DO_ROLES=false
DO_SOULS=false
[ $# -eq 0 ] && DO_ALL=true || DO_ALL=false

for arg in "$@"; do
  case "$arg" in
    --check-login) DO_LOGIN=true ;;
    --check-roles) DO_ROLES=true ;;
    --check-souls) DO_SOULS=true ;;
    --all) DO_ALL=true ;;
  esac
done

$DO_ALL && { DO_LOGIN=true; DO_ROLES=true; DO_SOULS=true; }

# ─── Helpers ───
get_env() {
  local env_file="$1" key="$2"
  grep -m1 "^${key}=" "$env_file" 2>/dev/null | sed "s/^${key}=//" | tr -d '"'"'"
}

test_login() {
  local email="$1" password="$2"
  local result
  result=$(ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "root@$ADC_HOST" \
    "curl -s -m 10 '$ADC_API/auth/login' -H 'Content-Type: application/json' -d '{\"email\":\"$email\",\"password\":\"$password\"}'" 2>/dev/null || echo '{}')
  if echo "$result" | grep -q '"accessToken"'; then
    echo "$result" | python3 -c "import sys,json; d=json.loads(sys.stdin.read()); print(d['user']['role'])" 2>/dev/null
  else
    echo "FAIL:$(echo "$result" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('message','unknown'))" 2>/dev/null)"
  fi
}

# ─── 1. Check ADC Login ───
if $DO_LOGIN; then
  echo "=== 🔐 ADC Login Check ==="
  total=0; ok=0; fail=0; weak=0
  while IFS= read -r env_file; do
    email=$(get_env "$env_file" "ADC_EMAIL")
    [ -z "$email" ] && email=$(get_env "$env_file" "ADC_EMAIL")
    [ -z "$email" ] && continue
    password=$(get_env "$env_file" "ADC_PASSWORD")
    [ -z "$password" ] && password=$(get_env "$env_file" "ADC_PASSWORD")
    [ -z "$password" ] && continue

    ws=$(basename "$(dirname "$env_file")")
    total=$((total+1))

    # Check for known weak passwords
    is_weak=false
    for weak_pw in "agent2026" "devtools-agent2026!" "itops-agent2026!"; do
      if [ "$password" = "$weak_pw" ]; then is_weak=true; weak=$((weak+1)); break; fi
    done

    result=$(test_login "$email" "$password")
    if [[ "$result" == FAIL:* ]]; then
      fail=$((fail+1))
      echo "  ❌ $ws ($email): ${result#FAIL:}"
    else
      ok=$((ok+1))
      weak_tag=""
      $is_weak && weak_tag=" ⚠️ DEFAULT PASSWORD"
      echo "  ✅ $ws ($email): role=$result$weak_tag"
    fi
  done < <(find "$GROUPS_DIR" -maxdepth 2 -name ".env" -not -path "*/ARCHIVE/*" -not -path "*/.trash/*" 2>/dev/null | sort)
  echo ""
  echo "  Total: $total | OK: $ok | Failed: $fail | Weak: $weak"
  echo ""
fi

# ─── 2. Check Role Mismatch ───
if $DO_ROLES; then
  echo "=== 🏷️ Role Mismatch Check ==="
  mismatches=0
  while IFS= read -r env_file; do
    email=$(get_env "$env_file" "ADC_EMAIL")
    [ -z "$email" ] && email=$(get_env "$env_file" "ADC_EMAIL")
    [ -z "$email" ] && continue
    password=$(get_env "$env_file" "ADC_PASSWORD")
    [ -z "$password" ] && password=$(get_env "$env_file" "ADC_PASSWORD")
    [ -z "$password" ] && continue

    ws=$(basename "$(dirname "$env_file")")
    result=$(test_login "$email" "$password")
    [[ "$result" == FAIL:* ]] && continue

    adc_role="$result"
    # Get expected role from IDENTITY.md or SOUL.md
    soul_file="$(dirname "$env_file")/SOUL.md"
    if [ -f "$soul_file" ]; then
      # Detect if agent is doing ADC dev work when it shouldn't be
      if grep -qi "adc.*开发\|adc.*开发\|需求.*审批\|ADC.*patrol\|ADC.*巡检" "$soul_file" 2>/dev/null; then
        if [ "$adc_role" != "admin" ] && [ "$adc_role" != "cto_agent" ]; then
          echo "  ⚠️ $ws: SOUL.md mentions ADC work but role=$adc_role (expected admin/cto_agent)"
          mismatches=$((mismatches+1))
        fi
      fi
    fi
  done < <(find "$GROUPS_DIR" -maxdepth 2 -name ".env" -not -path "*/ARCHIVE/*" -not -path "*/.trash/*" 2>/dev/null | sort)
  [ $mismatches -eq 0 ] && echo "  ✅ No role mismatches detected"
  echo ""
fi

# ─── 3. Check SOUL.md Templates ───
if $DO_SOULS; then
  echo "=== 🧠 SOUL.md Template Check ==="
  default_count=0
  while IFS= read -r soul_file; do
    if head -5 "$soul_file" 2>/dev/null | grep -q "You're not a chatbot"; then
      ws=$(basename "$(dirname "$(dirname "$soul_file")")")
      [ "$(basename "$(dirname "$soul_file")")" != "workspace-"* ] && ws=$(basename "$(dirname "$soul_file")")
      echo "  ⚠️ $ws: Using default SOUL.md template"
      default_count=$((default_count+1))
    fi
  done < <(find "$GROUPS_DIR" -maxdepth 3 -name "SOUL.md" -not -path "*/ARCHIVE/*" -not -path "*/.trash/*" 2>/dev/null | sort)
  [ $default_count -eq 0 ] && echo "  ✅ All agents have custom SOUL.md"
  echo "  Default templates: $default_count"
  echo ""
fi

echo "=== ✅ Audit complete ==="
echo "Report saved to: $REPORT_DIR"
