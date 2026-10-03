#!/usr/bin/env bash
# Dry-run every submission body in a batch file against POST /submissions/validate/
# WITHOUT creating anything. Cheap insurance before a real submit pass: it catches
# payload-shape and natural-key errors up front.
#
# Usage:
#   OAG_TOKEN=oag_... ./oag-validate-batch.sh org-with-product.batch.json
#
# The batch file is a JSON array of submission bodies (see org-with-product.batch.json).
# Exits non-zero if any body fails validation.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=./oag-common.sh
. "$here/oag-common.sh"

batch_file="${1:?usage: oag-validate-batch.sh BATCH_FILE.json}"
oag_require_token

count="$(jq 'length' "$batch_file")"
echo "Validating $count submission(s) from $batch_file against $OAG_BASE_URL"

failures=0
for i in $(seq 0 $((count - 1))); do
  body="$(jq -c ".[$i]" "$batch_file")"
  label="$(printf '%s' "$body" | jq -r '.model + " " + (.payload.slug // .object_id // "?")')"

  oag_api POST /api/v1/submissions/validate/ "$body"
  resp="$OAG_LAST_BODY"
  if [ "${OAG_LAST_STATUS:-}" = "200" ] && [ "$(printf '%s' "$resp" | jq -r '.valid')" = "true" ]; then
    echo "  [$i] OK       $label"
  else
    failures=$((failures + 1))
    # A payload-shape / natural-key failure — the whole point of the dry-run — comes
    # back as { "errors": { "<field path>": [msg, …] } } on the public API; conflicts
    # as .conflict_type; other coded errors as .detail. Render whichever is present.
    detail="$(printf '%s' "$resp" | jq -rc '.detail // .conflict_type // .errors // "unknown error"')"
    echo "  [$i] INVALID  $label -> HTTP ${OAG_LAST_STATUS:-?}: $detail"
  fi
  [ "$i" -lt "$((count - 1))" ] && oag_pace
done

if [ "$failures" -gt 0 ]; then
  echo "$failures/$count invalid. Fix the payloads before submitting." >&2
  exit 1
fi
echo "All $count valid."
