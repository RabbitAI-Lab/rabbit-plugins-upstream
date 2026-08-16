#!/usr/bin/env bash
set -euo pipefail

# lg_agent_list.sh — Agent Skill Gateway discovery wrapper.
#
#   lg_agent_list.sh                    # list every skill visible to this token
#   lg_agent_list.sh describe <skillId> # show one skill's params schema + example
#
# `describe` is a thin GET /agent/skills?skillId=<id>.
#
# NOTE (2026-08-03): the list is NO LONGER filtered by the caller's granted
# scopes. Every entry carries a `granted` boolean instead — read that to know
# whether you can actually call it; ungranted entries also carry
# `presetsGrantingScope`. Pass `?granted=true` for the old filtered shape.
# Execution authorization is unchanged: /agent/skills/execute still checks
# scope on every call, so a visible skill is not necessarily a callable one.
# Every skill entry in the response carries a `params` schema array
# ({name,in,required,type,example?,aliases?}) and a curated or auto-derived
# `exampleInvocation` string for the new flat command-line form — read
# these directly from the JSON to see which keys a skill accepts before
# calling lg_agent_exec.sh.

# Default to official domain to avoid security scanner warnings
BASE_URL="${LG_AGENT_BASE_URL:-https://lg-data.cc}"
: "${LG_AGENT_TOKEN:?LG_AGENT_TOKEN is required}"

usage() {
  echo "Usage:" >&2
  echo "  $0                      # list all skills visible to this token" >&2
  echo "  $0 describe <skillId>   # show one skill's params schema + example" >&2
  exit 1
}

if [[ $# -eq 0 ]]; then
  curl -sS "${BASE_URL}/agent/skills" \
    -H "Authorization: Bearer ${LG_AGENT_TOKEN}" \
    -H "Accept: application/json"
  exit 0
fi

if [[ "$1" != "describe" ]]; then
  usage
fi
if [[ $# -lt 2 ]]; then
  usage
fi
SKILL_ID="$2"

curl -sS "${BASE_URL}/agent/skills?skillId=$(printf '%s' "$SKILL_ID" | sed -e 's/ /%20/g')" \
  -H "Authorization: Bearer ${LG_AGENT_TOKEN}" \
  -H "Accept: application/json"
