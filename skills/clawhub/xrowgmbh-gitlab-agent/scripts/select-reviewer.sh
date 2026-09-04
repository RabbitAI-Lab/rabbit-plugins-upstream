#!/usr/bin/env bash
set -euo pipefail

apply=false
if [[ "${1:-}" == "--apply" ]]; then
  apply=true
  shift
fi

if [[ $# -ne 2 || ! "$2" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 [--apply] <project-path> <merge-request-iid>" >&2
  exit 64
fi

project_path=$1
mr_iid=$2

fail() {
  echo "[reviewer-selection] $*" >&2
  exit 78
}

for command in glab jq; do
  command -v "${command}" >/dev/null || fail "${command} is required"
done

encoded_project=$(jq -rn --arg value "${project_path}" '$value | @uri')

api_object() {
  local value
  value=$(glab api "$1" 2>/dev/null) || fail "unable to read $2"
  jq -e 'type == "object"' <<<"${value}" >/dev/null || fail "$2 is incomplete"
  printf '%s\n' "${value}"
}

api_array() {
  local value
  value=$(glab api "$1" --paginate 2>/dev/null) || fail "unable to read $2"
  jq -s -e 'if all(.[]; type == "array") then add else error("invalid") end' <<<"${value}" 2>/dev/null ||
    fail "$2 is incomplete"
}

me=$(api_object user "current user")
project=$(api_object "projects/${encoded_project}" "project")
mr_endpoint="projects/${encoded_project}/merge_requests/${mr_iid}"
mr=$(api_object "${mr_endpoint}" "merge request")
members=$(api_array "projects/${encoded_project}/members/all?per_page=100" "project memberships")
linked=$(api_array "${mr_endpoint}/closes_issues?per_page=100" "linked work items")

agent_id=$(jq -er '.id' <<<"${me}") || fail "current user is incomplete"
default_branch=$(jq -er '.default_branch' <<<"${project}") || fail "project is incomplete"
jq -e --argjson iid "${mr_iid}" --argjson agent "${agent_id}" '
  .iid == $iid and .state == "opened" and (.sha | length > 0) and
  any(.assignees[]; .id == $agent)
' <<<"${mr}" >/dev/null || fail "merge request is not open and assigned to the current user"
jq -e 'all(.[]; .id and .username and .access_level and .state and (.locked | type == "boolean"))' \
  <<<"${members}" >/dev/null || fail "project memberships are incomplete"
jq -e 'all(.[]; .iid and .author.id and .author.username)' \
  <<<"${linked}" >/dev/null || fail "linked work items are incomplete"

configured='[]'
encoded_branch=$(jq -rn --arg value "${default_branch}" '$value | @uri')
tree=$(api_array "projects/${encoded_project}/repository/tree?ref=${encoded_branch}&per_page=100" "default-branch tree")
if jq -e 'any(.[]; .path == "AGENTS.md")' <<<"${tree}" >/dev/null; then
  agents=$(glab api "projects/${encoded_project}/repository/files/AGENTS.md/raw?ref=${encoded_branch}" 2>/dev/null) ||
    fail "unable to read default-branch AGENTS.md"
  configured_lines=$(awk -F'|' '
    tolower($2) ~ /^[[:space:]]*reviewers[[:space:]]*$/ { print $3 }
  ' <<<"${agents}" | grep -oE '\[[A-Za-z0-9_.-]+\]' | tr -d '[]' || true)
  configured=$(jq -Rsc 'split("\n") | map(select(length > 0)) | reduce .[] as $v ([]; if index($v) then . else . + [$v] end)' \
    <<<"${configured_lines}")
fi

excluded=$(jq -c --argjson agent "${agent_id}" '
  [$agent, .author.id] + [.assignees[].id] | unique
' <<<"${mr}")
eligible=$(jq -c --argjson excluded "${excluded}" '
  [.[] | select(.state == "active" and .locked == false) |
   select(.access_level == 40 or .access_level == 50) |
   select(.id as $id | $excluded | index($id) | not)]
' <<<"${members}")
linked_candidates=$(jq -cn --argjson linked "${linked}" --argjson eligible "${eligible}" '
  [$linked[].author.id as $id | $eligible[] | select(.id == $id)] | unique_by(.id)
')

case $(jq 'length' <<<"${linked_candidates}") in
  1)
    rule=linked-work-item-author
    reviewer=$(jq '.[0]' <<<"${linked_candidates}")
    ;;
  0)
    configured_candidates=$(jq -cn --argjson names "${configured}" --argjson eligible "${eligible}" '
      [$names[] as $name | $eligible[] | select(.username == $name)]
    ')
    if [[ $(jq 'length' <<<"${configured_candidates}") -gt 0 ]]; then
      rule=configured-reviewer
      reviewer=$(jq '.[0]' <<<"${configured_candidates}")
    else
      reviewer=$(jq 'sort_by(.access_level, .username, .id) | .[0] // empty' <<<"${eligible}")
      [[ -n "${reviewer}" ]] || fail "no eligible reviewer"
      if [[ $(jq '.access_level' <<<"${reviewer}") == 40 ]]; then
        rule=maintainer-fallback
      else
        rule=owner-fallback
      fi
    fi
    ;;
  *) fail "linked work items have different eligible authors" ;;
esac

reviewer_id=$(jq -er '.id' <<<"${reviewer}")
result=$(jq -cn \
  --arg project "${project_path}" \
  --arg rule "${rule}" \
  --argjson mr_iid "${mr_iid}" \
  --argjson reviewer "$(jq '{id, username, access_level}' <<<"${reviewer}")" \
  --argjson linked_iids "$(jq '[.[].iid]' <<<"${linked}")" \
  '{project: $project, merge_request_iid: $mr_iid, reviewer: $reviewer,
    rule: $rule, linked_work_item_iids: $linked_iids, dry_run: true, applied: false}')

if [[ "${apply}" == true ]]; then
  fresh_member=$(api_object "projects/${encoded_project}/members/all/${reviewer_id}" "reviewer membership")
  jq -e --argjson id "${reviewer_id}" '
    .id == $id and .state == "active" and .locked == false and
    (.access_level == 40 or .access_level == 50)
  ' <<<"${fresh_member}" >/dev/null || fail "reviewer is no longer eligible"

  fresh_mr=$(api_object "${mr_endpoint}" "merge request revalidation")
  old_signature=$(jq -c '{state,sha,author:.author.id,assignees:[.assignees[].id]|sort,reviewers:[.reviewers[].id]|sort}' <<<"${mr}")
  new_signature=$(jq -c '{state,sha,author:.author.id,assignees:[.assignees[].id]|sort,reviewers:[.reviewers[].id]|sort}' <<<"${fresh_mr}")
  [[ "${old_signature}" == "${new_signature}" ]] || fail "merge request changed; reviewers were not modified"

  reviewer_ids=$(jq -c --argjson id "${reviewer_id}" '[.reviewers[].id, $id] | unique' <<<"${fresh_mr}")
  jq -cn --argjson ids "${reviewer_ids}" '{reviewer_ids: $ids}' |
    glab api -X PUT "${mr_endpoint}" --header 'Content-Type: application/json' --input - >/dev/null ||
    fail "unable to add reviewer"
  result=$(jq '.dry_run = false | .applied = true' <<<"${result}")
fi

jq . <<<"${result}"
