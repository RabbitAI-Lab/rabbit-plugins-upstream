#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 <project-path> <owner-username> [<issue|merge_request> <iid>]" >&2
}

if [[ $# -ne 2 && $# -ne 4 ]]; then
  usage
  exit 64
fi

project_path=$1
owner_username=$2
object_kind=${3:-}
object_iid=${4:-}
object_endpoint=
other_workflows="workflow::backlog,workflow::in-progress,workflow::paused,workflow::blocked,workflow::need-human,workflow::review,workflow::stale,workflow::done"

if [[ -n "${object_kind}" ]]; then
  case "${object_kind}" in
    issue) object_collection=issues ;;
    merge_request) object_collection=merge_requests ;;
    *)
      usage
      exit 64
      ;;
  esac
  if [[ ! "${object_iid}" =~ ^[0-9]+$ ]]; then
    usage
    exit 64
  fi
fi

if ! command -v glab >/dev/null 2>&1; then
  echo "[forbidden] glab is required" >&2
  exit 77
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "[forbidden] jq is required" >&2
  exit 77
fi

encoded_project=$(jq -rn --arg value "${project_path}" '$value | @uri')
if [[ -n "${object_kind}" ]]; then
  object_endpoint="projects/${encoded_project}/${object_collection}/${object_iid}"
fi

sync_forbidden_label() {
  local state=$1

  [[ -n "${object_endpoint}" ]] || return 0
  if [[ "${state}" == "forbidden" ]]; then
    glab api -X PUT "${object_endpoint}" \
      -f add_labels=workflow::forbidden \
      -f remove_labels="${other_workflows}" >/dev/null
  else
    glab api -X PUT "${object_endpoint}" \
      -f remove_labels=workflow::forbidden >/dev/null
  fi
}

fail() {
  sync_forbidden_label forbidden || echo "[warning] unable to set workflow::forbidden" >&2
  echo "[forbidden] $*" >&2
  exit 77
}

if ! user_json=$(glab api user 2>/dev/null); then
  fail "unable to resolve the authenticated GitLab user"
fi

agent_id=$(jq -er '.id | select(type == "number")' <<<"${user_json}") || fail "GitLab user id is missing"
agent_username=$(jq -er '.username | select(type == "string" and length > 0)' <<<"${user_json}") || fail "GitLab username is missing"

if ! membership_json=$(glab api "projects/${encoded_project}/members/all/${agent_id}" 2>/dev/null); then
  fail "${agent_username} is not a project member of ${project_path}"
fi

membership_state=$(jq -er '.membership_state | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership state is missing"
access_level=$(jq -er '.access_level | select(type == "number")' <<<"${membership_json}") || fail "membership access level is missing"
created_by=$(jq -er '.created_by.username | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership creator is missing"
member_username=$(jq -er '.username | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership username is missing"

[[ "${member_username}" == "${agent_username}" ]] || fail "membership identity does not match the authenticated user"
[[ "${membership_state}" == "active" ]] || fail "membership is not active"
((access_level >= 10)) || fail "membership does not grant project access"
[[ "${created_by}" == "${owner_username}" ]] || fail "membership was created by ${created_by}, not ${owner_username}"

sync_forbidden_label allowed || fail "unable to remove workflow::forbidden"
echo "[allowed] ${agent_username} was added to ${project_path} by ${owner_username}"
