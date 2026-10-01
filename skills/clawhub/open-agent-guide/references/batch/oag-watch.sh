#!/usr/bin/env bash
# Poll a set of submissions to a terminal state and render check / review / resolution
# state per submission. The detail endpoint deliberately omits inline checks and reviews
# (sub-resource envelopes), so this walks links.checks / links.reviews per row.
#
# Usage:
#   OAG_TOKEN=oag_... ./oag-watch.sh <submission-id> [<submission-id> ...]
#   OAG_TOKEN=oag_... ./oag-watch.sh --file submitted-ids.txt
#
# Polls every $OAG_WATCH_INTERVAL seconds (default 15) until every submission is
# merged or closed. Prints a status line per submission each round; on a terminal
# state it prints the two-tier resolution.{merged,closed} reason/summary.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=./oag-common.sh
. "$here/oag-common.sh"

: "${OAG_WATCH_INTERVAL:=15}"

ids=()
if [ "${1:-}" = "--file" ]; then
  file="${2:?usage: oag-watch.sh --file IDS.txt}"
  while IFS= read -r line; do
    [ -n "$line" ] && ids+=("$line")
  done <"$file"
else
  [ "$#" -ge 1 ] || { echo "usage: oag-watch.sh <id>... | --file IDS.txt" >&2; exit 1; }
  ids=("$@")
fi
oag_require_token

# Render one submission: overall status, per-check state (from links.checks), and the
# resolution reason once terminal. Returns 0 when terminal (merged/closed), 1 when
# still open, so the caller can count what remains.
render_one() {
  id="$1"
  oag_api GET "/api/v1/submissions/$id/"
  detail="$OAG_LAST_BODY"
  status="$(printf '%s' "$detail" | jq -r '.status')"
  ready="$(printf '%s' "$detail" | jq -r '.review_ready')"
  slug="$(printf '%s' "$detail" | jq -r '.payload.slug // .object_id')"
  echo "  $id  $slug  status=$status review_ready=$ready"

  case "$status" in
    merged)
      printf '%s' "$detail" | jq -r '"      merged: " + (.resolution.merged.summary // "(no summary)") + " by " + (.resolution.merged.user.username // "?")'
      return 0
      ;;
    closed)
      printf '%s' "$detail" | jq -r '"      closed: " + (.resolution.closed.reason // "(no reason)") + " by " + (.resolution.closed.user.username // "?")'
      return 0
      ;;
    *)
      checks_path="$(printf '%s' "$detail" | jq -r '.links.checks')"
      oag_api GET "$checks_path"
      checks="$OAG_LAST_BODY"
      # The checks list is cursor-paginated. The default check set is a handful of
      # rows (well under one 20-row page), so we render page 1 only and don't follow
      # .next. A drift test asserts the default set fits one page; if that ever grows
      # past the page size, follow the cursor here.
      printf '%s' "$checks" \
        | jq -r '.results[] | "      check " + .check_type + " = " + .status + (if .summary != "" then " (" + .summary + ")" else "" end)'
      return 1
      ;;
  esac
}

while :; do
  echo "== polling ${#ids[@]} submission(s) =="
  open_count=0
  for id in "${ids[@]}"; do
    render_one "$id" || open_count=$((open_count + 1))
  done

  if [ "$open_count" -eq 0 ]; then
    echo "All submissions terminal."
    break
  fi
  echo "$open_count still open; sleeping ${OAG_WATCH_INTERVAL}s"
  sleep "$OAG_WATCH_INTERVAL"
done
