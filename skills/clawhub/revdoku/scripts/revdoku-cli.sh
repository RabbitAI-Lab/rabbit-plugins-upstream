#!/usr/bin/env bash
set -euo pipefail

DEFAULT_URL="https://app.revdoku.com"
CREDENTIALS_PATH="${REVDOKU_CREDENTIALS:-${HOME}/.revdoku/credentials}"
DEFAULT_BUCKET_PATH="${REVDOKU_DEFAULT_BUCKET_FILE:-${CREDENTIALS_PATH}.bucket}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEVICE_CODE_GRANT_TYPE="urn:ietf:params:oauth:grant-type:device_code"

# Config dir + installed client version stamp (written by install.sh). Used for
# `--version` and the non-blocking update notice.
REVDOKU_CONFIG_DIR="$(dirname "$CREDENTIALS_PATH")"
CLIENT_VERSION_FILE="${REVDOKU_CLIENT_VERSION_FILE:-${REVDOKU_CONFIG_DIR}/client_version}"
UPDATE_CHECK_STAMP="${REVDOKU_CONFIG_DIR}/.update_check"

installed_client_version() {
  local v="unknown"
  if [[ -f "$CLIENT_VERSION_FILE" ]]; then
    v="$(tr -d '[:space:]' < "$CLIENT_VERSION_FILE" 2>/dev/null || true)"
    [[ -n "$v" ]] || v="unknown"
  fi
  printf '%s' "$v"
}

BASE_URL="${REVDOKU_URL:-$DEFAULT_URL}"
API_KEY="${REVDOKU_API_KEY:-}"
TITLE="${REVDOKU_BUCKET_TITLE:-}"
DESCRIPTION="${REVDOKU_BUCKET_DESCRIPTION:-}"
UPLOAD_MODE="${REVDOKU_UPLOAD_MODE:-auto}"
BUCKET_ID="${REVDOKU_BUCKET_ID:-}"
METADATA_JSON="${REVDOKU_BUCKET_METADATA:-}"
RESTORE_VERSION_ID="${REVDOKU_RESTORE_VERSION_ID:-}"
RESTORE_COMMENT="${REVDOKU_RESTORE_COMMENT:-}"
BROWSER_LOGIN_PATH="${REVDOKU_BROWSER_LOGIN_PATH:-/buckets}"
APPEND_TEXT_PATH="${REVDOKU_APPEND_TEXT_PATH:-}"
APPEND_TEXT_CONTENT="${REVDOKU_APPEND_TEXT_CONTENT:-}"
APPEND_TEXT_CONTENT_FILE="${REVDOKU_APPEND_TEXT_CONTENT_FILE:-}"
APPEND_TEXT_NEWLINE_BEFORE="${REVDOKU_APPEND_TEXT_NEWLINE_BEFORE:-true}"
GRANT_TOKEN=""
ACCOUNT_ID=""
CLIENT_ACCOUNT_NAME=""
CLIENT_DISPLAY_NAME=""
TAG_PATHS=()
AGENT_NAME="${REVDOKU_AGENT_NAME:-}"
AGENT_CLIENT="${REVDOKU_AGENT_CLIENT:-revdoku}"
AGENT_VERSION="${REVDOKU_AGENT_VERSION:-}"
if [[ -z "$AGENT_VERSION" ]]; then
  AGENT_VERSION="$(installed_client_version)"
  [[ "$AGENT_VERSION" == "unknown" ]] && AGENT_VERSION="0.1.0"
fi
AGENT_RUN_ID="${REVDOKU_AGENT_RUN_ID:-}"
AGENT_PROJECT="${REVDOKU_AGENT_PROJECT:-}"
AGENT_TASK="${REVDOKU_AGENT_TASK:-}"
BUCKET_UPLOAD_DESCRIPTOR_BATCH_SIZE="${REVDOKU_BUCKET_UPLOAD_DESCRIPTOR_BATCH_SIZE:-25}"
BUCKET_UPLOAD_CLIENT_SESSION_KEY="${REVDOKU_BUCKET_UPLOAD_CLIENT_SESSION_KEY:-}"
HTTP_TRANSIENT_MAX_ATTEMPTS="${REVDOKU_HTTP_TRANSIENT_MAX_ATTEMPTS:-5}"
HTTP_RETRYABLE_CONFLICT_MAX_ATTEMPTS="${REVDOKU_HTTP_RETRYABLE_CONFLICT_MAX_ATTEMPTS:-12}"
HTTP_LOCK_MAX_ATTEMPTS="${REVDOKU_HTTP_LOCK_MAX_ATTEMPTS:-3}"
DIRECT_UPLOAD_MAX_ATTEMPTS="${REVDOKU_DIRECT_UPLOAD_MAX_ATTEMPTS:-5}"
LOGIN="false"
ACTION="store"
PATH_TO_STORE=""
PATH_EXPLICIT="false"
READ_FILE_PATH=""
THREAD_FOR=""
OUTPUT_PATH=""
SHOW_UPLOAD_HINT="false"
# Project-local binding (.revdoku): remembers the bucket so `revdoku upload`
# updates the same stored files. Populated from the target dir, --bucket-id overrides.
REVDOKU_PROJECT_FILE=""
BOUND_BUCKET_ID=""
BINDING_EXISTED="false"
LAST_HTTP_STATUS=""
LAST_ERROR_CODE=""
LAST_ERROR_MESSAGE=""
LAST_ERROR_DETAILS_JSON=""

die() {
  echo "error: $1" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "requires $1"
}

# Identify the AI agent or tool driving this CLI so uploads are attributed to
# the real caller (claude-code, codex, ...) instead of a generic "cli".
# Precedence: --agent flag / REVDOKU_AGENT_NAME override this entirely; this
# function only runs as the fallback. Always degrades safely to "cli".
detect_agent_name() {
  if [[ -n "${CLAUDECODE:-}" || -n "${CLAUDE_CODE_ENTRYPOINT:-}" ]]; then
    printf 'claude-code'
  elif [[ -n "${CODEX_SANDBOX:-}" || -n "${CODEX_HOME:-}" ]]; then
    printf 'codex'
  elif [[ -n "${CURSOR_TRACE_ID:-}" ]]; then
    printf 'cursor'
  elif [[ -n "${AI_AGENT:-}" ]]; then
    # Generic convention, e.g. AI_AGENT="claude-code_2-1-173_agent" -> "claude-code"
    printf '%s' "${AI_AGENT%%_*}"
  else
    printf 'cli'
  fi
}

usage() {
  cat <<USAGE
revdoku — cloud storage with an email address for every bucket.

Usage: revdoku <command> [PATH] [options]

  upload [PATH]         Save local files or a folder (default: current folder).
                        Opens browser sign-in when credentials are missing.
  ls, list              List your buckets.
  o, open               Open this bucket in the dashboard.
  st, status            Show connection and account status.
  login                 Sign in to an existing account in the browser.
  grant TOKEN           Use a one-time connection token from the web app.
  inbox                 Show incoming address, readiness, and email activity.
  files                 List files and stored email in a bucket.
  read PATH             Read a bucket file; --output FILE saves it locally.
  versions              Show bucket version history.
  restore ID            Restore a bucket version; --restore-comment TEXT.
  append PATH           Append text; --content TEXT or --content-file FILE.
  archive | unarchive | delete    Manage a bucket.
  account               Account, plan and storage status.
  account create-client NAME     Create a client account within an authorized agency.
  dashboard             Print the dashboard URL; normal sign-in is required.

Options:
  --account-id ID       Select a granted account for this command.
  --client-name NAME    Client person or business (account create-client).
  --bucket-id ID        Target bucket; overrides the local .revdoku binding.
  --thread-for FILE_ID  With files: list this email's conversation and replies.
  --title TEXT         --description TEXT     --tag-path LABEL     --metadata JSON
  --url URL            App URL (default $DEFAULT_URL).
  --api-key KEY        API credential (or REVDOKU_API_KEY / $CREDENTIALS_PATH).
  --agent NAME         Attribute uploads (default: auto-detected).
  --upload-mode MODE   auto or direct (default: auto).
  --version            Print installed client version.
  -h, --help           Show this help.

Examples:
  revdoku upload ./project-files
  revdoku files --bucket-id bkt_...
  revdoku read notes.md --bucket-id bkt_...
  revdoku dashboard

You can start free. Plans: https://app.revdoku.com/pricing
USAGE
}

# ---------------------------------------------------------------------------
# Command parsing. The first non-option token is the verb (upload, ls, open …);
# options may appear before or after it. A bare path (`revdoku .`) stores files;
# no args at all shows status + a hint. The most common verb is the shortest.
# ---------------------------------------------------------------------------
VERB_SEEN="false"
ORIGINAL_ARGC=$#

while [[ $# -gt 0 ]]; do
  case "$1" in
    --api-key)
      [[ $# -ge 2 ]] || die "--api-key requires a value"
      API_KEY="$2"
      shift 2
      ;;
    --url)
      [[ $# -ge 2 ]] || die "--url requires a value"
      BASE_URL="$2"
      shift 2
      ;;
    --title)
      [[ $# -ge 2 ]] || die "--title requires a value"
      TITLE="$2"
      shift 2
      ;;
    --description)
      [[ $# -ge 2 ]] || die "--description requires a value"
      DESCRIPTION="$2"
      shift 2
      ;;
    --tag-path)
      [[ $# -ge 2 ]] || die "--tag-path requires a value"
      TAG_PATHS+=("$2")
      shift 2
      ;;
    --account-id)
      [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || die "--account-id requires an account id"
      ACCOUNT_ID="$2"
      shift 2
      ;;
    --client-name)
      [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || die "--client-name requires a client name"
      CLIENT_DISPLAY_NAME="$2"
      shift 2
      ;;
    --bucket-id)
      [[ $# -ge 2 ]] || die "--bucket-id requires a value"
      BUCKET_ID="$2"
      shift 2
      ;;
    --thread-for)
      [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || die "--thread-for requires an email file id"
      THREAD_FOR="$2"
      shift 2
      ;;
    --metadata)
      [[ $# -ge 2 ]] || die "--metadata requires a JSON object"
      METADATA_JSON="$2"
      shift 2
      ;;
    --agent)
      [[ $# -ge 2 ]] || die "--agent requires a value"
      AGENT_NAME="$2"
      shift 2
      ;;
    --output)
      [[ $# -ge 2 ]] || die "--output requires a value"
      OUTPUT_PATH="$2"
      shift 2
      ;;
    --restore-comment)
      [[ $# -ge 2 ]] || die "--restore-comment requires a value"
      RESTORE_COMMENT="$2"
      shift 2
      ;;
    --content)
      [[ $# -ge 2 ]] || die "--content requires a value"
      APPEND_TEXT_CONTENT="$2"
      shift 2
      ;;
    --content-file)
      [[ $# -ge 2 ]] || die "--content-file requires a local file path or -"
      APPEND_TEXT_CONTENT_FILE="$2"
      shift 2
      ;;
    --no-newline-before)
      APPEND_TEXT_NEWLINE_BEFORE="false"
      shift
      ;;
    --upload-mode)
      [[ $# -ge 2 ]] || die "--upload-mode requires a value"
      UPLOAD_MODE="$2"
      shift 2
      ;;
    --version)
      printf '%s\n' "$(installed_client_version)"
      printf 'Latest: https://github.com/revdoku/revdoku — update using your original installation method: https://revdoku.com/llms-install.md\n' >&2
      exit 0
      ;;
    --login)
      # Compatibility with older public prompts. `revdoku login` is the
      # canonical spelling, but existing copied instructions must keep working.
      LOGIN="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      die "unknown option: $1 (run 'revdoku --help')"
      ;;
    *)
      if [[ "$VERB_SEEN" == "true" ]]; then
        PATH_TO_STORE="$1"
        PATH_EXPLICIT="true"
        shift
      else
        VERB_SEEN="true"
        case "$1" in
          upload|put)     shift ;;
          p|publish|down|unpublish|preview|sites|analytics|i|init)
            die "This command is unavailable. Use revdoku --help for storage commands." ;;
          ls|list)        ACTION="list_buckets"; shift ;;
          o|open)         ACTION="open_dashboard"; shift ;;
          st|status)      ACTION="connection_status"; shift ;;
          login)          LOGIN="true"; shift ;;
          grant)          [[ $# -ge 2 && "$2" != -* ]] || die "grant needs the one-time token right after it"; ACTION="exchange_grant"; GRANT_TOKEN="$2"; shift 2 ;;
          files)          ACTION="list_files"; shift ;;
          inbox)          ACTION="inbox_status"; shift ;;
          read)           [[ $# -ge 2 && "$2" != -* ]] || die "read needs a bucket PATH right after it, e.g. revdoku read notes.md --bucket-id ID"; ACTION="read_file"; READ_FILE_PATH="$2"; shift 2 ;;
          versions)       ACTION="list_versions"; shift ;;
          restore)        [[ $# -ge 2 && "$2" != -* ]] || die "restore needs a version id right after it, e.g. revdoku restore VERSION_ID --bucket-id ID"; ACTION="restore_version"; RESTORE_VERSION_ID="$2"; shift 2 ;;
          append)         [[ $# -ge 2 && "$2" != -* ]] || die "append needs a bucket PATH right after it, e.g. revdoku append leads.csv --bucket-id ID --content-file new.csv"; ACTION="append_text_file"; APPEND_TEXT_PATH="$2"; shift 2 ;;
          archive)        ACTION="archive_bucket"; shift ;;
          unarchive)      ACTION="unarchive_bucket"; shift ;;
          delete)         ACTION="delete_bucket"; shift ;;
          account)
            shift
            if [[ "${1:-}" == "create-client" ]]; then
              [[ $# -ge 2 && -n "$2" && "$2" != -* ]] || die "account create-client needs a name"
              ACTION="create_client_account"; CLIENT_ACCOUNT_NAME="$2"; shift 2
            else
              ACTION="account_status"
            fi
            ;;
          dashboard)      ACTION="open_dashboard"; shift ;;
          help)           usage; exit 0 ;;
          version)        printf '%s\n' "$(installed_client_version)"; exit 0 ;;
          *)
            # An existing or path-like token selects files to store.
            if [[ -e "$1" || "$1" == .* || "$1" == /* || "$1" == \~* ]]; then
              PATH_TO_STORE="$1"
              PATH_EXPLICIT="true"
              shift
            else
              die "unknown command: $1 (run 'revdoku --help')"
            fi
            ;;
        esac
      fi
      ;;
  esac
done

# No verb and no path token: bare `revdoku` shows status + a hint; other
# options-only invocations store the current folder.
if [[ "$VERB_SEEN" == "false" && "$ACTION" == "store" && "$LOGIN" != "true" ]]; then
  if [[ "$ORIGINAL_ARGC" -eq 0 ]]; then
    ACTION="connection_status"
    SHOW_UPLOAD_HINT="true"
  fi
fi

if [[ -z "$PATH_TO_STORE" ]]; then
  if [[ -n "${1:-}" ]]; then
    PATH_TO_STORE="$1"
    PATH_EXPLICIT="true"
  else
    PATH_TO_STORE="."
  fi
fi
BASE_URL="${BASE_URL%/}"
[[ -n "$AGENT_NAME" ]] || AGENT_NAME="$(detect_agent_name)"

need_cmd curl
need_cmd openssl
need_cmd base64
need_cmd find

if [[ -x "${SCRIPT_DIR}/jq" ]]; then
  JQ_BIN="${SCRIPT_DIR}/jq"
elif command -v jq >/dev/null 2>&1; then
  JQ_BIN="$(command -v jq)"
else
  die "requires jq"
fi

API_KEY_FROM_CREDENTIALS="false"
if [[ -z "$API_KEY" && -f "$CREDENTIALS_PATH" ]]; then
  API_KEY="$(tr -d '\r\n' < "$CREDENTIALS_PATH")"
  API_KEY_FROM_CREDENTIALS="true"
fi

if [[ -z "$BUCKET_ID" && "$API_KEY_FROM_CREDENTIALS" == "true" && -f "$DEFAULT_BUCKET_PATH" ]]; then
  BUCKET_ID="$(tr -d '\r\n' < "$DEFAULT_BUCKET_PATH")"
fi

# A .revdoku file binds this folder to a bucket for upload/read commands.
# An explicit --bucket-id takes precedence. The binding is excluded from uploads.
if [[ -d "$PATH_TO_STORE" || ! -e "$PATH_TO_STORE" ]]; then
  REVDOKU_PROJECT_FILE="${PATH_TO_STORE%/}/.revdoku"
else
  REVDOKU_PROJECT_FILE="$(dirname "$PATH_TO_STORE")/.revdoku"
fi
if [[ -f "$REVDOKU_PROJECT_FILE" ]]; then
  BINDING_EXISTED="true"
  BOUND_BUCKET_ID="$(sed -n 's/^bucket_id=//p' "$REVDOKU_PROJECT_FILE" 2>/dev/null | head -n1 | tr -d '\r')"
fi
if [[ -z "$BUCKET_ID" && -n "$BOUND_BUCKET_ID" ]]; then
  BUCKET_ID="$BOUND_BUCKET_ID"
fi
# Persist (or refresh) the .revdoku binding for a directory project after a
# successful upload. Silent unless it is the first time we bind.
write_project_binding() {
  local bucket="$1" url="$2"
  [[ "${REVDOKU_WRITE_BINDING:-true}" == "true" ]] || return 0
  [[ -n "$bucket" && -n "$REVDOKU_PROJECT_FILE" ]] || return 0
  [[ -d "$PATH_TO_STORE" ]] || return 0
  {
    printf '# Revdoku project binding — created by `revdoku upload`. Safe to commit or gitignore.\n'
    printf 'bucket_id=%s\n' "$bucket"
    [[ -n "$url" ]] && printf 'url=%s\n' "$url"
  } > "$REVDOKU_PROJECT_FILE" 2>/dev/null || return 0
  if [[ "$BINDING_EXISTED" != "true" ]]; then
    echo "Bound this folder to $bucket (.revdoku). Next time just run: revdoku upload ." >&2
    BINDING_EXISTED="true"
  fi
}

if [[ -n "$METADATA_JSON" ]]; then
  METADATA_JSON="$(printf "%s" "$METADATA_JSON" | "$JQ_BIN" -c 'if type == "object" then . else error("metadata must be a JSON object") end')" || die "--metadata must be a JSON object"
else
  METADATA_JSON="{}"
fi

normalize_optional_bool() {
  local name="$1"
  local value="$2"
  [[ -n "$value" ]] || return 0
  case "$value" in
    true|1|yes|on)
      printf "true"
      ;;
    false|0|no|off)
      printf "false"
      ;;
    *)
      die "$name must be true or false"
      ;;
  esac
}

APPEND_TEXT_NEWLINE_BEFORE="$(normalize_optional_bool "REVDOKU_APPEND_TEXT_NEWLINE_BEFORE" "$APPEND_TEXT_NEWLINE_BEFORE")"
APPEND_TEXT_NEWLINE_BEFORE="${APPEND_TEXT_NEWLINE_BEFORE:-true}"

if [[ "$ACTION" == "append_text_file" ]]; then
  [[ -n "$BUCKET_ID" ]] || die "append requires --bucket-id"
  [[ -n "$APPEND_TEXT_PATH" ]] || die "append requires a bucket-relative PATH"
  if [[ -n "$APPEND_TEXT_CONTENT" && -n "$APPEND_TEXT_CONTENT_FILE" ]]; then
    die "use either --content or --content-file with append, not both"
  fi
  if [[ -z "$APPEND_TEXT_CONTENT" && -z "$APPEND_TEXT_CONTENT_FILE" ]]; then
    die "append requires --content or --content-file"
  fi
fi

account_request_path() {
  local request_path="$1" separator="?"
  if [[ -n "$ACCOUNT_ID" && "$request_path" == /api/v1/* ]]; then
    [[ "$request_path" != *\?* ]] || separator="&"
    printf '%s%saccount_id=%s' "$request_path" "$separator" "$("$JQ_BIN" -rn --arg id "$ACCOUNT_ID" '$id|@uri')"
  else
    printf '%s' "$request_path"
  fi
}

api_url() {
  printf "%s%s" "$BASE_URL" "$1"
}

json_string() {
  "$JQ_BIN" -rn --arg value "$1" '$value'
}

http_status_success() {
  local status="${1:-}"
  [[ "$status" =~ ^[0-9]+$ ]] && (( status >= 200 && status < 300 ))
}

http_status_retryable() {
  case "${1:-}" in
    408|425|429|500|502|503|504)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

http_error_code_retryable() {
  case "${1:-}" in
    DATABASE_BUSY_RETRY|BUCKET_FILE_PATH_INDEX_BACKFILL_PENDING|BUCKET_DELETE_BUSY|BUCKET_DELETE_ENQUEUE_FAILED)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

retry_delay_for_attempt() {
  local attempt="${1:-1}"
  local retry_after="${2:-}"
  local delay
  if [[ "$retry_after" =~ ^[0-9]+$ && "$retry_after" -gt 0 ]]; then
    echo "$retry_after"
    return 0
  fi
  case "$attempt" in
    1) delay=1 ;;
    2) delay=2 ;;
    3) delay=4 ;;
    *) delay=8 ;;
  esac
  echo "$delay"
}

http_success_json_replay_allowed() {
  local method="$1"
  local path="$2"
  case "$method:$path" in
    GET:*)
      return 0
      ;;
    POST:/api/v1/buckets)
      return 0
      ;;
    POST:*/upload_sessions|POST:*/upload_sessions/*/uploads|POST:*/upload_sessions/*/finalize|POST:*/upload_sessions/*/finalize_batch)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

http_conflict_retry_allowed() {
  local method="$1"
  local path="$2"
  case "$method:$path" in
    GET:*)
      return 0
      ;;
    POST:/api/v1/buckets)
      return 0
      ;;
    POST:*/upload_sessions|POST:*/upload_sessions/*/uploads|POST:*/upload_sessions/*/finalize|POST:*/upload_sessions/*/finalize_batch)
      return 0
      ;;
    DELETE:/api/v1/buckets/*)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

http_lock_retry_allowed() {
  local method="$1"
  local path="$2"
  case "$method:$path" in
    POST:*/files/append_text)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

lock_detail_summary() {
  local details_json="${1:-{}}"
  "$JQ_BIN" -r '
    def present: select(. != null and . != "");
    (.locked_by_api_key.label // .locked_by.name // .locked_by.email // .locked_by_api_key.id // .locked_by.id // "another actor") as $owner
    | (.message // .kind // "" | tostring) as $message
    | (.locked_until // "" | tostring) as $until
    | "locked by " + $owner
      + (if ($message | length) > 0 then " (" + $message + ")" else "" end)
      + (if ($until | length) > 0 then " until " + $until else "" end)
  ' <<<"$details_json" 2>/dev/null || printf 'locked by another actor'
}

agent_header_args() {
  printf "%s\0" \
    "-H" "User-Agent: Revdoku/${AGENT_VERSION} (${AGENT_CLIENT})" \
    "-H" "X-Revdoku-Agent: ${AGENT_NAME}" \
    "-H" "X-Revdoku-Agent-Client: ${AGENT_CLIENT}" \
    "-H" "X-Revdoku-Agent-Version: ${AGENT_VERSION}"
  [[ -n "$AGENT_RUN_ID" ]] && printf "%s\0" "-H" "X-Revdoku-Agent-Run-Id: ${AGENT_RUN_ID}"
  [[ -n "$AGENT_PROJECT" ]] && printf "%s\0" "-H" "X-Revdoku-Agent-Project: ${AGENT_PROJECT}"
  [[ -n "$AGENT_TASK" ]] && printf "%s\0" "-H" "X-Revdoku-Agent-Task: ${AGENT_TASK}"
}

http_json() {
  local method="$1"
  local path="$2"
  local payload="$3"
  local auth="${4:-true}"
  if [[ -n "$ACCOUNT_ID" && "$auth" == "true" && "$path" == /api/v1/* ]]; then
    if [[ "$method" == "GET" || "$method" == "HEAD" ]]; then
      path="$(account_request_path "$path")"
    else
      payload="$("$JQ_BIN" -c --arg account_id "$ACCOUNT_ID" '. + {account_id: $account_id}' <<<"$payload")"
    fi
  fi
  local body_file status message code request_id retry_after details_json attempt curl_status delay agent_args=()
  LAST_HTTP_STATUS=""
  LAST_ERROR_CODE=""
  LAST_ERROR_MESSAGE=""
  LAST_ERROR_DETAILS_JSON=""
  body_file="$(mktemp)"
  attempt=0

  while IFS= read -r -d '' value; do
    agent_args+=("$value")
  done < <(agent_header_args)

  local args=(-sS -o "$body_file" -w "%{http_code}" -X "$method" "$(api_url "$path")" "${agent_args[@]}" -H "Content-Type: application/json")
  if [[ "$auth" == "true" ]]; then
    args+=(-H "Authorization: Bearer $API_KEY")
  fi
  args+=(--data "$payload")

  while true; do
    : > "$body_file"
    if status="$(curl "${args[@]}")"; then
      curl_status=0
    else
      curl_status=$?
      if (( attempt < HTTP_TRANSIENT_MAX_ATTEMPTS )); then
        attempt=$((attempt + 1))
        delay="$(retry_delay_for_attempt "$attempt")"
        echo "Network error while calling $path; retrying in ${delay}s (${attempt}/${HTTP_TRANSIENT_MAX_ATTEMPTS})..." >&2
        sleep "$delay"
        continue
      fi
      rm -f "$body_file"
      LAST_HTTP_STATUS=""
      LAST_ERROR_CODE=""
      LAST_ERROR_MESSAGE="Network error while calling $path"
      LAST_ERROR_DETAILS_JSON=""
      echo "error: network error while calling $path (curl exit $curl_status)" >&2
      return 1
    fi

    if http_status_success "$status"; then
      if [[ "$status" != "204" ]] && ! "$JQ_BIN" -e . "$body_file" >/dev/null 2>&1; then
        if http_success_json_replay_allowed "$method" "$path" && (( attempt < HTTP_TRANSIENT_MAX_ATTEMPTS )); then
          attempt=$((attempt + 1))
          delay="$(retry_delay_for_attempt "$attempt")"
          echo "Invalid JSON response from $path after HTTP $status; retrying in ${delay}s (${attempt}/${HTTP_TRANSIENT_MAX_ATTEMPTS})..." >&2
          sleep "$delay"
          continue
        fi
        rm -f "$body_file"
        LAST_HTTP_STATUS="$status"
        LAST_ERROR_CODE="INVALID_JSON_RESPONSE"
        LAST_ERROR_MESSAGE="Invalid JSON response from $path after HTTP $status"
        LAST_ERROR_DETAILS_JSON=""
        echo "error: invalid JSON response from $path after HTTP $status" >&2
        return 1
      fi
      cat "$body_file"
      rm -f "$body_file"
      return 0
    fi

    message="$("$JQ_BIN" -r '.error.message // .error_description // .message // empty' "$body_file" 2>/dev/null || true)"
    code="$("$JQ_BIN" -r '.error.code // .error // empty' "$body_file" 2>/dev/null || true)"
    request_id="$("$JQ_BIN" -r '.error.request_id // .request_id // empty' "$body_file" 2>/dev/null || true)"
    retry_after="$("$JQ_BIN" -r '.error.details.retry_after // empty' "$body_file" 2>/dev/null || true)"
    details_json="$("$JQ_BIN" -c '.error.details // {}' "$body_file" 2>/dev/null || printf '{}')"

    if [[ "$status" == "429" && "$attempt" -lt 20 ]]; then
      [[ "$retry_after" =~ ^[0-9]+$ && "$retry_after" -gt 0 ]] || retry_after=5
      attempt=$((attempt + 1))
      echo "Rate limited while calling $path; retrying in ${retry_after}s..." >&2
      sleep "$retry_after"
      continue
    fi

    if [[ "$status" == "409" ]] && http_error_code_retryable "$code" && http_conflict_retry_allowed "$method" "$path" && (( attempt < HTTP_RETRYABLE_CONFLICT_MAX_ATTEMPTS )); then
      attempt=$((attempt + 1))
      delay="$(retry_delay_for_attempt "$attempt" "$retry_after")"
      echo "Server is busy while calling $path; retrying in ${delay}s (${attempt}/${HTTP_RETRYABLE_CONFLICT_MAX_ATTEMPTS})..." >&2
      sleep "$delay"
      continue
    fi

    if [[ "$status" == "423" && ( "$code" == "BUCKET_LOCKED" || "$code" == "FILE_LOCKED" ) ]] && http_lock_retry_allowed "$method" "$path" && (( attempt < HTTP_LOCK_MAX_ATTEMPTS )); then
      attempt=$((attempt + 1))
      delay="$(retry_delay_for_attempt "$attempt" "$retry_after")"
      echo "Locked while calling $path ($(lock_detail_summary "$details_json")); retrying in ${delay}s (${attempt}/${HTTP_LOCK_MAX_ATTEMPTS})..." >&2
      sleep "$delay"
      continue
    fi

    if http_status_retryable "$status" && (( attempt < HTTP_TRANSIENT_MAX_ATTEMPTS )); then
      attempt=$((attempt + 1))
      delay="$(retry_delay_for_attempt "$attempt")"
      echo "Transient HTTP $status while calling $path; retrying in ${delay}s (${attempt}/${HTTP_TRANSIENT_MAX_ATTEMPTS})..." >&2
      sleep "$delay"
      continue
    fi

    rm -f "$body_file"
    LAST_HTTP_STATUS="$status"
    LAST_ERROR_CODE="$code"
    LAST_ERROR_MESSAGE="$message"
    LAST_ERROR_DETAILS_JSON="$details_json"
    [[ -n "$message" ]] || message="HTTP $status"
    [[ -n "$code" ]] && message="${message} (${code})"
    [[ -n "$request_id" ]] && message="${message} request_id=${request_id}"
    echo "error: $message" >&2
    if [[ "$status" == "423" && ( "$code" == "BUCKET_LOCKED" || "$code" == "FILE_LOCKED" ) ]]; then
      echo "Lock details: $(lock_detail_summary "$details_json")" >&2
    fi
    if [[ "$auth" == "true" ]]; then
      if [[ "$code" == "ACCOUNT_ACCESS_UNAVAILABLE" ]]; then
        echo "This connection uses bucket-scoped agent credentials, which cannot read account-level status. Verify the connection with 'revdoku status', or open Revdoku in a browser for account details." >&2
      elif [[ "$status" == "401" || "$status" == "403" ]]; then
        echo "Run 'revdoku login' to reconnect and save a fresh Revdoku API key." >&2
      fi
    fi
    return 1
  done
}

http_json_quiet() {
  local method="$1"
  local path="$2"
  local payload="$3"
  local body_file status message code agent_args=()
  LAST_HTTP_STATUS=""
  LAST_ERROR_CODE=""
  LAST_ERROR_MESSAGE=""
  LAST_ERROR_DETAILS_JSON=""
  body_file="$(mktemp)"

  while IFS= read -r -d '' value; do
    agent_args+=("$value")
  done < <(agent_header_args)

  if ! status="$(curl -sS -o "$body_file" -w "%{http_code}" -X "$method" "$(api_url "$path")" "${agent_args[@]}" -H "Content-Type: application/json" --data "$payload")"; then
    rm -f "$body_file"
    LAST_HTTP_STATUS=""
    LAST_ERROR_CODE="NETWORK_ERROR"
    LAST_ERROR_MESSAGE="Network error while calling $path"
    LAST_ERROR_DETAILS_JSON=""
    return 1
  fi

  if http_status_success "$status"; then
    cat "$body_file"
    rm -f "$body_file"
    return 0
  fi

  message="$("$JQ_BIN" -r 'if (.error | type) == "object" then (.error.message // empty) else (.error_description // .message // empty) end' "$body_file" 2>/dev/null || true)"
  code="$("$JQ_BIN" -r 'if (.error | type) == "object" then (.error.code // empty) else (.error // empty) end' "$body_file" 2>/dev/null || true)"
  LAST_HTTP_STATUS="$status"
  LAST_ERROR_CODE="$code"
  LAST_ERROR_MESSAGE="$message"
  LAST_ERROR_DETAILS_JSON="$("$JQ_BIN" -c 'if (.error | type) == "object" then (.error.details // {}) else {} end' "$body_file" 2>/dev/null || printf '{}')"
  rm -f "$body_file"
  return 1
}

prompt_read() {
  local prompt="$1"
  local value
  if [[ -t 0 ]]; then
    printf "%s" "$prompt" >&2
    IFS= read -r value
  elif { exec 3<>/dev/tty; } 2>/dev/null; then
    printf "%s" "$prompt" >&3
    IFS= read -r value <&3
    exec 3>&-
  else
    die "Browser login could not start, and the email-code fallback needs an interactive terminal. Retry 'revdoku login' in a terminal."
  fi
  printf "%s" "$value"
}

save_api_key() {
  local key="$1"
  [[ -n "$key" ]] || die "API key is required"
  mkdir -p "$(dirname "$CREDENTIALS_PATH")"
  umask 077
  printf "%s\n" "$key" > "$CREDENTIALS_PATH"
  rm -f "$DEFAULT_BUCKET_PATH"
  echo "Saved Revdoku API key to $CREDENTIALS_PATH" >&2
  echo "This is a one-time setup. Future runs will reuse the saved key automatically." >&2
  API_KEY="$key"
}

open_browser_url() {
  local url="$1"
  [[ -n "$url" ]] || return 1
  if command -v open >/dev/null 2>&1; then
    open "$url" >/dev/null 2>&1 && return 0
  fi
  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$url" >/dev/null 2>&1 && return 0
  fi
  if command -v wslview >/dev/null 2>&1; then
    wslview "$url" >/dev/null 2>&1 && return 0
  fi
  return 1
}

# Open the selected bucket in the authenticated dashboard.
open_dashboard() {
  if [[ -n "$BUCKET_ID" ]]; then
    BROWSER_LOGIN_PATH="/buckets/view?id=$BUCKET_ID"
  else
    BROWSER_LOGIN_PATH="/buckets"
  fi
  browser_login_link
}

request_device_agent_key() {
  local payload response response_file client_id device_code user_code verification_uri_complete expires_in interval deadline now token_payload key

  payload="$("$JQ_BIN" -nc --arg grant "$DEVICE_CODE_GRANT_TYPE" '{client_name:"Revdoku CLI", redirect_uris:[], grant_types:[$grant,"refresh_token"], response_types:[], token_endpoint_auth_method:"none"}')"
  response="$(http_json_quiet POST "/oauth/register" "$payload")" || return 1
  client_id="$("$JQ_BIN" -r '.client_id // empty' <<<"$response")"
  [[ -n "$client_id" ]] || return 1

  payload="$("$JQ_BIN" -nc --arg client_id "$client_id" --arg resource "${BASE_URL%/}/mcp" '{client_id:$client_id, scope:"revdoku:mcp", resource:$resource}')"
  response="$(http_json_quiet POST "/oauth/device_authorization" "$payload")" || return 1
  device_code="$("$JQ_BIN" -r '.device_code // empty' <<<"$response")"
  user_code="$("$JQ_BIN" -r '.user_code // empty' <<<"$response")"
  verification_uri_complete="$("$JQ_BIN" -r '.verification_uri_complete // .verification_uri // empty' <<<"$response")"
  expires_in="$("$JQ_BIN" -r '.expires_in // 600' <<<"$response")"
  interval="$("$JQ_BIN" -r '.interval // 5' <<<"$response")"
  [[ -n "$device_code" && -n "$user_code" && -n "$verification_uri_complete" ]] || return 1
  [[ "$expires_in" =~ ^[0-9]+$ && "$expires_in" -gt 0 ]] || expires_in=600
  [[ "$interval" =~ ^[0-9]+$ && "$interval" -gt 0 ]] || interval=5

  echo "Open this Revdoku link to connect:" >&2
  echo "$verification_uri_complete" >&2
  echo "Connection ID is $user_code" >&2
  echo "This is a safety check. Make sure the same ID appears in the top-right of Revdoku, then select Confirm Connection." >&2
  if open_browser_url "$verification_uri_complete"; then
    echo "Opened the approval page in your browser." >&2
  else
    echo "Could not open a browser automatically; paste the link above into your browser." >&2
  fi
  echo "Waiting for browser approval..." >&2

  deadline=$(( $(date +%s) + expires_in ))
  response_file="$(mktemp)"
  while true; do
    now="$(date +%s)"
    if [[ "$now" =~ ^[0-9]+$ && "$now" -ge "$deadline" ]]; then
      rm -f "$response_file"
      die "device login expired; run 'revdoku login' again"
    fi

    sleep "$interval"
    token_payload="$("$JQ_BIN" -nc --arg grant "$DEVICE_CODE_GRANT_TYPE" --arg client_id "$client_id" --arg device_code "$device_code" --arg resource "${BASE_URL%/}/mcp" '{grant_type:$grant, client_id:$client_id, device_code:$device_code, resource:$resource}')"
    : > "$response_file"
    # Keep http_json_quiet in this shell. Command substitution would run it in a
    # subshell and discard LAST_ERROR_CODE, turning the expected
    # authorization_pending response into a false legacy-login fallback.
    if http_json_quiet POST "/oauth/token" "$token_payload" > "$response_file"; then
      response="$(cat "$response_file")"
      key="$("$JQ_BIN" -r '.revdoku_api_key // empty' <<<"$response")"
      [[ -n "$key" ]] || die "device login did not return a Revdoku API key"
      save_api_key "$key"
      rm -f "$response_file"
      return 0
    fi

    case "$LAST_ERROR_CODE" in
      authorization_pending)
        ;;
      slow_down)
        interval=$((interval + 5))
        ;;
      access_denied)
        rm -f "$response_file"
        die "Revdoku connection was denied in the browser"
        ;;
      expired_token)
        rm -f "$response_file"
        die "device login expired; run 'revdoku login' again"
        ;;
      *)
        rm -f "$response_file"
        return 1
        ;;
    esac
  done
}

request_email_agent_key() {
  local email code payload response key

  while true; do
    email="$(prompt_read "Email: ")"
    [[ -n "$email" ]] || die "email is required"

    payload="$("$JQ_BIN" -nc --arg email "$email" '{email:$email}')"
    if http_json POST "/api/v1/agent_auth/request_code" "$payload" false >/dev/null; then
      break
    fi

    die "could not start email verification"
  done

  echo "If $email can receive Revdoku sign-in codes, a verification code was sent." >&2
  echo "If no code arrives, sign in at ${BASE_URL%/}/users/sign_in or retry browser device sign-in with 'revdoku login'." >&2

  code="$(prompt_read "Code: ")"
  [[ -n "$code" ]] || die "code is required"

  payload="$("$JQ_BIN" -nc --arg email "$email" --arg code "$code" '{email:$email, code:$code, label:"Revdoku bucket client"}')"
  if ! response="$(http_json POST "/api/v1/agent_auth/verify_code" "$payload" false)"; then
    die "Could not verify the code. If no code arrived or the code is rejected, use 'revdoku login' and complete browser device sign-in."
  fi
  key="$("$JQ_BIN" -r '.data.api_key // empty' <<<"$response")"
  [[ -n "$key" ]] || die "verification did not return an API key. Use 'revdoku login' and complete browser device sign-in."

  save_api_key "$key"
}

request_agent_key() {
  if request_device_agent_key; then
    return
  fi

  echo "Browser device login is unavailable on this Revdoku server; using legacy email-code fallback." >&2
  request_email_agent_key
}

exchange_agent_grant() {
  local token="$1" payload response key account_id account_name
  [[ -n "$token" ]] || die "one-time connection token is required"
  payload="$("$JQ_BIN" -nc --arg grant_token "$token" --arg label "${AGENT_NAME} connection" '{grant_token:$grant_token,label:$label}')"
  response="$(http_json POST "/api/v1/agent_auth/exchange_grant" "$payload" false)" \
    || die "connection token is invalid, expired, or already used"
  key="$("$JQ_BIN" -r '.data.api_key // empty' <<<"$response")"
  account_id="$("$JQ_BIN" -r '.data.account_id // empty' <<<"$response")"
  account_name="$("$JQ_BIN" -r '.data.account_name // empty' <<<"$response")"
  [[ -n "$key" ]] || die "connection response did not include an API key"
  save_api_key "$key"
  echo "Connected to Revdoku${account_name:+: $account_name}." >&2
  [[ -n "$account_id" ]] && echo "Account: $account_id" >&2
}

if [[ "$ACTION" == "exchange_grant" ]]; then
  exchange_agent_grant "$GRANT_TOKEN"
  echo "Connection complete. You can return to your AI agent." >&2
  exit 0
fi

# Bare `revdoku` with no saved credentials: show a friendly hint instead of
# forcing the interactive login flow.
if [[ "$ACTION" == "connection_status" && "$SHOW_UPLOAD_HINT" == "true" && -z "$API_KEY" ]]; then
  echo "Revdoku CLI — not signed in yet." >&2
  echo "  Sign in:   revdoku login" >&2
  echo "  Upload:    revdoku upload PATH" >&2
  echo "  Commands:  revdoku --help" >&2
  exit 0
fi

if [[ "$LOGIN" == "true" || -z "$API_KEY" ]]; then
  request_agent_key
fi

if [[ "$LOGIN" == "true" && "$ACTION" == "store" && "$PATH_EXPLICIT" == "false" ]]; then
  echo "Login complete. Credentials saved to $CREDENTIALS_PATH." >&2
  echo "Next: revdoku upload PATH, or revdoku dashboard." >&2
  exit 0
fi

[[ -n "$API_KEY" ]] || die "REVDOKU_API_KEY is required"
case "$UPLOAD_MODE" in
  auto|direct) ;;
  *) die "--upload-mode must be auto or direct" ;;
esac
list_buckets() {
  local active_response archived_response
  active_response="$(http_json GET "/api/v1/buckets" "{}")"
  archived_response="$(http_json GET "/api/v1/buckets?archived=true" "{}")"
  "$JQ_BIN" -nc \
    --argjson active "$active_response" \
    --argjson archived "$archived_response" \
    '
      ($active.data.buckets // []) as $active_buckets
      | ($archived.data.buckets // []) as $archived_buckets
      | ($active_buckets + $archived_buckets | unique_by(.id)) as $buckets
      | $active + {
          data: ($active.data + {
            buckets: $buckets,
            active_buckets_count: ($active_buckets | length),
            archived_buckets_count: ($archived_buckets | length),
            includes_archived: true
          })
        }
    '
}

list_versions() {
  [[ -n "$BUCKET_ID" ]] || die "versions requires --bucket-id"
  http_json GET "/api/v1/buckets/${BUCKET_ID}/versions" "{}"
}

list_files() {
  [[ -n "$BUCKET_ID" ]] || die "files requires --bucket-id (or a remembered selected bucket)"
  local path="/api/v1/buckets/${BUCKET_ID}/files"
  if [[ -n "$THREAD_FOR" ]]; then
    path="${path}?thread_for=$("$JQ_BIN" -rn --arg value "$THREAD_FOR" '$value | @uri')"
  fi
  http_json GET "$path" "{}"
}

# Read a bucket file's content by its bucket-relative path. Uses the by_path
# endpoint, which 302-redirects to a short-lived signed blob URL; curl -L follows
# it (and drops the bearer on the cross-host hop, as intended).
read_file() {
  [[ -n "$BUCKET_ID" ]] || die "read requires --bucket-id (or a remembered selected bucket)"
  [[ -n "$READ_FILE_PATH" ]] || die "read requires a bucket-relative PATH"
  [[ -n "$API_KEY" ]] || die "No Revdoku API key. Run 'revdoku login' first."

  local encoded url body_file status message
  encoded="$("$JQ_BIN" -rn --arg s "$READ_FILE_PATH" '$s|@uri')"
  url="$(api_url "$(account_request_path "/api/v1/buckets/${BUCKET_ID}/files/by_path?path=${encoded}&disposition=inline")")"
  body_file="$(mktemp 2>/dev/null || mktemp -t revdoku)"

  status="$(curl -sSL --max-time 120 -o "$body_file" -w "%{http_code}" \
    -H "Authorization: Bearer $API_KEY" -H "Accept: */*" "$url" 2>/dev/null || echo "000")"

  if [[ "$status" == 2* ]]; then
    if [[ -n "$OUTPUT_PATH" ]]; then
      mv "$body_file" "$OUTPUT_PATH"
      echo "Saved $READ_FILE_PATH to $OUTPUT_PATH" >&2
    else
      cat "$body_file"
      rm -f "$body_file"
    fi
    return 0
  fi

  message="$("$JQ_BIN" -r '.error.message // .message // empty' "$body_file" 2>/dev/null || true)"
  rm -f "$body_file"
  case "$status" in
    401|403) die "Not authorized to read '$READ_FILE_PATH'${message:+: $message}" ;;
    404) die "File not found at path '$READ_FILE_PATH' in bucket $BUCKET_ID" ;;
    000) die "Network error while reading '$READ_FILE_PATH'" ;;
    *) die "Failed to read '$READ_FILE_PATH' (HTTP ${status})${message:+: $message}" ;;
  esac
}

restore_version() {
  local payload
  [[ -n "$BUCKET_ID" ]] || die "restore requires --bucket-id"
  [[ -n "$RESTORE_VERSION_ID" ]] || die "restore requires a bucket version id"
  payload="$("$JQ_BIN" -nc \
    --arg version_id "$RESTORE_VERSION_ID" \
    --arg comment "$RESTORE_COMMENT" \
    '{version_id:$version_id} + (if $comment != "" then {comment:$comment} else {} end)')"
  http_json POST "/api/v1/buckets/${BUCKET_ID}/versions/restore" "$payload"
}

append_text_file() {
  local content_file tmp_content payload response path
  [[ -n "$BUCKET_ID" ]] || die "append requires --bucket-id"
  [[ -n "$APPEND_TEXT_PATH" ]] || die "append requires a bucket-relative PATH"

  tmp_content=""
  if [[ -n "$APPEND_TEXT_CONTENT_FILE" ]]; then
    if [[ "$APPEND_TEXT_CONTENT_FILE" == "-" ]]; then
      tmp_content="$(mktemp)"
      cat > "$tmp_content"
      content_file="$tmp_content"
    else
      [[ -f "$APPEND_TEXT_CONTENT_FILE" ]] || die "--content-file does not exist: $APPEND_TEXT_CONTENT_FILE"
      content_file="$APPEND_TEXT_CONTENT_FILE"
    fi
  else
    tmp_content="$(mktemp)"
    printf "%s" "$APPEND_TEXT_CONTENT" > "$tmp_content"
    content_file="$tmp_content"
  fi

  if [[ ! -s "$content_file" ]]; then
    [[ -z "$tmp_content" ]] || rm -f "$tmp_content"
    die "append content must not be empty"
  fi

  path="$APPEND_TEXT_PATH"
  payload="$("$JQ_BIN" -Rs \
    --arg path "$path" \
    --argjson newline_before "$APPEND_TEXT_NEWLINE_BEFORE" \
    '{path:$path, content: ., newline_before:$newline_before}' < "$content_file")"
  if ! response="$(http_json POST "/api/v1/buckets/${BUCKET_ID}/files/append_text" "$payload")"; then
    [[ -z "$tmp_content" ]] || rm -f "$tmp_content"
    return 1
  fi
  [[ -z "$tmp_content" ]] || rm -f "$tmp_content"
  printf "%s\n" "$response"
}

archive_bucket() {
  [[ -n "$BUCKET_ID" ]] || die "archive requires --bucket-id"
  http_json POST "/api/v1/buckets/${BUCKET_ID}/archive" "{}"
}

unarchive_bucket() {
  [[ -n "$BUCKET_ID" ]] || die "unarchive requires --bucket-id"
  http_json POST "/api/v1/buckets/${BUCKET_ID}/unarchive" "{}"
}

delete_bucket() {
  local bucket_response allowed required_action confirmation payload response deletion_started total_items phase
  [[ -n "$BUCKET_ID" ]] || die "delete requires --bucket-id"
  bucket_response="$(http_json GET "/api/v1/buckets/${BUCKET_ID}" "{}")"
  allowed="$("$JQ_BIN" -r '.data.bucket.delete.allowed // false' <<<"$bucket_response")"
  required_action="$("$JQ_BIN" -r '.data.bucket.delete.required_action // empty' <<<"$bucket_response")"
  confirmation="$("$JQ_BIN" -r '.data.bucket.delete.confirmation // empty' <<<"$bucket_response")"

  if [[ "$allowed" != "true" || -z "$confirmation" ]]; then
    case "$required_action" in
      archive_first)
        die "bucket must be archived before permanent delete; run 'revdoku archive' first"
        ;;
      *)
        die "bucket cannot be permanently deleted with this connection; review its action guidance in the dashboard"
        ;;
    esac
  fi

  payload="$("$JQ_BIN" -nc --arg confirmation "$confirmation" '{confirmation:$confirmation}')"
  response="$(http_json DELETE "/api/v1/buckets/${BUCKET_ID}" "$payload")" || return 1
  deletion_started="$("$JQ_BIN" -r '.data.bucket.deletion_started // false' <<<"$response")"
  if [[ "$deletion_started" == "true" ]]; then
    phase="$("$JQ_BIN" -r '.data.delete_progress.phase // "queued"' <<<"$response")"
    total_items="$("$JQ_BIN" -r '.data.delete_progress.total_items // empty' <<<"$response")"
    if [[ -n "$total_items" ]]; then
      echo "Bucket deletion ${phase}; ${total_items} file/version items will be removed in the background. Poll 'revdoku ls' or bucket details for delete progress." >&2
    else
      echo "Bucket deletion ${phase}; removal will continue in the background. Poll 'revdoku ls' or bucket details for delete progress." >&2
    fi
  fi
  printf "%s\n" "$response"
}

connection_status() {
  http_json GET "/api/v1/status" "{}" | "$JQ_BIN" -c '{
    success: (.success // true),
    data: {
      connected: (.data.connected // true),
      account: .data.account,
      default_account_id: .data.default_account_id,
      accounts: .data.accounts,
      connection: .data.connection,
      features: .data.features,
      onboarding: .data.onboarding
    }
  }'
}

create_client_account() {
  local payload
  payload="$("$JQ_BIN" -cn --arg name "$CLIENT_ACCOUNT_NAME" --arg client_name "$CLIENT_DISPLAY_NAME" '{name: $name} + (if $client_name == "" then {} else {client_name: $client_name} end)')"
  http_json POST "/api/v1/accounts" "$payload"
}

account_status() {
  local identity
  identity="$(http_json GET "/api/v1/status" "{}")"
  if [[ "$(printf '%s' "$identity" | "$JQ_BIN" -r '.data.account.account_kind // .data.account.kind')" == "client" ]]; then
    printf '%s\n' "$identity"
    return
  fi
  http_json GET "/api/v1/account/credits" "{}" | "$JQ_BIN" --argjson identity "$identity" -c '
    .data.credits as $credits
    | ($credits.account_limits // {}) as $limits
    | {
        success: (.success // true),
        data: {
          account: $identity.data.account,
          default_account_id: $identity.data.default_account_id,
          accounts: $identity.data.accounts,
          plan: ($credits.plan // {}),
          storage: {
            used_bytes: $limits.used_storage_bytes,
            used_human: $limits.used_storage_human,
            available_bytes: $limits.available_storage_bytes,
            available_human: $limits.available_storage_human,
            max_mb: $limits.max_storage_mb,
            max_human: $limits.max_storage_human,
            max_file_size_mb: $limits.max_file_size_mb,
            max_file_size_human: $limits.max_file_size_human
          },
          connections: {
            max: $limits.max_account_connections,
            max_account_members: $limits.max_account_members,
            max_api_keys: $limits.max_api_keys,
            max_agent_connections: $limits.max_agent_connections,
            active_api_keys_count: $limits.active_api_keys_count,
            active_agent_connections_count: $limits.active_agent_connections_count,
            api_rate_limit_requests_per_minute: $limits.api_rate_limit_requests_per_minute
          },
          credits: {
            balance: $credits.balance,
            subscription: $credits.subscription,
            purchased: $credits.purchased,
            total: $credits.total,
            purchased_expires_at: $credits.purchased_expires_at,
            next_refill_at: $credits.next_refill_at,
            one_time_credits_purchasable: $credits.one_time_credits_purchasable
          }
        }
      }'
}

print_terminal_link_hint() {
  if [[ -t 2 ]]; then
    echo "Tip: Cmd-click the link on macOS, or Ctrl-click it on Windows/Linux, if your terminal supports clickable links." >&2
  fi
}

browser_login_link() {
  local payload response url redirect_path
  payload="$("$JQ_BIN" -nc --arg redirect_path "$BROWSER_LOGIN_PATH" '{redirect_path:$redirect_path}')"
  response="$(http_json POST "/api/v1/agent_auth/browser_login_link" "$payload")"
  url="$("$JQ_BIN" -r '.data.url // empty' <<<"$response")"
  redirect_path="$("$JQ_BIN" -r '.data.redirect_path // empty' <<<"$response")"
  [[ -n "$url" ]] || die "browser login response did not include url"
  echo "Open Revdoku: $url" >&2
  [[ -n "$redirect_path" ]] && echo "Destination: $redirect_path" >&2
  echo "Sign in normally if your browser does not already have a Revdoku session." >&2
  print_terminal_link_hint
  printf "%s\n" "$url"
}

# Best-effort, throttled (~24h), never-blocking notice when the server advertises
# a newer client/connector version than the one install.sh stamped. Compares the
# server's /api/v1/status client_version against ~/.revdoku/client_version and
# only nudges when the server version is strictly newer (numeric compare via jq;
# avoids relying on `sort -V`, which is unavailable on busybox/older BSD sort).
maybe_notify_update() {
  [[ -n "$API_KEY" ]] || return 0
  command -v "$JQ_BIN" >/dev/null 2>&1 || return 0

  local now last installed latest body
  now="$(date +%s 2>/dev/null || echo 0)"
  if [[ -f "$UPDATE_CHECK_STAMP" ]]; then
    last="$(cat "$UPDATE_CHECK_STAMP" 2>/dev/null || echo 0)"
    if [[ "$now" -gt 0 && "$last" =~ ^[0-9]+$ && $((now - last)) -lt 86400 ]]; then
      return 0
    fi
  fi
  mkdir -p "$REVDOKU_CONFIG_DIR" 2>/dev/null || true
  printf '%s' "$now" > "$UPDATE_CHECK_STAMP" 2>/dev/null || true

  installed="$(installed_client_version)"
  [[ "$installed" != "unknown" ]] || return 0
  body="$(curl -fsS --max-time 5 "$(api_url "/api/v1/status")" -H "Authorization: Bearer $API_KEY" -H "Accept: application/json" 2>/dev/null || true)"
  [[ -n "$body" ]] || return 0
  latest="$("$JQ_BIN" -r '.data.client_version // empty' <<<"$body" 2>/dev/null || true)"
  [[ -n "$latest" && "$latest" != "$installed" ]] || return 0
  if "$JQ_BIN" -ne --arg inst "$installed" --arg lat "$latest" \
    '($inst | split(".") | map(tonumber? // 0)) < ($lat | split(".") | map(tonumber? // 0))' >/dev/null 2>&1; then
    echo "Revdoku CLI update available (${installed} → ${latest}). Update using your original installation method: https://revdoku.com/llms-install.md" >&2
  fi
}

maybe_notify_update || true

case "$ACTION" in
  list_buckets)
    list_buckets
    exit 0
    ;;
  inbox_status)
    [[ -n "$BUCKET_ID" ]] || die "inbox requires --bucket-id or a bound folder"
    http_json GET "/api/v1/buckets/${BUCKET_ID}/inbound_email" "{}"
    exit 0
    ;;
  list_files)
    list_files
    exit 0
    ;;
  read_file)
    read_file
    exit 0
    ;;
  list_versions)
    list_versions
    exit 0
    ;;
  restore_version)
    restore_version
    exit 0
    ;;
  append_text_file)
    append_text_file
    exit 0
    ;;
  archive_bucket)
    archive_bucket
    exit 0
    ;;
  unarchive_bucket)
    unarchive_bucket
    exit 0
    ;;
  delete_bucket)
    delete_bucket
    exit 0
    ;;
  create_client_account)
    create_client_account
    exit 0
    ;;
  account_status)
    account_status
    exit 0
    ;;
  connection_status)
    connection_status
    if [[ "$SHOW_UPLOAD_HINT" == "true" ]]; then
      echo "Tip: run 'revdoku upload .' to save this folder, or 'revdoku --help' for all commands." >&2
    fi
    exit 0
    ;;
  open_dashboard)
    open_dashboard
    exit 0
    ;;
esac

[[ -e "$PATH_TO_STORE" ]] || die "$PATH_TO_STORE does not exist"

abs_path() {
  local path="$1"
  if [[ -d "$path" ]]; then
    (cd "$path" && pwd)
  else
    local dir base
    dir="$(dirname "$path")"
    base="$(basename "$path")"
    printf "%s/%s" "$(cd "$dir" && pwd)" "$base"
  fi
}

ROOT_PATH="$(abs_path "$PATH_TO_STORE")"

default_title() {
  # ROOT_PATH is absolute. Use the folder name, but if it's a generic build
  # output dir (docs/dist/build/...), use the project (parent) dir name instead,
  # so e.g. ~/projects/my-site/docs -> "my-site".
  local name parent
  name="$(basename "$ROOT_PATH")"
  if [[ -d "$ROOT_PATH" ]]; then
    case "$name" in
      docs|dist|build|public|out|_site|site|www|html|htdocs|wwwroot|public_html|_public)
        parent="$(basename "$(dirname "$ROOT_PATH")")"
        [[ -n "$parent" && "$parent" != "/" && "$parent" != "." ]] && name="$parent"
        ;;
    esac
  fi
  printf '%s\n' "$name"
}

effective_metadata_json() {
  printf "%s" "$METADATA_JSON"
}

content_type_for() {
  local file="$1"
  local lower="${file##*.}"
  lower="$(printf "%s" "$lower" | tr '[:upper:]' '[:lower:]')"
  case "$lower" in
    html|htm) echo "text/html" ;;
    css|csss|scss|sass|less|styl|stylus) echo "text/css" ;;
    js|mjs|cjs) echo "text/javascript" ;;
    map) echo "application/json" ;;
    webmanifest) echo "application/manifest+json" ;;
    json) echo "application/json" ;;
    txt) echo "text/plain" ;;
    md) echo "text/markdown" ;;
    png) echo "image/png" ;;
    apng) echo "image/apng" ;;
    jpg|jpe|jpeg|jfif|pjp|pjpeg) echo "image/jpeg" ;;
    webp) echo "image/webp" ;;
    gif) echo "image/gif" ;;
    avif) echo "image/avif" ;;
    bmp) echo "image/bmp" ;;
    ico|cur) echo "image/x-icon" ;;
    heic|heics) echo "image/heic" ;;
    heif|heifs) echo "image/heif" ;;
    jp2) echo "image/jp2" ;;
    svg) echo "image/svg+xml" ;;
    woff) echo "font/woff" ;;
    woff2) echo "font/woff2" ;;
    ttf) echo "font/ttf" ;;
    otf) echo "font/otf" ;;
    wasm) echo "application/wasm" ;;
    pdf) echo "application/pdf" ;;
    xml) echo "application/xml" ;;
    rss) echo "application/rss+xml" ;;
    atom) echo "application/atom+xml" ;;
    mp4) echo "video/mp4" ;;
    mov) echo "video/quicktime" ;;
    webm) echo "video/webm" ;;
    m4v) echo "video/x-m4v" ;;
    ogv) echo "video/ogg" ;;
    avi) echo "video/x-msvideo" ;;
    mkv) echo "video/x-matroska" ;;
    mpg|mpeg) echo "video/mpeg" ;;
    ts) echo "video/mp2t" ;;
    m3u8) echo "application/vnd.apple.mpegurl" ;;
    mp3) echo "audio/mpeg" ;;
    ogg|oga) echo "audio/ogg" ;;
    wav) echo "audio/wav" ;;
    m4a) echo "audio/mp4" ;;
    aac) echo "audio/aac" ;;
    flac) echo "audio/flac" ;;
    opus) echo "audio/opus" ;;
    *) echo "application/octet-stream" ;;
  esac
}

file_size() {
  wc -c < "$1" | tr -d '[:space:]'
}

md5_base64() {
  openssl dgst -md5 -binary "$1" | base64 | tr -d '\r\n'
}

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | awk '{print $1}'
  else
    openssl dgst -sha256 "$1" | awk '{print $2}'
  fi
}

relative_path_for() {
  local file="$1"
  if [[ -f "$ROOT_PATH" ]]; then
    basename "$file"
  else
    printf "%s/%s" "$(basename "$ROOT_PATH")" "${file#"$ROOT_PATH"/}"
  fi
}

local_file_for_relative_path() {
  local rel="$1"
  local root_name
  if [[ -f "$ROOT_PATH" ]]; then
    printf "%s" "$ROOT_PATH"
    return
  fi

  root_name="$(basename "$ROOT_PATH")"
  if [[ "$rel" == "$root_name/"* ]]; then
    printf "%s/%s" "$ROOT_PATH" "${rel#"$root_name"/}"
  else
    printf "%s/%s" "$ROOT_PATH" "$rel"
  fi
}

create_bucket() {
  local title payload response id
  title="$TITLE"
  [[ -n "$title" ]] || title="$(default_title)"
  payload="$(bucket_payload "$title")"
  response="$(http_json POST "/api/v1/buckets" "$payload")" || die "bucket create failed"
  id="$("$JQ_BIN" -r '.data.bucket.id // empty' <<<"$response")"
  [[ -n "$id" ]] || die "bucket create response did not include id"
  printf "%s" "$id"
}

tag_paths_json() {
  if [[ "${#TAG_PATHS[@]}" -eq 0 ]]; then
    printf "[]"
  else
    "$JQ_BIN" -nc '$ARGS.positional' --args "${TAG_PATHS[@]}"
  fi
}

bucket_payload() {
  local title="$1"
  local tag_paths metadata client_create_key
  tag_paths="$(tag_paths_json)"
  metadata="$(effective_metadata_json)"
  client_create_key="$(bucket_client_create_key "$title" "$metadata" "$tag_paths")"
  "$JQ_BIN" -nc \
    --arg title "$title" \
    --arg description "$DESCRIPTION" \
    --arg client_create_key "$client_create_key" \
    --argjson metadata "$metadata" \
    --argjson tag_paths "$tag_paths" \
    '{
      bucket: (
        {title: $title, metadata: ($metadata + {"_revdoku_client_create_key": $client_create_key})}
        + (if $description != "" then {description: $description} else {} end)
        + (if ($tag_paths | length) > 0 then {tag_paths: $tag_paths} else {} end)
      )
    }'
}

bucket_client_create_key() {
  local title="$1"
  local metadata="$2"
  local tag_paths="$3"
  local digest
  digest="$(printf "%s\n%s\n%s\n%s\n%s" "$title" "$ROOT_PATH" "$metadata" "$tag_paths" "$AGENT_RUN_ID" | openssl dgst -sha256 -hex | awk '{print $2}')"
  printf "cli:%s" "$digest"
}

bucket_update_payload() {
  local tag_paths
  tag_paths="$(tag_paths_json)"
  "$JQ_BIN" -nc \
    --arg title "$TITLE" \
    --arg description "$DESCRIPTION" \
    --argjson metadata "$METADATA_JSON" \
    --argjson tag_paths "$tag_paths" \
    '{
      bucket: (
        {}
        + (if $title != "" then {title: $title} else {} end)
        + (if $description != "" then {description: $description} else {} end)
        + (if ($metadata | length) > 0 then {metadata: $metadata} else {} end)
        + (if ($tag_paths | length) > 0 then {tag_paths: $tag_paths} else {} end)
      )
    }'
}

bucket_update_needed() {
  [[ "$METADATA_JSON" != "{}" || -n "$DESCRIPTION" || "${#TAG_PATHS[@]}" -gt 0 ]]
}

put_direct_upload() {
  local upload_json="$1"
  local file="$2"
  local url header_args=() body_file status curl_status attempt delay
  LAST_DIRECT_UPLOAD_STATUS=""
  url="$("$JQ_BIN" -r '.url // empty' <<<"$upload_json")"
  [[ -n "$url" ]] || return 1

  while IFS=$'\t' read -r key value; do
    [[ -n "$key" ]] || continue
    header_args+=(-H "${key}: ${value}")
  done < <("$JQ_BIN" -r '.headers // {} | to_entries[] | [.key, .value] | @tsv' <<<"$upload_json")

  attempt=0
  while true; do
    body_file="$(mktemp)"
    # Bash 3 with nounset treats an empty array as unset.
    if status="$(curl -sS -o "$body_file" -w "%{http_code}" -X PUT ${header_args[@]+"${header_args[@]}"} --data-binary "@${file}" "$url")"; then
      curl_status=0
    else
      curl_status=$?
    fi

    if [[ "$curl_status" == "0" ]] && http_status_success "$status"; then
      LAST_DIRECT_UPLOAD_STATUS="$status"
      rm -f "$body_file"
      return 0
    fi

    if (( attempt < DIRECT_UPLOAD_MAX_ATTEMPTS )) && { [[ "$curl_status" != "0" ]] || http_status_retryable "$status"; }; then
      attempt=$((attempt + 1))
      delay="$(retry_delay_for_attempt "$attempt")"
      if [[ "$curl_status" != "0" ]]; then
        echo "Direct upload network error; retrying in ${delay}s (${attempt}/${DIRECT_UPLOAD_MAX_ATTEMPTS})..." >&2
      else
        echo "Direct upload HTTP $status; retrying in ${delay}s (${attempt}/${DIRECT_UPLOAD_MAX_ATTEMPTS})..." >&2
      fi
      rm -f "$body_file"
      sleep "$delay"
      continue
    fi

    if [[ "$curl_status" != "0" ]]; then
      LAST_DIRECT_UPLOAD_STATUS=""
      echo "error: direct upload failed (curl exit $curl_status)" >&2
    else
      LAST_DIRECT_UPLOAD_STATUS="$status"
      echo "error: direct upload failed (HTTP $status)" >&2
      if [[ -s "$body_file" ]]; then
        cat "$body_file" >&2
      fi
    fi
    rm -f "$body_file"
    return 1
  done
}

upload_file_direct() {
  local bucket_id="$1"
  local file="$2"
  local file_list
  file_list="$(mktemp)"
  printf "%s\0" "$file" > "$file_list"
  store_bucket_session_upload "$bucket_id" "$file_list"
  local status=$?
  rm -f "$file_list"
  return "$status"
}

upload_file() {
  local bucket_id="$1"
  local file="$2"
  local rel
  rel="$(relative_path_for "$file")"
  echo "Uploading $rel" >&2

  upload_file_direct "$bucket_id" "$file"
}

bucket_upload_session_manifest_json() {
  local file_list="$1"
  local manifest_lines rel filename content_type size checksum sha256
  manifest_lines="$(mktemp)"
  while IFS= read -r -d '' file; do
    rel="$(relative_path_for "$file")"
    filename="$(basename "$file")"
    content_type="$(content_type_for "$file")"
    size="$(file_size "$file")"
    checksum="$(md5_base64 "$file")"
    sha256="$(sha256_file "$file")"
    "$JQ_BIN" -nc \
      --arg path "$rel" \
      --argjson byte_size "$size" \
      --arg content_type "$content_type" \
      --arg checksum "$checksum" \
      --arg sha256 "$sha256" \
      '{path:$path, byte_size:$byte_size, content_type:$content_type, checksum:$checksum, sha256:$sha256}' >> "$manifest_lines"
  done < "$file_list"
  "$JQ_BIN" -sc '.' "$manifest_lines"
  rm -f "$manifest_lines"
}

bucket_upload_session_client_key() {
  local bucket_id="$1"
  local manifest_json="$2"
  local delete_missing="${3:-false}"
  local digest
  if [[ -n "$BUCKET_UPLOAD_CLIENT_SESSION_KEY" ]]; then
    printf "%s" "$BUCKET_UPLOAD_CLIENT_SESSION_KEY"
    return 0
  fi
  digest="$(printf "%s:%s:%s" "$bucket_id" "$manifest_json" "$delete_missing" | openssl dgst -sha256 -hex | awk '{print $2}')"
  printf "cli:%s:%s" "$bucket_id" "$digest"
}

bucket_upload_session_payload() {
  local client_session_key="$1"
  local expected_file_count="$2"
  local delete_missing="${3:-false}"
  "$JQ_BIN" -nc \
    --arg client_session_key "$client_session_key" \
    --argjson expected_file_count "$expected_file_count" \
    --arg delete_missing "$delete_missing" \
    '{
      client_session_key: $client_session_key,
      expected_file_count: $expected_file_count
    }
    + (if $delete_missing == "true" then {delete_missing: true} else {} end)'
}

prepare_bucket_upload_descriptors() {
  local bucket_id="$1"
  local session_id="$2"
  local batch_json="$3"
  local payload
  payload="$("$JQ_BIN" -nc --argjson files "$batch_json" '{files: $files}')"
  http_json POST "/api/v1/buckets/${bucket_id}/upload_sessions/${session_id}/uploads" "$payload"
}

finalize_bucket_upload_session() {
  local bucket_id="$1"
  local session_id="$2"
  local complete="${3:-true}"
  local payload response pending attempts=0 remaining
  local max_attempts="${REVDOKU_FINALIZE_MAX_ATTEMPTS:-1000}"
  [[ -n "$session_id" ]] || return 0
  "$JQ_BIN" -nc --argjson complete "$complete" '{complete:$complete}' | {
    payload="$(cat)"
    while :; do
      response="$(http_json POST "/api/v1/buckets/${bucket_id}/upload_sessions/${session_id}/finalize" "$payload")" || return 1
      pending="$("$JQ_BIN" -r '.data.finalize_pending // false' <<<"$response")"
      [[ "$pending" == "true" && "$complete" == "true" ]] || return 0
      attempts=$((attempts + 1))
      remaining="$("$JQ_BIN" -r '.data.remaining_files_count // .data.bucket_upload_session.remaining_files_count // empty' <<<"$response" 2>/dev/null || true)"
      if (( attempts == 1 || attempts % 5 == 0 )); then
        if [[ -n "$remaining" && "$remaining" != "null" ]]; then
          echo "Still finalizing ${remaining} file(s)… (attempt ${attempts})" >&2
        else
          echo "Still finalizing files… (attempt ${attempts})" >&2
        fi
      fi
      if (( attempts >= max_attempts )); then
        echo "Timed out finalizing the upload session after ${attempts} attempts (~$((attempts * 2 / 60)) min)." >&2
        echo "Files may still be processing in the background; re-run the command to resume." >&2
        return 1
      fi
      sleep 2
    done
  }
}

finalize_bucket_upload_session_batch() {
  local bucket_id="$1"
  local session_id="$2"
  local limit="${3:-100}"
  local attempts=0 missing_entry_json missing_path
  [[ -n "$session_id" ]] || return 0
  "$JQ_BIN" -nc --argjson limit "$limit" '{limit:$limit}' | {
    local payload
    payload="$(cat)"
    while :; do
      if http_json POST "/api/v1/buckets/${bucket_id}/upload_sessions/${session_id}/finalize_batch" "$payload" >/dev/null; then
        return 0
      fi

      if [[ "${LAST_ERROR_CODE:-}" == "DIRECT_UPLOAD_NOT_FOUND" && "$attempts" -lt "$BUCKET_UPLOAD_DESCRIPTOR_BATCH_SIZE" ]]; then
        missing_entry_json="$LAST_ERROR_DETAILS_JSON"
        missing_path="$("$JQ_BIN" -r '.path // empty' <<<"$missing_entry_json" 2>/dev/null || true)"
        if [[ -n "$missing_path" ]] && upload_bucket_session_missing_entry "$bucket_id" "$session_id" "$missing_entry_json"; then
          attempts=$((attempts + 1))
          echo "Retrying bucket upload batch finalize after refreshing $missing_path." >&2
          continue
        fi
      fi

      return 1
    done
  }
}

upload_bucket_session_missing_entry() {
  local bucket_id="$1"
  local session_id="$2"
  local entry_json="$3"
  local rel file response upload_json

  rel="$("$JQ_BIN" -r '.path // empty' <<<"$entry_json" 2>/dev/null || true)"
  [[ -n "$rel" ]] || return 1
  file="$(local_file_for_relative_path "$rel")"
  [[ -f "$file" ]] || {
    echo "error: upload session asked to refresh unknown upload path: $rel" >&2
    return 1
  }

  echo "Refreshing missing direct upload for $rel." >&2
  response="$(prepare_bucket_upload_descriptors "$bucket_id" "$session_id" "[$entry_json]")" || return 1
  upload_json="$("$JQ_BIN" -c '.data.uploads[0].upload // empty' <<<"$response")"
  [[ -n "$upload_json" && "$upload_json" != "null" ]] || return 1

  echo "Uploading $rel" >&2
  put_direct_upload "$upload_json" "$file"
}

store_bucket_session_upload() {
  local bucket_id="$1"
  local file_list="$2"
  local delete_missing="${3:-false}"
  local manifest_json payload response session_id upload_line rel upload_json file batch_json batch_response expected_file_count client_session_key failed=0 finalized=0 entry_json refresh_response uploaded_index=0
  manifest_json="$(bucket_upload_session_manifest_json "$file_list")"
  expected_file_count="$("$JQ_BIN" -r 'length' <<<"$manifest_json")"
  client_session_key="$(bucket_upload_session_client_key "$bucket_id" "$manifest_json" "$delete_missing")"
  payload="$(bucket_upload_session_payload "$client_session_key" "$expected_file_count" "$delete_missing")"
  response="$(http_json POST "/api/v1/buckets/${bucket_id}/upload_sessions" "$payload")" || return 1
  session_id="$("$JQ_BIN" -r '.data.bucket_upload_session.id // empty' <<<"$response")"
  [[ -n "$session_id" ]] || die "bucket upload session response did not include id"
  echo "Bucket upload session: $session_id" >&2

  while IFS= read -r batch_json; do
    [[ -n "$batch_json" && "$batch_json" != "[]" ]] || continue
    batch_response="$(prepare_bucket_upload_descriptors "$bucket_id" "$session_id" "$batch_json")" || {
      failed=1
      break
    }
    while IFS= read -r upload_line; do
      [[ -n "$upload_line" ]] || continue
      rel="$("$JQ_BIN" -r '.path' <<<"$upload_line")"
      upload_json="$("$JQ_BIN" -c '.upload' <<<"$upload_line")"
      file="$(local_file_for_relative_path "$rel")"
      [[ -f "$file" ]] || {
        echo "error: upload session asked for unknown upload path: $rel" >&2
        failed=1
        break
      }
      uploaded_index=$((uploaded_index + 1))
      echo "Uploading ${uploaded_index}/${expected_file_count}: $rel" >&2
      if ! put_direct_upload "$upload_json" "$file"; then
        if [[ "${LAST_DIRECT_UPLOAD_STATUS:-}" == "403" || "${LAST_DIRECT_UPLOAD_STATUS:-}" == "404" ]]; then
          entry_json="$("$JQ_BIN" -c --arg rel "$rel" 'map(select(.path == $rel))[0] // empty' <<<"$batch_json")"
          if [[ -n "$entry_json" ]] && refresh_response="$(prepare_bucket_upload_descriptors "$bucket_id" "$session_id" "[$entry_json]")"; then
            upload_json="$("$JQ_BIN" -c '.data.uploads[0].upload // empty' <<<"$refresh_response")"
            if [[ -n "$upload_json" ]] && put_direct_upload "$upload_json" "$file"; then
              continue
            fi
          fi
        fi
        echo "error: upload failed for $rel" >&2
        failed=1
        break
      fi
    done < <("$JQ_BIN" -c '.data.uploads[]?' <<<"$batch_response")
    [[ "$failed" == "0" ]] || break

    if [[ "$delete_missing" != "true" ]] && ! finalize_bucket_upload_session_batch "$bucket_id" "$session_id" "$BUCKET_UPLOAD_DESCRIPTOR_BATCH_SIZE"; then
      failed=1
      break
    fi
  done < <("$JQ_BIN" -c --argjson size "$BUCKET_UPLOAD_DESCRIPTOR_BATCH_SIZE" 'range(0; length; $size) as $i | .[$i:($i + $size)]' <<<"$manifest_json")

  if [[ "$failed" == "0" ]] && finalize_bucket_upload_session "$bucket_id" "$session_id" true; then
    finalized=1
  else
    failed=1
  fi
  if [[ "$finalized" != "1" ]]; then
    finalize_bucket_upload_session "$bucket_id" "$session_id" false >/dev/null 2>&1 || true
  fi
  return "$failed"
}

bucket_id_for_storage() {
  if [[ -n "$BUCKET_ID" ]]; then
    if bucket_update_needed; then
      local payload
      payload="$(bucket_update_payload)"
      http_json PATCH "/api/v1/buckets/${BUCKET_ID}" "$payload" >/dev/null
    fi
    printf "%s" "$BUCKET_ID"
  else
    create_bucket
  fi
}

store_bucket() {
  local bucket_id bucket_id_file file_list
  file_list="$(mktemp)"
  if ! collect_files > "$file_list"; then
    rm -f "$file_list"
    return 1
  fi
  if [[ ! -s "$file_list" ]]; then
    rm -f "$file_list"
    die "no files found to store after safety exclusions"
  fi

  bucket_id_file="$(mktemp)"
  if ! bucket_id_for_storage > "$bucket_id_file"; then
    rm -f "$bucket_id_file" "$file_list"
    return 1
  fi
  bucket_id="$(cat "$bucket_id_file")"
  rm -f "$bucket_id_file"
  [[ -n "$bucket_id" ]] || {
    rm -f "$file_list"
    die "bucket id is required before uploading files"
  }
  echo "Bucket: $bucket_id" >&2
  echo "Saved bucket: $bucket_id" >&2
  store_bucket_session_upload "$bucket_id" "$file_list" false || {
    rm -f "$file_list"
    return 1
  }
  rm -f "$file_list"
  printf "%s" "$bucket_id"
}

collect_files() {
  if [[ -f "$ROOT_PATH" ]]; then
    if should_skip_storage_path "$ROOT_PATH"; then
      die "refusing to store file from Revdoku upload safety list: $(basename "$ROOT_PATH")"
    fi
    printf "%s\0" "$ROOT_PATH"
    return
  fi

  find "$ROOT_PATH" \
    \( -type d \( -name ".git" -o -name ".hg" -o -name ".svn" -o -name ".revdoku" -o -name ".terraform" -o -name ".cache" -o -name ".parcel-cache" -o -name ".turbo" -o -name ".vite" -o -name ".next" -o -name ".astro" -o -name "node_modules" \) -prune \) \
    -o -type f -print0 |
    while IFS= read -r -d '' file; do
      if should_skip_storage_path "$file"; then
        echo "Skipping file from Revdoku upload safety list: $(relative_path_for "$file")" >&2
        continue
      fi
      printf "%s\0" "$file"
    done
}

should_skip_storage_path() {
  local file="$1"
  local rel name lower_rel lower_name part extension
  rel="$(relative_path_for "$file")"
  name="$(basename "$file")"
  lower_rel="$(printf "%s" "$rel" | tr '[:upper:]' '[:lower:]')"
  lower_name="$(printf "%s" "$name" | tr '[:upper:]' '[:lower:]')"

  # The pattern lines below are GENERATED from apps/web/config/upload_safety.json by
  # scripts/generate-cli-upload-safety.rb so the CLI's local skip-list never drifts
  # from the server policy (the server is the hard gate; this is a local-UX mirror).
  # Edit the JSON and re-run the generator — do not hand-edit between the markers.
  IFS='/' read -r -a path_parts <<< "$lower_rel"
  for part in "${path_parts[@]}"; do
    case "$part" in
      # >>> revdoku:generated local_only_basenames
      .ds_store|__macosx|.localized|.appledouble|.lsoverride|.documentrevisions-v100|.fseventsd|.spotlight-v100|.temporaryitems|.trashes|.volumeicon.icns|.appledb|.appledesktop|.apdisk|network\ trash\ folder|temporary\ items|thumbs.db|thumbs.db:encryptable|ehthumbs.db|ehthumbs_vista.db|desktop.ini|\$recycle.bin|system\ volume\ information|.directory|.trash|lost+found|.git|.hg|.svn|.revdoku|.terraform|.cache|.parcel-cache|.turbo|.vite|.next|.astro|node_modules)
      # <<< revdoku:generated local_only_basenames
        return 0
        ;;
      # >>> revdoku:generated local_only_name_globs
      ._*|.trash-*|.fuse_hidden*|.nfs*)
      # <<< revdoku:generated local_only_name_globs
        return 0
        ;;
      agents.md|claude.md)
        # Keep local agent-instruction files out of bulk uploads.
        return 0
        ;;
      # >>> revdoku:generated prohibited_basenames
      .env|.npmrc|.pypirc|.netrc|id_rsa|id_rsa.pub|id_dsa|id_dsa.pub|id_ecdsa|id_ecdsa.pub|id_ed25519|id_ed25519.pub)
      # <<< revdoku:generated prohibited_basenames
        return 0
        ;;
      # >>> revdoku:generated prohibited_name_globs
      .env.*|env.local|env.production|env.staging|env.development|env.test|*.pem|*.key|*.p12|*.pfx|*.crt|*.cer|*.der|*.kdb|*.jks|*.mobileprovision|api-token.*|api_key.*|credentials.*|credential.*|secrets.*|secret.*|*.secret|*.secrets|private-key.*|private_key.*)
      # <<< revdoku:generated prohibited_name_globs
        return 0
        ;;
    esac
  done

  extension="${lower_name##*.}"
  if [[ "$lower_name" == *.* && "$extension" != "$lower_name" ]]; then
    case ".${extension}" in
      # >>> revdoku:generated prohibited_extensions
      .exe|.com|.scr|.pif|.cpl|.dll|.sys|.drv|.msi|.msp|.app|.dmg|.pkg|.deb|.rpm|.apk|.ipa|.jar|.jnlp|.run|.bin|.lnk|.pem|.key|.p12|.pfx|.crt|.cer|.der|.kdb|.jks|.mobileprovision|.zip|.zipx|.tar|.rar|.gz|.gzip|.tgz|.bz2|.tbz|.tbz2|.xz|.txz|.7z|.z|.lz|.lzma|.lz4|.zst|.zstd|.cab|.arj|.lzh|.lha|.war|.ear|.iso|.img|.vhd|.vhdx|.vmdk)
      # <<< revdoku:generated prohibited_extensions
        return 0
        ;;
    esac
  fi

  return 1
}

bucket_id_file="$(mktemp)"
if ! store_bucket > "$bucket_id_file"; then
  rm -f "$bucket_id_file"
  die "bucket store failed"
fi
bucket_id="$(cat "$bucket_id_file")"
rm -f "$bucket_id_file"
echo "Saved bucket: $bucket_id" >&2

# stdout stays the bucket ID for scripts; the dashboard link goes to stderr.
echo "View in Revdoku: $BASE_URL/buckets/view?id=$bucket_id" >&2
write_project_binding "$bucket_id" ""
print_terminal_link_hint
printf "%s\n" "$bucket_id"
