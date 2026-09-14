#!/usr/bin/env bash
# WordPress REST API wrapper with draft-by-default safety and explicit consent gates.
# Usage: wp.sh <METHOD> <endpoint> [json_body]
#        wp.sh --login | --logout      (move the app password into/out of your OS keychain)
# Config: WP_URL, WP_USER, WP_APP_PASSWORD  (see "Permissions, Data Flow & Consent" in SKILL.md)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# --- Config loading -----------------------------------------------------------
# ONE loader, shared with wp-upload.sh. This script used to carry its own copy;
# the copies drifted and the drift WAS the bug — the explicit WP_ENV_FILE path was
# validated while the implicit <skill>/.env path got no symlink, ownership or mode
# check at all. Sourcing the shared loader means a fix cannot miss a caller.
# shellcheck source=wp-credentials.sh
. "$SCRIPT_DIR/wp-credentials.sh"

wp_load_env_file "$SKILL_DIR"
wp_require_https
wp_check_allowlist

# --- Keychain management ------------------------------------------------------
# wp-credentials.sh points users at these two commands when it refuses a plain
# file; they have to actually exist or that advice is a dead end.
case "${1:-}" in
  --login)
    : "${WP_USER:?Set WP_USER (env or env file) before --login}"
    echo "Paste the WordPress application password for ${WP_USER} @ ${WP_HOST}, then Ctrl-D:" >&2
    if wp_keychain_set; then
      echo "🔐 Stored in your OS keychain. You can now delete WP_APP_PASSWORD from your env file." >&2
      exit 0
    fi
    echo "❌ No usable OS keychain (install libsecret's secret-tool on Linux)." >&2
    echo "   Keep the password in a 0600 env file instead — it will warn on every use." >&2
    exit 1
    ;;
  --logout)
    : "${WP_USER:?Set WP_USER (env or env file) before --logout}"
    wp_keychain_clear
    echo "🔓 Keychain entry for ${WP_USER} @ ${WP_HOST} cleared (if one existed)." >&2
    echo "   This does NOT revoke the password. Revoke it in WordPress → Users → Profile →" >&2
    echo "   Application Passwords, and remove any WP_APP_PASSWORD line from your env file." >&2
    exit 0
    ;;
esac

wp_resolve_password

METHOD="${1:?Usage: wp.sh <GET|POST|PUT|PATCH|DELETE> <endpoint> [json_body]}"
ENDPOINT="${2:?Missing endpoint}"
BODY="${3:-}"

METHOD=$(printf '%s' "$METHOD" | tr '[:lower:]' '[:upper:]')

# --- Route canonicalisation ---------------------------------------------------
# SAFETY: the consent gates below match on the route, so the route they match MUST
# be the route the server will actually resolve. It used to not be: only ONE leading
# slash was stripped, so `//plugins` reached the gates as `/plugins`, matched no
# case arm, and sailed past WP_ALLOW_ADMIN while the server still routed it to
# /plugins. Percent-encoding (`%70lugins`) and traversal (`posts/../plugins`) had
# the same effect. Three rules close it:
#   1. Split path from query FIRST, so query values are never mangled.
#   2. Normalise the path (all leading slashes, repeated slashes, trailing slash)
#      and send THAT — request and gate see one string.
#   3. Gate on the percent-DECODED path, i.e. on what the server will resolve, and
#      refuse `.` / `..` segments outright rather than trying to resolve them.
REQ_PATH="${ENDPOINT%%\?*}"
if [[ "$ENDPOINT" == *\?* ]]; then QUERY="?${ENDPOINT#*\?}"; else QUERY=""; fi

wp_normalize_path() {
  local p="$1"
  while [[ "$p" == /* ]]; do p="${p#/}"; done
  p="$(printf '%s' "$p" | tr -s '/')"
  while [[ "$p" == */ ]]; do p="${p%/}"; done
  printf '%s' "$p"
}

REQ_PATH="$(wp_normalize_path "$REQ_PATH")"
[[ -n "$REQ_PATH" ]] || { echo "❌ Empty endpoint after normalisation." >&2; exit 1; }

# What the server sees after it percent-decodes. This is the string the gates read.
ROUTE="$(printf '%s' "$REQ_PATH" \
  | python3 -c 'import sys,urllib.parse; sys.stdout.write(urllib.parse.unquote(sys.stdin.read()))' 2>/dev/null \
  || printf '%s' "$REQ_PATH")"
ROUTE="$(wp_normalize_path "$ROUTE")"
ROUTE="$(printf '%s' "$ROUTE" | tr '[:upper:]' '[:lower:]')"

case "/$ROUTE/" in
  */../*|*/./*)
    echo "❌ Endpoint contains a relative path segment ('.' or '..'): $ENDPOINT" >&2
    echo "   Refusing — the server would resolve it to a different route than the safety gates see." >&2
    exit 1 ;;
esac

URL="${WP_URL}/wp-json/wp/v2/${REQ_PATH}${QUERY}"

# --- OFF SWITCH ---------------------------------------------------------------
# WP_READONLY=1 (env, or in your .env file) makes this script incapable of
# changing anything: GET still works, every other method stops here.
if [[ -n "${WP_READONLY:-}" && "${WP_READONLY}" != "0" && "$METHOD" != "GET" ]]; then
  echo "🔒 WP_READONLY is set — $METHOD $ROUTE blocked. Unset WP_READONLY to allow writes." >&2
  exit 1
fi

# --- SAFETY: draft by default, publishing needs explicit consent ---------------
# New posts/pages are forced to draft. Going live — on create OR on update — needs
# WP_ALLOW_PUBLISH=1. This is the code behind the "draft-only safety" claim.
BODY_STATUS=""
if [[ -n "$BODY" ]]; then
  BODY_STATUS=$(printf '%s' "$BODY" | python3 -c "import json,sys; print(json.load(sys.stdin).get('status',''))" 2>/dev/null || echo "")
fi

if [[ "$METHOD" == "POST" && ("$ROUTE" == "posts" || "$ROUTE" == "pages") ]]; then
  if [[ -z "$BODY" ]]; then
    BODY='{"status":"draft"}'
  elif [[ "$BODY_STATUS" != "publish" ]]; then
    BODY=$(printf '%s' "$BODY" | python3 -c "import json,sys; d=json.load(sys.stdin); d['status']='draft'; print(json.dumps(d))")
  fi
fi

if [[ "$BODY_STATUS" == "publish" && "$METHOD" != "GET" ]]; then
  if [[ "${WP_ALLOW_PUBLISH:-0}" != "1" ]]; then
    echo "❌ Publishing is gated. This would put content live at ${WP_URL} immediately." >&2
    echo "   Confirm with the site owner, then re-run with WP_ALLOW_PUBLISH=1." >&2
    exit 1
  fi
  echo "⚠️  WP_ALLOW_PUBLISH=1 — status=publish. Content goes live immediately." >&2
fi

# Editing an already-live post/page without sending status=publish still changes
# public content. PUT/PATCH on posts|pages therefore needs the same opt-in.
if [[ "$METHOD" == "PUT" || "$METHOD" == "PATCH" ]]; then
  case "$ROUTE" in
    posts|posts/*|pages|pages/*)
      if [[ "${WP_ALLOW_PUBLISH:-0}" != "1" ]]; then
        echo "❌ Editing live posts/pages is gated (a PUT/PATCH without status still changes public content)." >&2
        echo "   Re-run with WP_ALLOW_PUBLISH=1 once the site owner has agreed." >&2
        exit 1
      fi
      ;;
  esac
fi

# --- SAFETY: site administration needs explicit consent ------------------------
# Installing/activating a plugin or theme is arbitrary code execution on the site;
# users/settings changes are privilege and configuration changes. Reading them is
# free, writing them needs WP_ALLOW_ADMIN=1.
case "$ROUTE" in
  plugins|plugins/*|themes|themes/*|users|users/*|settings|settings/*)
    if [[ "$METHOD" != "GET" && "${WP_ALLOW_ADMIN:-0}" != "1" ]]; then
      echo "❌ $METHOD $ROUTE is a site-administration write and is gated." >&2
      echo "   Installing a plugin or theme runs code on the site; users/settings writes" >&2
      echo "   change who can do what. Re-run with WP_ALLOW_ADMIN=1 once the site owner" >&2
      echo "   has agreed to this specific change." >&2
      exit 1
    fi
    ;;
esac

# --- SAFETY: block permanent delete -------------------------------------------
# WordPress DELETE without force moves a post/page/comment to Trash (recoverable),
# and is the only way to trash on installs whose REST status enum omits "trash"
# (some WooCommerce/SureCart sites reject PUT {"status":"trash"} as
# rest_invalid_param). force=true is the permanent, unrecoverable delete and stays
# blocked — in the query string AND in the JSON body, since WP reads either.
if [[ "$METHOD" == "DELETE" ]]; then
  BODY_FORCE=""
  if [[ -n "$BODY" ]]; then
    BODY_FORCE=$(printf '%s' "$BODY" | python3 -c "import json,sys; print(json.load(sys.stdin).get('force',''))" 2>/dev/null || echo "")
  fi
  QUERY_LC="$(printf '%s' "$QUERY" | python3 -c 'import sys,urllib.parse; print(urllib.parse.unquote(sys.stdin.read()).lower())' 2>/dev/null || printf '%s' "$QUERY")"
  if [[ "$QUERY_LC" == *"force=true"* || "$QUERY_LC" == *"force=1"* \
     || "$BODY_FORCE" == "True" || "$BODY_FORCE" == "true" || "$BODY_FORCE" == "1" || "$BODY_FORCE" == "yes" ]]; then
    echo "❌ Permanent DELETE (force) blocked by safety policy. Drop force= to trash instead (recoverable)." >&2
    exit 1
  fi
fi

# Dry run: print the gate decision and the exact URL without sending anything.
if [[ -n "${WP_DRY_RUN:-}" && "${WP_DRY_RUN}" != "0" ]]; then
  echo "DRY RUN: $METHOD $URL"
  echo "ROUTE: $ROUTE"
  exit 0
fi

# Execute. Some sites sit behind Cloudflare, which challenges plain curl's TLS/JA3
# fingerprint ("Just a moment..." 403). curl_cffi impersonates Chrome's handshake
# and passes; fall back to plain curl when it is not installed.
if python3 -c "import curl_cffi" 2>/dev/null; then
  RESPONSE=$(WP_METHOD="$METHOD" WP_URL_FULL="$URL" WP_BODY="$BODY" \
    WP_AUTH_USER="$WP_USER" WP_AUTH_PW="$WP_APP_PASSWORD" python3 - <<'PY'
import os
from curl_cffi import requests
m=os.environ["WP_METHOD"]; url=os.environ["WP_URL_FULL"]; body=os.environ.get("WP_BODY","")
auth=(os.environ["WP_AUTH_USER"], os.environ["WP_AUTH_PW"].replace(" ",""))
kw=dict(impersonate="chrome", auth=auth, headers={"Content-Type":"application/json"}, timeout=60)
if body and m!="GET": kw["data"]=body.encode()
print(requests.request(m, url, **kw).text)
PY
)
else
  # Password stays in a 0600 netrc file, never on argv. wp_netrc_create installs an
  # EXIT/HUP/INT/TERM trap, so a curl failure under `set -e` cannot leave the
  # credential file behind — which is exactly what the previous version did.
  wp_netrc_create
  CURL_ARGS=(-s -X "$METHOD" --netrc-file "$WP_NETRC" -H "Content-Type: application/json")
  [[ -n "$BODY" && "$METHOD" != "GET" ]] && CURL_ARGS+=(-d "$BODY")
  RESPONSE=$(curl "${CURL_ARGS[@]}" "$URL")
  wp_netrc_cleanup
fi

# Pretty print if python3 available
printf '%s\n' "$RESPONSE" | python3 -m json.tool 2>/dev/null || printf '%s\n' "$RESPONSE"
