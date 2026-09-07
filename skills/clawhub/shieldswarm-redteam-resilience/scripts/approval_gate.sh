#!/bin/bash
# ShieldSwarm approval_gate.sh — append-only approval log with separation-of-duties.
# Portable: bash 3.2+ (no associative arrays), coreutils only, no network.
#
# Contract (machine-readable):
#   record: approval_gate.sh --scope TEXT --risk {low|medium|high}
#                  --rollback-owner NAME --approver NAME [--id ID] [--file PATH]
#   check:  approval_gate.sh --file PATH --check [--id ID] [--scope TEXT]
#   log:    JSONL, one object per line:
#           {"id":..,"ts":..,"scope":..,"risk":..,"rollback_owner":..,"approver":..,"operator":..}
#   output: approval_id=<id>            (record ok)
#           approval_status=found ...   (check ok)
#   exit:   0=ok, 1=blocked or not found, 2=usage error
# Rules: risk=high REQUIRES approver != rollback_owner AND approver != operator.
set -eu

SCOPE="" RISK="" OWNER="" APPROVER="" ID="" FILE="" CHECK=0

usage() {
  cat <<'EOF'
Usage:
  approval_gate.sh --scope TEXT --risk {low|medium|high} --rollback-owner NAME \
      --approver NAME [--id ID] [--file PATH]
  approval_gate.sh --file PATH --check [--id ID] [--scope TEXT]
Records an approval in an append-only JSONL file (atomic write: tmp + mv).
Separation of duties: for risk=high, approver must differ from both the
rollback owner and the current operator (whoami).
Output (stdout): approval_id=<id> or approval_status=found|missing
Exit codes: 0=ok, 1=blocked/not found, 2=usage error
EOF
  exit 2
}

make_id() {
  # deterministic-ish unique id from time + pid + counter (no /proc dep)
  echo "appr-$(date -u +%Y%m%dT%H%M%SZ)-$$-${APPR_SEQ:-0}"
}

json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  printf '%s' "$s"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --scope) SCOPE="${2:-}"; shift 2 ;;
    --risk) RISK="${2:-}"; shift 2 ;;
    --rollback-owner) OWNER="${2:-}"; shift 2 ;;
    --approver) APPROVER="${2:-}"; shift 2 ;;
    --id) ID="${2:-}"; shift 2 ;;
    --file) FILE="${2:-}"; shift 2 ;;
    --check) CHECK=1; shift ;;
    -h|--help) usage ;;
    *) echo "error=invalid_argument arg=$1" >&2; exit 2 ;;
  esac
done

[ -n "$FILE" ] || FILE="approval.jsonl"

if [ "$CHECK" -eq 1 ]; then
  [ -f "$FILE" ] || { echo "approval_status=missing reason=logfile_not_found file=$FILE"; exit 1; }
  if [ -n "$ID" ]; then
    if grep -q "\"id\": *\"$ID\"" "$FILE" 2>/dev/null; then
      echo "approval_status=found id=$ID"
      exit 0
    else
      echo "approval_status=missing id=$ID"
      exit 1
    fi
  elif [ -n "$SCOPE" ]; then
    if grep -q "\"scope\": *\"$SCOPE\"" "$FILE" 2>/dev/null; then
      echo "approval_status=found scope=$SCOPE"
      exit 0
    else
      echo "approval_status=missing scope=$SCOPE"
      exit 1
    fi
  else
    echo "error=missing_required_args arg=id|scope (with --check)" >&2
    exit 2
  fi
fi

# ---- record mode -------------------------------------------------------------
for req in "scope:$SCOPE" "risk:$RISK" "rollback-owner:$OWNER" "approver:$APPROVER"; do
  key="${req%%:*}"; val="${req#*:}"
  [ -n "$val" ] || { echo "error=missing_required_args arg=$key" >&2; exit 2; }
done
case "$RISK" in low|medium|high) ;;
  *) echo "error=invalid_risk value=$RISK allowed=low|medium|high" >&2; exit 2 ;;
esac

OPERATOR="$(whoami 2>/dev/null || echo unknown)"

if [ "$RISK" = "high" ]; then
  if [ "$APPROVER" = "$OWNER" ]; then
    echo "approval_status=blocked reason=approver_equals_rollback_owner approver=$APPROVER"
    exit 1
  fi
  if [ "$APPROVER" = "$OPERATOR" ]; then
    echo "approval_status=blocked reason=approver_equals_operator approver=$APPROVER"
    exit 1
  fi
fi

[ -n "$ID" ] || ID="$(make_id)"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
DIR="$(dirname "$FILE")"
mkdir -p "$DIR" 2>/dev/null || true
TMP="$(mktemp "${DIR}/.approval.XXXXXX")" || { echo "error=mktemp_failed dir=$DIR" >&2; exit 1; }
if [ -f "$FILE" ]; then cat "$FILE" > "$TMP"; fi
printf '{"id":"%s","ts":"%s","scope":"%s","risk":"%s","rollback_owner":"%s","approver":"%s","operator":"%s"}\n' \
  "$(json_escape "$ID")" "$TS" "$(json_escape "$SCOPE")" "$RISK" \
  "$(json_escape "$OWNER")" "$(json_escape "$APPROVER")" "$(json_escape "$OPERATOR")" >> "$TMP"
chmod 600 "$TMP"
mv "$TMP" "$FILE"
echo "approval_id=$ID"
echo "approval_file=$FILE"
exit 0
