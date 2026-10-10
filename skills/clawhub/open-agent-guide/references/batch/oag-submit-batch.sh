#!/usr/bin/env bash
# Create a submission for every body in a batch file via POST /submissions/, pacing
# under the mutation rate limit. Prints the new submission id per row and writes all
# ids (one per line) to the file named by $2 (default: submitted-ids.txt) so you can
# hand them straight to oag-watch.sh.
#
# Usage:
#   OAG_TOKEN=oag_... ./oag-submit-batch.sh org-with-product.batch.json [ids-out.txt]
#
# Any non-201 row is reported (with its error detail) and skipped, not fatal. The one
# worth recognizing is 409 open_submission_conflict — an open submission already holds
# that slug; re-post with "force": true only to supersede a submission wedged open by a
# review-side stall (see SKILL.md).
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=./oag-common.sh
. "$here/oag-common.sh"

batch_file="${1:?usage: oag-submit-batch.sh BATCH_FILE.json [IDS_OUT.txt]}"
ids_out="${2:-submitted-ids.txt}"
oag_require_token
: >"$ids_out"

count="$(jq 'length' "$batch_file")"
echo "Submitting $count submission(s) from $batch_file to $OAG_BASE_URL"

for i in $(seq 0 $((count - 1))); do
  body="$(jq -c ".[$i]" "$batch_file")"
  label="$(printf '%s' "$body" | jq -r '.model + " " + (.payload.slug // .object_id // "?")')"

  oag_api POST /api/v1/submissions/ "$body"
  resp="$OAG_LAST_BODY"
  if [ "${OAG_LAST_STATUS:-}" = "201" ]; then
    id="$(printf '%s' "$resp" | jq -r '.id')"
    echo "$id" >>"$ids_out"
    echo "  [$i] CREATED  $label -> $id"
  else
    detail="$(printf '%s' "$resp" | jq -rc '.detail // .conflict_type // .errors // "unknown error"')"
    echo "  [$i] SKIPPED  $label -> HTTP ${OAG_LAST_STATUS:-?}: $detail"
  fi
  [ "$i" -lt "$((count - 1))" ] && oag_pace
done

echo "Wrote $(wc -l <"$ids_out" | tr -d ' ') id(s) to $ids_out"
