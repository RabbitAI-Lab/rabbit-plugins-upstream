#!/usr/bin/env bash
# Yielding Bear — doctor/status/models/smoke/set-model/set-routing/explain CLI
# Usage: yb.sh <cmd> …
set -euo pipefail

SITE_URL="${YIELDINGBEAR_SITE_URL:-https://yieldingbear.com}"
BASE_URL="${YIELDINGBEAR_BASE_URL:-${SITE_URL}/api/v1}"
VERSION="2.3.2"
GRIZZLY="yieldingbear/grizzly-1.0g-pro"

# Build Authorization header without embedding secrets in source comments.
auth_header() {
  # $1 = raw API key
  printf 'Authorization: Bearer %s' "$1"
}

resolve_paths() {
  if [[ -n "${HERMES_HOME:-}" || -d "${HOME}/.hermes" ]]; then
    ROOT="${HERMES_HOME:-$HOME/.hermes}"
    RUNTIME=hermes
  elif [[ -n "${OPENCLAW_HOME:-}" || -d "${HOME}/.openclaw" ]]; then
    ROOT="${OPENCLAW_HOME:-$HOME/.openclaw}"
    RUNTIME=openclaw
  else
    ROOT="${HOME}/.config/yieldingbear"
    RUNTIME=shell
  fi
  if [[ "$RUNTIME" == "shell" ]]; then
    KEY_FILE="${ROOT}/secrets/yieldingbear-token"
    CONFIG_FILE="${ROOT}/yieldingbear.json"
    ENV_FILE="${ROOT}/env.sh"
  else
    KEY_FILE="${ROOT}/secrets/yieldingbear-token"
    CONFIG_FILE="${ROOT}/config/yieldingbear.json"
    ENV_FILE="${ROOT}/config/env.sh"
  fi
}

load_key() {
  resolve_paths
  if [[ -n "${YIELDINGBEAR_API_KEY:-}" ]]; then
    KEY="$YIELDINGBEAR_API_KEY"
  elif [[ -s "$KEY_FILE" ]]; then
    KEY="$(tr -d '[:space:]' < "$KEY_FILE")"
  else
    KEY=""
  fi
}

cfg_get() {
  # $1 = json key
  if [[ -f "$CONFIG_FILE" ]] && command -v python3 >/dev/null 2>&1; then
    python3 -c 'import json,sys; c=json.load(open(sys.argv[1])); print(c.get(sys.argv[2]) or "")' \
      "$CONFIG_FILE" "$1" 2>/dev/null || true
  fi
}

fetch_recs() {
  REC_HIGH="" REC_MID="" REC_LOW="" REC_ROUTER="$GRIZZLY"
  local j
  j="$(curl -sS -m 12 -H 'Accept: application/json' \
    "${SITE_URL}/api/public/routing-recommendations" 2>/dev/null || true)"
  if command -v python3 >/dev/null 2>&1 && [[ -n "$j" ]]; then
    eval "$(
      printf '%s' "$j" | python3 -c '
import json,sys,shlex
try: j=json.load(sys.stdin)
except Exception: sys.exit(0)
def q(s): return shlex.quote(str(s or ""))
print("REC_HIGH="+q(j.get("high")))
print("REC_MID="+q(j.get("mid")))
print("REC_LOW="+q(j.get("low")))
print("REC_ROUTER="+q(j.get("router_model") or "yieldingbear/grizzly-1.0g-pro"))
' 2>/dev/null || true
    )"
  fi
  [[ -n "$REC_HIGH" ]] || REC_HIGH="anthropic/claude-sonnet-4.6"
  [[ -n "$REC_MID" ]] || REC_MID="google/gemini-2.5-flash"
  [[ -n "$REC_LOW" ]] || REC_LOW="nvidia/nemotron-3-nano-30b"
  [[ -n "$REC_ROUTER" ]] || REC_ROUTER="$GRIZZLY"
  return 0
}

write_config_fields() {
  # args via env: NEW_MODE NEW_MODEL
  resolve_paths
  mkdir -p "$(dirname "$CONFIG_FILE")" 2>/dev/null || true
  fetch_recs
  if command -v python3 >/dev/null 2>&1; then
    python3 - "$CONFIG_FILE" "${NEW_MODE}" "${NEW_MODEL}" "$VERSION" "$BASE_URL" \
      "$REC_HIGH" "$REC_MID" "$REC_LOW" "$REC_ROUTER" "$KEY_FILE" <<'PY'
import json, sys
path, mode, model, ver, base, hi, mid, lo, router, keyf = sys.argv[1:11]
try:
    c = json.load(open(path))
except Exception:
    c = {}
c["version"] = ver
c["base_url"] = base
c["routing_mode"] = mode
c["default_model"] = model
c["recommended_tiers"] = {"high": hi, "mid": mid, "low": lo}
c.setdefault("fallback_models", [router, lo, "liquid/lfm-2.5-2.6b"])
c["key_file"] = keyf
json.dump(c, open(path, "w"), indent=2)
print("updated", path)
PY
  else
    cat > "$CONFIG_FILE" <<EOF
{
  "version": "${VERSION}",
  "base_url": "${BASE_URL}",
  "routing_mode": "${NEW_MODE}",
  "default_model": "${NEW_MODEL}",
  "key_file": "${KEY_FILE}"
}
EOF
  fi
  chmod 600 "$CONFIG_FILE" 2>/dev/null || true

  # env.sh
  if [[ -f "$ENV_FILE" ]]; then
    tmp="$(mktemp)"
    if grep -q 'YIELDINGBEAR_DEFAULT_MODEL=' "$ENV_FILE" 2>/dev/null; then
      sed "s|^export YIELDINGBEAR_DEFAULT_MODEL=.*|export YIELDINGBEAR_DEFAULT_MODEL=\"${NEW_MODEL}\"|" "$ENV_FILE" > "$tmp"
      mv "$tmp" "$ENV_FILE"
    else
      echo "export YIELDINGBEAR_DEFAULT_MODEL=\"${NEW_MODEL}\"" >> "$ENV_FILE"
    fi
    if grep -q 'YIELDINGBEAR_ROUTING_MODE=' "$ENV_FILE" 2>/dev/null; then
      tmp="$(mktemp)"
      sed "s|^export YIELDINGBEAR_ROUTING_MODE=.*|export YIELDINGBEAR_ROUTING_MODE=\"${NEW_MODE}\"|" "$ENV_FILE" > "$tmp"
      mv "$tmp" "$ENV_FILE"
    else
      echo "export YIELDINGBEAR_ROUTING_MODE=\"${NEW_MODE}\"" >> "$ENV_FILE"
    fi
    chmod 600 "$ENV_FILE" 2>/dev/null || true
  fi
}

sync_server_prefs() {
  load_key
  [[ -z "$KEY" ]] && return 0
  local model="${1:-$GRIZZLY}"
  local tier="${2:-auto}"
  local body
  body="$(printf '{"active_default_model":"%s","routing_tier":"%s","tier_routes":null}' "$model" "$tier")"
  curl -sS -m 20 -o /tmp/yb-pref-sync.json -w '' \
    -X PUT "${SITE_URL}/api/user/default-model" \
    -H "$(auth_header "$KEY")" \
    -H "Content-Type: application/json" \
    -d "$body" >/dev/null 2>&1 || true
}

cmd_status() {
  resolve_paths
  load_key
  echo "Yielding Bear CLI  v${VERSION}"
  echo "  runtime:  ${RUNTIME}"
  echo "  base:     ${BASE_URL}"
  echo "  key file: ${KEY_FILE}"
  if [[ -n "$KEY" ]]; then
    echo "  key:      ${KEY:0:12}… (${#KEY} chars)"
  else
    echo "  key:      NOT SET"
  fi
  if [[ -f "$CONFIG_FILE" ]]; then
    echo "  config:   $CONFIG_FILE"
    if command -v python3 >/dev/null 2>&1; then
      python3 - "$CONFIG_FILE" <<'PY' 2>/dev/null || true
import json, sys
c = json.load(open(sys.argv[1]))
print("  mode:    ", c.get("routing_mode") or "(legacy)")
print("  model:   ", c.get("default_model") or "(none)")
print("  cfg ver: ", c.get("version") or "(none)")
fb = c.get("fallback_models") or []
print("  fallback:", ", ".join(fb) if fb else "(none)")
rt = c.get("recommended_tiers") or {}
if rt:
    print("  rec high:", rt.get("high") or "")
    print("  rec mid: ", rt.get("mid") or "")
    print("  rec free:", rt.get("low") or "")
print("  offer:   ", c.get("signup_offer") or "(none)")
PY
    fi
  else
    echo "  config:   (missing — run install)"
  fi
}

cmd_doctor() {
  cmd_status
  echo ""
  echo "Checks:"
  code="$(curl -sS -o /tmp/yb-doc-models.json -w '%{http_code}' -m 20 \
    -H 'Accept: application/json' "${SITE_URL}/api/v1/models" 2>/dev/null || echo 000)"
  if [[ "$code" == "200" ]]; then
    echo "  OK  GET /api/v1/models ($code)"
  else
    echo "  FAIL GET /api/v1/models ($code)"
  fi

  rcode="$(curl -sS -o /tmp/yb-doc-route.json -w '%{http_code}' -m 15 \
    -H 'Accept: application/json' \
    "${SITE_URL}/api/public/routing-recommendations" 2>/dev/null || echo 000)"
  if [[ "$rcode" == "200" ]]; then
    echo "  OK  GET /api/public/routing-recommendations ($rcode)"
    if command -v python3 >/dev/null 2>&1; then
      python3 <<'PY' 2>/dev/null || true
import json
j=json.load(open("/tmp/yb-doc-route.json"))
print(f"      mode auto → {j.get('router_model')}")
print(f"      high={j.get('high')}  mid={j.get('mid')}  free={j.get('low')}")
PY
    fi
  else
    echo "  FAIL GET routing-recommendations ($rcode)"
  fi

  hcode="$(curl -sS -o /tmp/yb-doc-health.json -w '%{http_code}' -m 15 \
    "${SITE_URL}/api/health/grizzly-routing" 2>/dev/null || echo 000)"
  if [[ "$hcode" == "200" ]]; then
    echo "  OK  GET /api/health/grizzly-routing ($hcode)"
  else
    echo "  FAIL GET /api/health/grizzly-routing ($hcode)"
  fi

  load_key
  if [[ -n "$KEY" ]]; then
    scode="$(curl -sS -o /tmp/yb-doc-pref.json -w '%{http_code}' -m 15 \
      -H "$(auth_header "$KEY")" \
      "${SITE_URL}/api/user/default-model" 2>/dev/null || echo 000)"
    if [[ "$scode" == "200" ]]; then
      echo "  OK  GET /api/user/default-model ($scode)"
      if command -v python3 >/dev/null 2>&1; then
        python3 - "$CONFIG_FILE" <<'PY' 2>/dev/null || true
import json, sys, os
srv=json.load(open("/tmp/yb-doc-pref.json"))
local_mode=local_model=""
path=sys.argv[1] if len(sys.argv)>1 else ""
if path and os.path.isfile(path):
    try:
        c=json.load(open(path))
        local_mode=c.get("routing_mode") or ""
        local_model=c.get("default_model") or ""
    except Exception:
        pass
s_model=srv.get("active_default_model") or ""
print(f"      server default={s_model}  routing_tier={srv.get('routing_tier')}")
if local_model and s_model and local_model != s_model:
    print(f"      WARN local model ({local_model}) ≠ server ({s_model}) — run set-routing to sync")
if local_mode:
    print(f"      local routing_mode={local_mode}")
PY
      fi
    else
      echo "  FAIL GET /api/user/default-model ($scode)"
    fi
  else
    echo "  SKIP server prefs (no API key)"
  fi
  rm -f /tmp/yb-doc-models.json /tmp/yb-doc-route.json /tmp/yb-doc-health.json /tmp/yb-doc-pref.json 2>/dev/null || true
}

cmd_models() {
  local filter=""
  case "${1:-}" in
    --free) filter=free ;;
    --paid) filter=paid ;;
    --routers) filter=routers ;;
  esac
  fetch_recs
  echo "# recommendations  high=${REC_HIGH}  mid=${REC_MID}  free=${REC_LOW}  router=${REC_ROUTER}"
  tmp="$(mktemp)"
  code="$(curl -sS -o "$tmp" -w '%{http_code}' -m 25 \
    -H 'Accept: application/json' "${SITE_URL}/api/v1/models" 2>/dev/null || echo 000)"
  if [[ "$code" != "200" ]]; then
    echo "Failed to fetch models (HTTP $code)" >&2
    rm -f "$tmp"
    exit 1
  fi
  python3 - "$tmp" "$filter" "$REC_HIGH" "$REC_MID" "$REC_LOW" "$REC_ROUTER" <<'PY'
import json, sys
path, filt, hi, mid, lo, router = sys.argv[1:7]
stars = {hi: "★high", mid: "★mid", lo: "★free", router: "★auto"}
data = json.load(open(path))
rows = data.get("yieldingbear", {}).get("data") or data.get("data") or []
n = 0
for m in rows:
    mid_ = str(m.get("id") or "")
    if not mid_:
        continue
    is_free = m.get("is_free") is True
    is_router = m.get("is_virtual") is True or mid_.startswith("yieldingbear/")
    if filt == "free" and not is_free:
        continue
    if filt == "paid" and is_free:
        continue
    if filt == "routers" and not is_router:
        continue
    tags = []
    tags.append("free" if is_free else "paid")
    if m.get("is_active") is False:
        tags.append("inactive")
    if is_router:
        tags.append("router")
    star = stars.get(mid_, "")
    if star:
        tags.append(star)
    pr = m.get("pricing") or {}
    try:
        inp = float(pr.get("input_per_mtok_usd") or 0)
        out = float(pr.get("output_per_mtok_usd") or 0)
    except Exception:
        inp = out = 0.0
    if is_free:
        price = "0/0"
    elif is_router and inp == 0 and out == 0:
        price = "routed"
    else:
        price = f"{inp:g}/{out:g}"
    name = m.get("name") or m.get("display_name") or ""
    print(f"{mid_}\t[{','.join(tags)}]\t{price}\t{name}")
    n += 1
print(f"# {n} models", file=sys.stderr)
PY
  rm -f "$tmp" 2>/dev/null || true
}

cmd_smoke() {
  load_key
  if [[ -z "$KEY" ]]; then
    echo "No API key. Run: bash scripts/install.sh" >&2
    exit 1
  fi
  model="${1:-}"
  if [[ -z "$model" && -f "$CONFIG_FILE" ]] && command -v python3 >/dev/null 2>&1; then
    model="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("default_model") or "")' "$CONFIG_FILE" 2>/dev/null || true)"
  fi
  model="${model:-liquid/lfm-2.5-2.6b}"
  code="$(curl -sS -o /tmp/yb-smoke.json -w '%{http_code}' -m 60 \
    -X POST "${BASE_URL}/chat/completions" \
    -H "$(auth_header "$KEY")" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"${model}\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply with exactly: ready\"}],\"max_tokens\":8}" \
    2>/dev/null || echo 000)"
  echo "HTTP $code model=$model"
  if command -v python3 >/dev/null 2>&1 && [[ -f /tmp/yb-smoke.json ]]; then
    python3 <<'PY' 2>/dev/null || head -c 400 /tmp/yb-smoke.json
import json
j = json.load(open("/tmp/yb-smoke.json"))
if j.get("error"):
    print("error:", j["error"])
else:
    c = (j.get("choices") or [{}])[0]
    t = (c.get("message") or {}).get("content") or ""
    print("reply:", (t or "").strip()[:120])
PY
  fi
  rm -f /tmp/yb-smoke.json 2>/dev/null || true
}

cmd_set_model() {
  mid="${1:-}"
  if [[ -z "$mid" ]]; then
    echo "Usage: yb.sh set-model <model_id>" >&2
    exit 1
  fi
  NEW_MODE="manual"
  NEW_MODEL="$mid"
  # If user pins the router, treat as auto
  if [[ "$mid" == "$GRIZZLY" || "$mid" == yieldingbear/grizzly-1.0g* ]]; then
    NEW_MODE="auto"
    NEW_MODEL="$GRIZZLY"
  fi
  write_config_fields
  sync_server_prefs "$NEW_MODEL" "auto"
  echo "routing_mode → ${NEW_MODE}"
  echo "default_model → ${NEW_MODEL}"
}

cmd_set_routing() {
  mode="${1:-}"
  pin="${2:-}"
  mode="$(printf '%s' "$mode" | tr 'A-Z' 'a-z')"
  case "$mode" in
    auto|a)
      NEW_MODE="auto"
      NEW_MODEL="$GRIZZLY"
      ;;
    manual|man|m)
      NEW_MODE="manual"
      fetch_recs
      if [[ -n "$pin" ]]; then
        NEW_MODEL="$pin"
      else
        # keep existing or recommend free
        resolve_paths
        cur="$(cfg_get default_model)"
        NEW_MODEL="${cur:-$REC_LOW}"
        [[ -z "$NEW_MODEL" ]] && NEW_MODEL="$REC_LOW"
      fi
      ;;
    *)
      echo "Usage: yb.sh set-routing auto|manual [model_id]" >&2
      echo "  auto   → Grizzly classifies high/mid/free per prompt" >&2
      echo "  manual → pin one catalog model (optional id; YB recs via yb.sh models)" >&2
      exit 1
      ;;
  esac
  write_config_fields
  sync_server_prefs "$NEW_MODEL" "auto"
  echo "routing_mode → ${NEW_MODE}"
  echo "default_model → ${NEW_MODEL}"
  echo "Dashboard mirror: ${SITE_URL}/dashboard?tab=developer"
}

cmd_explain() {
  fetch_recs
  printf '%s\n' \
    "Yielding Bear routing" \
    "" \
    "  Modes (install + dashboard + yb.sh set-routing):" \
    "    auto   -> ${GRIZZLY}" \
    "             classifies each prompt -> high / mid / free" \
    "             uses live I/O \$/1M + allowance cascade (Pro/credits)" \
    "    manual -> pin any catalog model (or keep Grizzly + tier overrides in dashboard)" \
    "" \
    "  Live recommendations:" \
    "    high ${REC_HIGH}" \
    "    mid  ${REC_MID}" \
    "    free ${REC_LOW}" \
    "" \
    "  Server may also enable semantic cache / prompt-cache and optional bandit" \
    "  over tier picks when flags are on (account-dependent - not a guarantee)." \
    "" \
    "  Explicit request body \"model\" always wins over account default." \
    "" \
    "  CLI signup offer: \$10 off Pro first 3 months (\$89->\$99)" \
    "    ${SITE_URL}/offer/cli10x3" \
    "  Referral (bound only): \$20 off first Pro month - never stacked with CLI offer." \
    "" \
    "  Commands:" \
    "    yb.sh set-routing auto" \
    "    yb.sh set-routing manual ${REC_LOW}" \
    "    yb.sh models [--free|--paid|--routers]" \
    "    yb.sh set-model <id>" \
    "    yb.sh doctor" \
    "    yb.sh smoke [model]"
}

cmd_install() {
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  exec bash "${SCRIPT_DIR}/install.sh" "$@"
}

usage() {
  cat <<EOF
yb.sh v${VERSION} — Yielding Bear skill helper

  yb.sh install                       Interactive full setup
  yb.sh status                        Paths + key + routing mode
  yb.sh doctor                        Catalog + recs + prefs health
  yb.sh models [--free|--paid|--routers]
  yb.sh set-routing auto|manual [id]  Auto-select or manual pin
  yb.sh set-model <id>                Pin model (manual; router → auto)
  yb.sh explain                       Routing / offers (honest)
  yb.sh smoke [model]                 Tiny chat completion
EOF
}

main() {
  cmd="${1:-}"
  shift || true
  case "$cmd" in
    install) cmd_install "$@" ;;
    status) cmd_status "$@" ;;
    doctor) cmd_doctor "$@" ;;
    models) cmd_models "$@" ;;
    set-routing|set_routing|routing) cmd_set_routing "$@" ;;
    set-model|set_model) cmd_set_model "$@" ;;
    explain) cmd_explain "$@" ;;
    smoke) cmd_smoke "$@" ;;
    -h|--help|help|"") usage ;;
    *) echo "Unknown: $cmd" >&2; usage; exit 1 ;;
  esac
}

main "$@"
