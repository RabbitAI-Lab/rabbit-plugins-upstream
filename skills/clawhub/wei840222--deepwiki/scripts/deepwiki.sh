#!/usr/bin/env bash
# Source this file from Bash. No network requests run on load.

_dw_err() { printf 'deepwiki: %s\n' "$*" >&2; }

_dw_repo_id() {
  [[ "$1" =~ ^[A-Za-z0-9-]+/[A-Za-z0-9_.-]+$ && "$1" != */. && "$1" != */.. ]]
}

# For an unknown, intended-public repo only. Never pass a known-private name.
dw_public_repo() {
  local raw="$1" data canonical
  _dw_repo_id "$raw" || { _dw_err 'invalid owner/repo'; return 1; }
  data=$(curl -q -fsSL --proto '=https' --proto-redir '=https' --max-time 12 \
    "https://api.github.com/repos/$raw") || { _dw_err 'GitHub did not confirm public visibility'; return 1; }
  if ! canonical=$(jq -er 'select(.private == false) | .full_name | strings' <<<"$data") || ! _dw_repo_id "$canonical"; then
    _dw_err 'not confirmed public'; return 1
  fi
  printf '%s\n' "$canonical"
}

_dw_mc() {
  if [[ -n "${DEEPWIKI_MCPORTER_CONFIG:-}" ]]; then
    mcporter --config "$DEEPWIKI_MCPORTER_CONFIG" "$@"
  else
    mcporter "$@"
  fi
}

_dw_route() {
  local kind="$1" target="$2" schema
  if [[ "$kind" == public ]]; then
    schema=$(mcporter list "$target" --schema --json --no-oauth --timeout 8000 --exit-code) || return 1
  else
    schema=$(_dw_mc list "$target" --schema --json --no-oauth --timeout 8000 --exit-code) || return 1
  fi
  jq -ec --arg target "$target" --arg kind "$kind" '
    select(.status == "ok") | .tools as $t |
    def find($n): first($t[] | select(.name|ascii_downcase == $n));
    first(["deepwiki-", ""][] as $p |
    find($p+"read_wiki_structure") as $s |
    find($p+"read_wiki_contents") as $c |
    (find($p+"ask_wiki_question") // find($p+"ask_question")) as $q |
    {kind:$kind, target:$target, tools:{structure:$s.name, ask:$q.name, contents:$c.name},
     multi: ([$q.inputSchema.properties.repoName | ., .anyOf[]? | .type] | flatten | index("array") != null)})' \
    <<<"$schema"
}

# Pass trusted aliases explicitly if the config also contains unrelated servers.
# With no arguments, check up to five configured aliases, preferred first.
dw_discover() {
  local candidates server route
  if (( $# )); then
    candidates=$(printf '%s\n' "$@")
  else
    candidates=$(_dw_mc config list --json | jq -r --arg preferred "${DEEPWIKI_MCP_SERVER:-}" '
      [.servers[]?.name | strings] | unique |
      sort_by(if . == $preferred then 0 elif test("deepwiki";"i") then 1 else 2 end) | .[:5][]') || return 1
  fi
  while IFS= read -r server; do
    [[ -n "$server" ]] || continue
    if route=$(_dw_route configured "$server"); then printf '%s\n' "$route"; return 0; fi
    _dw_err "$server: schema unavailable or missing the DeepWiki tool family"
  done <<<"$candidates"
  _dw_err 'no compatible configured server'; return 1
}

# Ad hoc, public only; no config is written. Recheck visibility before tool calls.
dw_public_route() { _dw_route public 'https://mcp.deepwiki.com/mcp'; }

_dw_text() {
  jq -er '
    if type == "string" then .
    elif has("error") or .isError == true or .structuredContent.isError? == true then
      error((.error.message? // .content[0].text? // "MCP reported an error") | tostring)
    elif (.structuredContent.result? | type) == "string" then .structuredContent.result
    elif (.result? | type) == "string" then .result
    elif (.content? | type) == "array" then
      [.content[] | select(.type == "text") | .text | strings] | join("\n")
    else error("unrecognized MCP result") end |
    select(type == "string" and test("\\S"))'
}

_dw_call() {
  local route="$1" op="$2" payload="$3" limit="$4" kind target tool data
  kind=$(jq -er '.kind' <<<"$route") && target=$(jq -er '.target' <<<"$route") &&
    tool=$(jq -er --arg op "$op" '.tools[$op] | strings | select(length>0)' <<<"$route") || return 1
  if [[ "$kind" == public && "$target" == 'https://mcp.deepwiki.com/mcp' ]]; then
    data=$(mcporter call "$target.$tool" --args "$payload" --output json --no-oauth --timeout "$limit") || return 1
  elif [[ "$kind" == configured ]]; then
    data=$(_dw_mc call "$target.$tool" --args "$payload" --output json --no-oauth --timeout "$limit") || return 1
  else
    _dw_err 'invalid route'; return 1
  fi
  _dw_text <<<"$data"
}

dw_structure() {
  local route="$1" repo
  repo=$(dw_public_repo "$2") || return 1
  _dw_call "$route" structure "$(jq -nc --arg r "$repo" '{repoName:$r}')" 25000
}

dw_ask() {
  local route="$1" question="$2" raw repo repos='[]' payload
  shift 2
  if (( $# < 1 || $# > 10 )) || [[ ! "$question" =~ [^[:space:]] ]]; then
    _dw_err 'give a focused question and 1 to 10 public owner/repo names'; return 1
  fi
  if (( $# > 1 )) && ! jq -e '.multi == true' <<<"$route" >/dev/null; then
    _dw_err 'this live schema does not support multiple repositories'; return 1
  fi
  for raw in "$@"; do
    repo=$(dw_public_repo "$raw") || return 1
    repos=$(jq -ec --arg r "$repo" 'if index($r) == null then . + [$r] else . end' <<<"$repos") || return 1
  done
  payload=$(jq -nc --argjson r "$repos" --arg q "$question" \
    '{repoName:(if ($r|length)==1 then $r[0] else $r end),question:$q}') || return 1
  _dw_call "$route" ask "$payload" 65000
}

dw_contents() {
  local route="$1" repo
  [[ "${3:-}" == --allow-full ]] || { _dw_err 'full wiki requires explicit scope and --allow-full'; return 1; }
  repo=$(dw_public_repo "$2") || return 1
  _dw_call "$route" contents "$(jq -nc --arg r "$repo" '{repoName:$r}')" 65000
}
