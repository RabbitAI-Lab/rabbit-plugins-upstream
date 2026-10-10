# shellcheck shell=bash
# Shared helpers for the Open Agent Guide batch scripts. Source it, don't run it:
#   . "$(dirname "$0")/oag-common.sh"
#
# Requires: bash, curl, jq. Reads $OAG_TOKEN (bearer, prefix oag_) and
# $OAG_BASE_URL (defaults to https://www.openagentguide.com).
: "${OAG_BASE_URL:=https://www.openagentguide.com}"

# Submission mutations are throttled at 20/min + a 5/second burst. Pausing ~3.5s
# between mutating calls keeps a batch under the per-minute ceiling with headroom
# for the automatic retries below; reads are cheaper (120/min) but share the pace.
: "${OAG_MUTATION_PACE_SECONDS:=3.5}"

# Max attempts for a single call before giving up (used for 429 back-off).
: "${OAG_MAX_ATTEMPTS:=5}"

# Output variables: oag_api sets these for the caller to read AFTER the call.
# oag_api returns its results through shell globals, so callers must invoke it
# directly — never in a command-substitution subshell (`resp="$(oag_api ...)"`),
# whose child shell discards the assignments and leaves the status empty (the
# "HTTP ?" bug this pair of variables fixes). Read $OAG_LAST_STATUS and
# $OAG_LAST_BODY on the following line instead.
export OAG_LAST_STATUS=""
export OAG_LAST_BODY=""

oag_require_token() {
  if [ -z "${OAG_TOKEN:-}" ]; then
    echo "OAG_TOKEN is not set. Export your oag_ bearer token first." >&2
    exit 1
  fi
}

# oag_api METHOD PATH [JSON_BODY]
#
# Issues one authenticated request against $OAG_BASE_URL. On a 429 it waits and
# retries up to $OAG_MAX_ATTEMPTS — honoring Retry-After if present, else pausing
# $OAG_MUTATION_PACE_SECONDS. (The submission-mutation throttle currently sends no
# Retry-After, so the pace fallback is what fires; signup does send one.) Always
# returns 0: the caller reads the outcome from $OAG_LAST_STATUS and $OAG_LAST_BODY
# — a 4xx/5xx body is still captured so the caller can inspect the error envelope
# ({ "code", "detail" } or, on the public API, { "errors": {…} }). A transport
# failure surfaces as $OAG_LAST_STATUS "000" (curl's code for no response), which
# no success branch treats as OK.
oag_api() {
  local method path body attempt tmp_headers resp status retry_after wait_s
  method="$1"
  path="$2"
  body="${3:-}"
  attempt=1

  while :; do
    tmp_headers="$(mktemp)"
    # `|| true` keeps a curl transport failure (DNS, refused, timeout) from
    # aborting the caller under `set -e`: curl still writes "000" via -w before it
    # exits non-zero, so we capture that and fall through to the "000" status
    # below, letting the caller record the row as failed and move on.
    if [ -n "$body" ]; then
      resp="$(
        printf '%s' "$body" | curl -sS -X "$method" "$OAG_BASE_URL$path" \
          -D "$tmp_headers" \
          -w '\n%{http_code}' \
          -H "Authorization: Bearer ${OAG_TOKEN}" \
          -H "Content-Type: application/json" \
          --data-binary @- || true
      )"
    else
      resp="$(
        curl -sS -X "$method" "$OAG_BASE_URL$path" \
          -D "$tmp_headers" \
          -w '\n%{http_code}' \
          -H "Authorization: Bearer ${OAG_TOKEN}" || true
      )"
    fi

    # Read the status from curl's -w '%{http_code}', appended as the final line of
    # stdout. It is curl's own view of the response code — reliable across HTTP
    # versions and proxies — whereas parsing the -D header dump returned an empty
    # status in some environments. Split the trailing status line back off the
    # body (append is exactly "\n<code>", so cut on the last newline). The -D dump
    # is kept only for Retry-After, which -w cannot portably surface on older curl.
    status="${resp##*$'\n'}"
    resp="${resp%$'\n'*}"
    retry_after="$(awk 'tolower($1) ~ /^retry-after:/ {print $2}' "$tmp_headers" | tr -d '\r')"
    rm -f "$tmp_headers"
    OAG_LAST_STATUS="$status"

    # A 429 is usually the transient throttle, so retrying clears it. The one 429
    # that is NOT transient is the 25-open-submission cap on POST /submissions/ —
    # retrying won't help until reviews drain. Bulk-submitter accounts are exempt
    # from that cap and are the intended path for large batches (see the doc).
    if [ "$status" = "429" ] && [ "$attempt" -lt "$OAG_MAX_ATTEMPTS" ]; then
      wait_s="${retry_after:-$OAG_MUTATION_PACE_SECONDS}"
      echo "429 rate-limited on $method $path; waiting ${wait_s}s (attempt $attempt/$OAG_MAX_ATTEMPTS)" >&2
      sleep "$wait_s"
      attempt=$((attempt + 1))
      continue
    fi

    OAG_LAST_BODY="$resp"
    return 0
  done
}

# Pause between mutating calls to stay under the burst/minute limits.
oag_pace() {
  sleep "$OAG_MUTATION_PACE_SECONDS"
}
