#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 <project-path> <owner-username>" >&2
}

fail() {
  echo "[forbidden] $*" >&2
  exit 77
}

if [[ $# -ne 2 || -z "$1" || -z "$2" ]]; then
  usage
  exit 64
fi

project_path=$1
owner_username=$2

command -v glab >/dev/null 2>&1 || fail "glab is required"
command -v jq >/dev/null 2>&1 || fail "jq is required"

if ! user_json=$(glab api user 2>/dev/null); then
  fail "unable to resolve the authenticated GitLab user"
fi

agent_id=$(jq -er '.id | select(type == "number")' <<<"${user_json}") || fail "GitLab user id is missing"
agent_username=$(jq -er '.username | select(type == "string" and length > 0)' <<<"${user_json}") || fail "GitLab username is missing"
encoded_project=$(jq -rn --arg value "${project_path}" '$value | @uri')

if ! membership_json=$(glab api "projects/${encoded_project}/members/all/${agent_id}" 2>/dev/null); then
  fail "${agent_username} is not a project member of ${project_path}"
fi

membership_state=$(jq -er '.membership_state | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership state is missing"
access_level=$(jq -er '.access_level | select(type == "number")' <<<"${membership_json}") || fail "membership access level is missing"
created_by=$(jq -er '.created_by.username | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership creator is missing"
member_username=$(jq -er '.username | select(type == "string" and length > 0)' <<<"${membership_json}") || fail "membership username is missing"

[[ "${member_username}" == "${agent_username}" ]] || fail "membership identity does not match the authenticated user"
[[ "${membership_state}" == "active" ]] || fail "membership is not active"
(( access_level >= 10 )) || fail "membership does not grant project access"
[[ "${created_by}" == "${owner_username}" ]] || fail "membership was created by ${created_by}, not ${owner_username}"

echo "[allowed] ${agent_username} was added to ${project_path} by ${owner_username}"
