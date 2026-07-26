# DeepWiki via mcporter

This reference captures the practical workflow for using DeepWiki MCP tools through `mcporter`.

## Repository Visibility Preflight

Run this before any public DeepWiki or direct public MCP call. It accepts only a normalized `owner/repo` supplied by the user, queries the GitHub repository API, and prints GitHub's canonical public `full_name` only when GitHub reports `private: false`. Assign stdout back to `repo_name` and use that canonical value for every subsequent `repoName` argument. Any other result stops the public-MCP path.

```bash
repo_name="${repo_name:?set repo_name to normalized owner/repo}"
case "$repo_name" in
  *[!A-Za-z0-9_./-]*|*/*/*|/*|*/|*//*)
    printf '%s\n' '{"repositoryVisibility":"unknown","reason":"invalid-owner-repo"}' >&2
    exit 1
    ;;
esac

visibility_file="$(mktemp)"
trap 'rm -f "$visibility_file"' EXIT
visibility_http_code="$(curl -sS --location --max-time 15 --output "$visibility_file" --write-out '%{http_code}' \
  "https://api.github.com/repos/$repo_name")" || {
  printf '%s\n' '{"repositoryVisibility":"unknown","reason":"github-visibility-request-failed"}' >&2
  exit 1
}

canonical_repo_name="$(jq -r '
  if .private == false and (.full_name | type == "string")
  then .full_name | select(test("^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$"))
  else empty end
' "$visibility_file")"

if [ "$visibility_http_code" = "200" ] && [ -n "$canonical_repo_name" ]; then
  printf '%s\n' "$canonical_repo_name"
else
  printf '{"repositoryVisibility":"unknown","httpStatus":%s,"reason":"not-confirmed-public"}\n' "$visibility_http_code" >&2
  exit 1
fi
```

Do not infer that `404` means a repository is public, private, or nonexistent. A `401`, `403`, timeout, invalid JSON, missing `jq`, or absent/invalid `full_name` is also `unknown`; stop rather than trying public DeepWiki. Preserve the stderr diagnostic in the task record.

## Server Discovery

Do not assume a particular gateway, server name, URL, or authentication arrangement. On the first DeepWiki lookup in a task, inspect configured `mcporter` servers with a bounded schema request. A candidate must expose all three capabilities, with or without a gateway prefix:

- `read_wiki_structure` or `<prefix>-read_wiki_structure`
- `ask_question` or `<prefix>-ask_question`
- `read_wiki_contents` or `<prefix>-read_wiki_contents`

`DEEPWIKI_MCP_SERVER`, when set, is only a preference; it never bypasses the capability check. This command prints the selected server name to stdout and a structured diagnostic to stderr:

```bash
command -v mcporter >/dev/null 2>&1 || {
  printf '%s\n' '{"deepwikiMcp":"unavailable","reason":"mcporter-not-installed"}' >&2
  exit 1
}
command -v jq >/dev/null 2>&1 || {
  printf '%s\n' '{"deepwikiMcp":"unavailable","reason":"jq-not-installed"}' >&2
  exit 1
}

deepwiki_discovery_file="$(mktemp)"
trap 'rm -f "$deepwiki_discovery_file"' EXIT
deepwiki_discovery_exit=0

if [ -n "${DEEPWIKI_MCPORTER_CONFIG:-}" ]; then
  mcporter --config "$DEEPWIKI_MCPORTER_CONFIG" list --schema --json --timeout 7000 >"$deepwiki_discovery_file" || deepwiki_discovery_exit=$?
else
  mcporter list --schema --json --timeout 7000 >"$deepwiki_discovery_file" || deepwiki_discovery_exit=$?
fi

if ! jq empty "$deepwiki_discovery_file" 2>/dev/null; then
  printf '%s\n' '{"deepwikiMcp":"unavailable","reason":"mcporter-discovery-invalid-json"}' >&2
  exit 1
fi

deepwiki_discovery="$(jq -c --arg preferred "${DEEPWIKI_MCP_SERVER:-}" --argjson exit_code "$deepwiki_discovery_exit" '
  def supports_deepwiki:
    ([.tools[]?.name] | any(test("(^|[-_.])read_wiki_structure$"; "i"))) and
    ([.tools[]?.name] | any(test("(^|[-_.])ask_question$"; "i"))) and
    ([.tools[]?.name] | any(test("(^|[-_.])read_wiki_contents$"; "i")));
  . as $root
  | [($root.servers[]? // empty)
     | select(.status == "ok" and supports_deepwiki)
     | {name, preferred: (.name == $preferred), named: ((.name + " " + (.description // "")) | test("deepwiki"; "i"))}]
  | sort_by(if .preferred then 0 elif .named then 1 else 2 end) as $candidates
  | {deepwikiMcp: (if ($candidates | length) > 0 then "available" else "unavailable" end),
     selectedServer: ($candidates[0].name // null),
     candidateServers: ($candidates | map(.name)),
     exitCode: $exit_code,
     configuredServers: [$root.servers[]?.name],
     unavailableServers: [$root.servers[]? | select(.status != "ok") | {name, status, reason: (.issue.kind // .error // "unknown")}],
     reason: (if ($candidates | length) > 0 then null
              elif ($root.servers | length) == 0 then "no-mcporter-servers-configured"
              elif $exit_code != 0 then "mcporter-discovery-command-failed"
              else "no-healthy-deepwiki-capable-server" end)}
' "$deepwiki_discovery_file")"

deepwiki_server="$(printf '%s' "$deepwiki_discovery" | jq -r '.selectedServer // empty')"
[ -n "$deepwiki_server" ] || {
  printf '%s\n' "$deepwiki_discovery" >&2
  exit 1
}
printf '%s\n' "$deepwiki_discovery" >&2
printf '%s\n' "$deepwiki_server"
```

Preserve `candidateServers` for this task. If the selected server fails during a task, try every remaining candidate once before falling back; do not rediscover indefinitely. Set the host command timeout to 15 seconds where `mcporter` cannot enforce its own timeout.

DeepWiki official remote MCP endpoint:

- `https://mcp.deepwiki.com/mcp`

Legacy SSE endpoint:

- `https://mcp.deepwiki.com/sse`

Prefer `/mcp`; `/sse` is legacy and being deprecated.

## Default Research Flow

Start with structure:

```bash
mcporter call "$deepwiki_server.DeepWiki-read_wiki_structure" \
  --args "$(jq -nc --arg repo "$repo_name" '{repoName: $repo}')" \
  --output json
```

Use returned topics to plan follow-up questions:

```bash
mcporter call "$deepwiki_server.DeepWiki-ask_question" \
  --args "$(jq -nc --arg repo "$repo_name" --arg question "How does the Fiber work loop and scheduler fit together?" '{repoName: $repo, question: $question}')" \
  --output json
```

Use full contents only when broad wiki extraction is needed:

```bash
mcporter call "$deepwiki_server.DeepWiki-read_wiki_contents" \
  --args "$(jq -nc --arg repo "$repo_name" '{repoName: $repo}')" \
  --output json
```

## Tool Behavior

`read_wiki_structure`:

- Input: `repoName` in `owner/repo` format.
- Output: topic tree for the generated wiki.
- Best first call for unfamiliar repos.

`ask_question`:

- Input: `repoName` or up to 10 repo names, plus `question`.
- Output: context-grounded answer and usually a DeepWiki search URL.
- Best default for focused architecture or codebase questions.

`read_wiki_contents`:

- Input: `repoName`.
- Output: generated wiki pages and source-file references.
- Can be very large; avoid as the first step unless full contents are explicitly needed.

## Query Patterns

Good `ask_question` prompts:

```bash
mcporter call "$deepwiki_server.DeepWiki-ask_question" \
  --args "$(jq -nc --arg repo "$repo_name" --arg question "What are the main package boundaries and data flow?" '{repoName: $repo, question: $question}')" \
  --output json

mcporter call "$deepwiki_server.DeepWiki-ask_question" \
  --args "$(jq -nc --arg repo "$repo_name" --arg question "How does the scheduler plugin architecture work at a high level?" '{repoName: $repo, question: $question}')" \
  --output json
```

Good question traits:

- Names one repository or a small related set.
- Asks one architecture, subsystem, data-flow, or implementation question.
- Mentions the component or page topic from `read_wiki_structure` when available.

Avoid:

- Pulling full wiki contents for every task.
- Asking broad multi-topic questions when structure already shows separate pages.
- Treating generated wiki summaries as a replacement for reviewing source on high-risk changes.

## Answering Pattern

For repository explanations:

1. State the practical architectural answer.
2. Mention the repository and DeepWiki tool used.
3. Include DeepWiki links or source-file references returned by the tool.
4. If the answer may drive code changes, verify against local or upstream source before editing.
5. If DeepWiki output is stale or missing a subsystem, say so and use repository source as fallback.

## Steering DeepWiki Generation

For Devin-managed repositories, `.devin/wiki.json` can steer wiki generation.

Useful fields:

- `repo_notes[]`: context and priorities for documentation generation.
- `pages[]`: exact pages to generate.
- `pages[].title`: unique page title.
- `pages[].purpose`: what the page should document.
- `pages[].parent`: optional parent page title.
- `pages[].page_notes[]`: page-specific notes.

Limits from the official docs:

- Maximum 30 pages, or 80 for enterprise.
- Maximum 100 total notes across repo and pages.
- Maximum 10,000 characters per note.
- Page titles must be unique and non-empty.

Creating or editing `.devin/wiki.json` is a repository edit; read existing files first and follow the repo's workflow.

## Failure Matrix

| Trigger | First fix | Safe fallback |
| --- | --- | --- |
| `mcporter` missing, discovery times out, returns invalid JSON, or finds no compatible server | Preserve the structured discovery diagnostic and do not guess a server name. | For a confirmed public repository only, use the direct public MCP procedure in `api-fallback.md`; private or unverified repositories stop and require an approved Devin MCP path. |
| Selected server fails during a task | Try each remaining `candidateServers` entry once and record every failed server. | If every candidate fails, use direct public MCP only for a confirmed public repository; do not rediscover indefinitely. |
| HTTP `429` or provider rate limit | Honor a valid provider `Retry-After` value once; otherwise wait one second before one bounded retry. | After the retry fails, stop the MCP path and use repository source or report the unavailable result; do not issue concurrent or unbounded retries. |
| HTTP `401` or `403` | Stop immediately and report the server/authentication failure. | Do not send credentials to public DeepWiki. Verify the configured private MCP or Devin account path before retrying. |
| Repository not found, private, or its visibility is uncertain | Verify the exact public GitHub `owner/repo` spelling and visibility before any public MCP call. | For private repositories, require an approved Devin account and Devin MCP integration; never send the repository name, URL, source, or metadata to public DeepWiki. |
| Tool names or schema no longer match the expected three capabilities | Re-run the bounded discovery once and inspect the returned tool names. | Report schema drift and use the direct public MCP procedure only when its standard tools are available and the repository is confirmed public. |
| Wiki structure is empty, sparse, or does not cover the needed subsystem | Ask one narrower `ask_question` naming the subsystem. | State that the generated wiki is incomplete and verify against repository source before making consequential claims. |
| Full wiki contents are too large or truncated | Stop the full-content request and retain the structure result. | Use `read_wiki_structure` plus focused `ask_question` calls; do not retry the same unbounded request. |
