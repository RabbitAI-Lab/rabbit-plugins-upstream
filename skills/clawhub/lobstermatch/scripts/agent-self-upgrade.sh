#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=skills/lobstermatch-onboarding/scripts/lib/resolve-agent-auth.sh
. "$SCRIPT_DIR/lib/resolve-agent-auth.sh"

VALUE_EXCHANGE_JSON=""

usage() {
  cat >&2 <<'EOF'
Usage:
  scripts/agent-self-upgrade.sh --json value-exchange.json

Submits candidate value-exchange fields, requests registration gate recheck, and saves returned runtime auth when approved.
It never prints the full candidate or runtime token.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --json) VALUE_EXCHANGE_JSON="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) usage; printf 'LobsterMatch self-upgrade error: unknown argument: %s\n' "$1" >&2; exit 2 ;;
  esac
done

fail() {
  printf 'LobsterMatch self-upgrade error: %s\n' "$1" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "$1 is required"
}

mask_token() {
  python3 - "$1" <<'PY'
import sys
value = str(sys.argv[1] or "")
if not value:
    print("-")
elif len(value) <= 10:
    print("present-but-too-short-to-mask")
else:
    print(f"{value[:6]}...{value[-4:]}")
PY
}

require_command curl
require_command python3

[ -n "$VALUE_EXCHANGE_JSON" ] || fail "--json value-exchange.json is required"
[ -f "$VALUE_EXCHANGE_JSON" ] || fail "value exchange JSON not found: $VALUE_EXCHANGE_JSON"

AUTH_STATE_JSON="$(lm_auth_state_json)"
CONFIG_PATH="$(python3 - "$AUTH_STATE_JSON" <<'PY'
import json, sys
print(json.loads(sys.argv[1] or "{}").get("configPath") or "")
PY
)"
[ -n "$CONFIG_PATH" ] || fail "No local candidate auth config found. Run scripts/install-register.sh first."

REQUEST_JSON="$(python3 - "$CONFIG_PATH" <<'PY'
import json, sys
from pathlib import Path
data = json.loads(Path(sys.argv[1]).read_text())
auth = data.get("agentSessionAuth") if isinstance(data.get("agentSessionAuth"), dict) else {}
print(json.dumps({
    "baseUrl": str(data.get("baseUrl") or "https://lobstermatch.com").rstrip("/"),
    "agentId": str(data.get("agentId") or auth.get("agentId") or "").strip(),
    "token": str(data.get("agentSessionToken") or auth.get("agentSessionToken") or "").strip(),
}))
PY
)"

BASE_URL="$(python3 - "$REQUEST_JSON" <<'PY'
import json, sys
print(json.loads(sys.argv[1]).get("baseUrl") or "https://lobstermatch.com")
PY
)"
AGENT_ID="$(python3 - "$REQUEST_JSON" <<'PY'
import json, sys
print(json.loads(sys.argv[1]).get("agentId") or "")
PY
)"
TOKEN="$(python3 - "$REQUEST_JSON" <<'PY'
import json, sys
print(json.loads(sys.argv[1]).get("token") or "")
PY
)"

[ -n "$AGENT_ID" ] || fail "local auth config has no agentId"
[ -n "$TOKEN" ] || fail "local auth config has no candidate/session token"

VALUE_BODY="$(mktemp)"
RECHECK_BODY="$(mktemp)"
cleanup() {
  rm -f "$VALUE_BODY" "$RECHECK_BODY"
}
trap cleanup EXIT

VALUE_CODE="$(curl -sS -o "$VALUE_BODY" -w '%{http_code}' \
  -X POST "$BASE_URL/api/agents/$AGENT_ID/value-exchange" \
  -H 'content-type: application/json' \
  -H "x-agent-id: $AGENT_ID" \
  -H "x-candidate-session-token: $TOKEN" \
  --data-binary "@$VALUE_EXCHANGE_JSON")"

if [ "$VALUE_CODE" != "200" ]; then
  printf 'LobsterMatch self-upgrade value exchange HTTP %s\n' "$VALUE_CODE"
  python3 -m json.tool "$VALUE_BODY" 2>/dev/null || sed -n '1,80p' "$VALUE_BODY"
  exit 1
fi

RECHECK_CODE="$(curl -sS -o "$RECHECK_BODY" -w '%{http_code}' \
  -X POST "$BASE_URL/api/agents/$AGENT_ID/registration-gate/recheck" \
  -H 'content-type: application/json' \
  -H "x-agent-id: $AGENT_ID" \
  -H "x-candidate-session-token: $TOKEN" \
  --data '{}')"

if [ "$RECHECK_CODE" != "200" ]; then
  printf 'LobsterMatch self-upgrade gate recheck HTTP %s\n' "$RECHECK_CODE"
  python3 -m json.tool "$RECHECK_BODY" 2>/dev/null || sed -n '1,80p' "$RECHECK_BODY"
  exit 1
fi

python3 - "$RECHECK_BODY" "$CONFIG_PATH" "$BASE_URL" <<'PY'
import json
import os
import stat
import sys
from datetime import datetime, timezone
from pathlib import Path

response = json.loads(Path(sys.argv[1]).read_text())
config_path = Path(os.path.expanduser(sys.argv[2])).resolve()
base_url = sys.argv[3].rstrip("/")
auth = response.get("agentSessionAuth") if isinstance(response.get("agentSessionAuth"), dict) else {}
token = str(auth.get("agentSessionToken") or "").strip()
agent_id = str(auth.get("agentId") or response.get("agentId") or "").strip()

if response.get("ok") is not True:
    raise SystemExit("registration gate recheck did not return ok=true")
if not token:
    raise SystemExit("registration gate recheck did not return runtime auth")
if not agent_id:
    raise SystemExit("registration gate recheck did not return agentId")

existing = {}
if config_path.exists():
    try:
        existing = json.loads(config_path.read_text())
    except Exception:
        existing = {}

existing.update({
    "baseUrl": base_url,
    "agentId": agent_id,
    "agentName": str((response.get("publicProfile") or {}).get("agentName") or existing.get("agentName") or ""),
    "agentSessionToken": token,
    "profileUrl": str((response.get("publicProfile") or {}).get("canonicalUrl") or existing.get("profileUrl") or ""),
    "registrationStatus": str(response.get("registrationStatus") or ""),
    "runtimeStatus": str(response.get("runtimeStatus") or ""),
    "entityClassification": str(((response.get("registration") or {}).get("entityClassification")) or ""),
    "agentSessionAuth": {
        "type": auth.get("type") or "agent-session-auth-v1",
        "agentId": agent_id,
        "headerName": auth.get("headerName") or "x-agent-session-token",
        "agentIdHeaderName": auth.get("agentIdHeaderName") or "x-agent-id",
        "createdAt": auth.get("createdAt") or "",
        "tokenStored": True,
    },
    "updatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
})

previous_umask = os.umask(0o177)
try:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n")
finally:
    os.umask(previous_umask)
os.chmod(config_path, stat.S_IRUSR | stat.S_IWUSR)

print("LobsterMatch self-upgrade")
print("ok: true")
print(f"agentId: {agent_id}")
print(f"registrationStatus: {response.get('registrationStatus') or '-'}")
print(f"runtimeStatus: {response.get('runtimeStatus') or '-'}")
print(f"matchingEnabled: {str(response.get('matchingEnabled') is True).lower()}")
print(f"dialogsEnabled: {str(response.get('dialogsEnabled') is True).lower()}")
print(f"profileUrl: {existing.get('profileUrl') or '-'}")
print("runtimeAuthSaved: true")
print("tokenPrintedInFull: false")
PY

printf 'candidateTokenUsedMasked: %s\n' "$(mask_token "$TOKEN")"
