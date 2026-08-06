#!/usr/bin/env bash
set -euo pipefail

if ! command -v glab >/dev/null 2>&1; then
  echo "glab is required" >&2
  exit 69
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required" >&2
  exit 69
fi

user_json=$(glab api user)
username=$(jq -er '.username | select(type == "string" and length > 0)' <<<"${user_json}")

issues=$(glab api 'issues?state=opened&scope=assigned_to_me&per_page=100' --paginate | jq -s 'add // []')
merge_requests=$(glab api 'merge_requests?state=opened&scope=assigned_to_me&per_page=100' --paginate | jq -s 'add // []')

jq -n \
  --arg username "${username}" \
  --argjson issues "${issues}" \
  --argjson merge_requests "${merge_requests}" '
  [
    ($issues[] | {
      kind: "issue",
      project_id,
      iid,
      title,
      web_url,
      labels,
      assignees: [.assignees[].username]
    }),
    ($merge_requests[] | {
      kind: "merge_request",
      project_id,
      iid,
      title,
      web_url,
      labels,
      assignees: [.assignees[].username]
    })
  ]
  | map(select(
      (.labels | index("workflow::forbidden") | not)
      and (.assignees | index($username))
    ))
  | sort_by(.web_url)
'
