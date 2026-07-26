# Context7 via mcporter

This reference captures the practical workflow for using Context7 MCP tools through `mcporter`.

## Server Discovery

Do not assume a particular gateway, server name, URL, or auth arrangement. Discover a configured Context7-capable server by checking every `mcporter` server with a bounded schema lookup.

A candidate must expose both tool capabilities, allowing either unprefixed names or a gateway prefix:

- `resolve-library-id` or `<prefix>-resolve-library-id`
- `query-docs` or `<prefix>-query-docs`

`CONTEXT7_MCP_SERVER`, when set, is a preferred configured server name; it does not bypass the capability check.

## Default Research Flow

Resolve a library ID first:

```bash
mcporter call "$context7_server.resolve-library-id" \
  --args '{"libraryName":"React","query":"How to manage local component state"}' \
  --output json
```

Inspect returned candidates:

- `Context7-compatible library ID`
- `Title`
- `Description`
- `Code Snippets`
- `Source Reputation`
- `Benchmark Score`
- `Versions`

Then query docs:

```bash
mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/facebook/react","query":"How do I use useState for local component state?"}' \
  --output json
```

## Preflight and Time Budget

On the first Context7 lookup in a task, use this bounded discovery. It writes the selected server name to stdout, or exits nonzero when no compatible server is available:

```bash
command -v mcporter >/dev/null 2>&1 || {
  printf '%s\n' '{"context7Mcp":"unavailable","reason":"mcporter-not-installed"}' >&2
  exit 1
}
command -v jq >/dev/null 2>&1 || {
  printf '%s\n' '{"context7Mcp":"unavailable","reason":"jq-not-installed"}' >&2
  exit 1
}

context7_discovery_file="$(mktemp)"
trap 'rm -f "$context7_discovery_file"' EXIT
context7_discovery_exit=0

if [ -n "${CONTEXT7_MCPORTER_CONFIG:-}" ]; then
  mcporter --config "$CONTEXT7_MCPORTER_CONFIG" list --schema --json --timeout 7000 >"$context7_discovery_file" || context7_discovery_exit=$?
else
  mcporter list --schema --json --timeout 7000 >"$context7_discovery_file" || context7_discovery_exit=$?
fi

if ! jq empty "$context7_discovery_file" 2>/dev/null; then
  printf '%s\n' '{"context7Mcp":"unavailable","reason":"mcporter-discovery-invalid-json"}' >&2
  exit 1
fi

context7_discovery="$(jq -c --arg preferred "${CONTEXT7_MCP_SERVER:-}" --argjson exit_code "$context7_discovery_exit" '
    def supports_context7:
      ([.tools[]?.name] | any(test("(^|[-_.])resolve-library-id$"; "i"))) and
      ([.tools[]?.name] | any(test("(^|[-_.])query-docs$"; "i")));
    . as $root
    | [($root.servers[])
       | select(.status == "ok" and supports_context7)
       | {name,
          preferred: (.name == $preferred),
          named: ((.name + " " + (.description // "")) | test("context7"; "i")),
          exact: (([.tools[]?.name] | index("resolve-library-id")) != null)}]
    | sort_by(if .preferred then 0 elif .named then 1 elif .exact then 2 else 3 end) as $candidates
    | {context7Mcp: (if ($candidates | length) > 0 then "available" else "unavailable" end),
       selectedServer: ($candidates[0].name // null),
       candidateServers: ($candidates | map(.name)),
       exitCode: $exit_code,
       configuredServers: ([$root.servers[]?.name]),
       unavailableServers: [$root.servers[]? | select(.status != "ok") | {name, status, reason: (.issue.kind // .error // "unknown")}],
       reason: (if ($candidates | length) > 0 then null
                elif ($root.servers | length) == 0 then "no-mcporter-servers-configured"
                elif $exit_code != 0 then "mcporter-discovery-command-failed"
                else "no-healthy-context7-capable-server" end)}
  ' "$context7_discovery_file")"

context7_server="$(printf '%s' "$context7_discovery" | jq -r '.selectedServer // empty')"
[ -n "$context7_server" ] || {
  printf '%s\n' "$context7_discovery" >&2
  exit 1
}
printf '%s\n' "$context7_discovery" >&2
printf '%s\n' "$context7_server"
```

The structured lookup trace is emitted on stderr even when a server is selected. It distinguishes missing tools, no configuration, an invalid `mcporter` response, and individual server timeouts. Preserve its `candidateServers` array for this task. Set the host command timeout to 15 seconds where `mcporter` cannot enforce it. Do not issue ad hoc raw MCP calls when discovery fails; continue to REST or upstream documentation fallback instead.

If the selected server fails during a long task, try each remaining `candidateServers` entry once before declaring MCP unavailable. Report every attempted server and its failure; do not rediscover indefinitely.

Returned content usually includes:

- Short documentation explanation.
- Source URL.
- Code snippets.
- Separators between snippets.

## Direct Library ID Flow

If the user gives a Context7 ID, skip resolution:

```bash
mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/vercel/next.js","query":"How to implement redirects in proxy middleware"}' \
  --output json
```

Version-pinned examples:

```bash
mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/vercel/next.js/v15.1.8","query":"How does the App Router handle middleware authentication?"}' \
  --output json

mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/vercel/next.js@v15.1.8","query":"How does the App Router handle middleware authentication?"}' \
  --output json
```

## Query Patterns

Prefer specific, natural-language tasks:

```bash
mcporter call "$context7_server.resolve-library-id" \
  --args '{"libraryName":"Supabase","query":"email password sign up auth API"}' \
  --output json

mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/supabase/supabase","query":"How do I sign up a user with email and password in JavaScript?"}' \
  --output json
```

Good query traits:

- Names the library and feature.
- Includes runtime or framework when relevant.
- Asks one concept per call.
- Includes version when the user cares about a specific release.

Avoid:

- Vague queries like `auth`, `hooks`, or `routing`.
- Combining unrelated topics like auth, caching, deployment, and ORM usage in one call.
- Sending private code, credentials, personal data, or proprietary snippets in the query.

## Library ID Selection

When multiple candidates are returned:

1. Prefer exact library or package name match.
2. Prefer higher source reputation.
3. Prefer stronger code snippet coverage.
4. Prefer higher benchmark score.
5. Prefer versions that match the user's dependency version or lockfile.
6. If ambiguity remains, state the ambiguity and choose the most likely ID only when the task can tolerate it.

For a close or consequential choice, report the selected ID, up to two alternatives, and the deciding factor. Never silently substitute a similarly named package or remove a user-supplied version pin.

## Answering Pattern

For coding answers:

1. State the practical implementation.
2. Mention the selected Context7 library ID.
3. Include relevant source URLs from returned snippets.
4. Note if docs refer to a renamed API, unstable version, canary branch, or version-specific behavior.
5. If snippets conflict with local package versions, prefer the local lockfile and query a version-pinned Context7 ID.

Include a compact lookup trace in the answer:

- `libraryId` and version-pin status.
- Source URL or URLs returned by Context7.
- Resolution reason when more than one candidate was plausible.
- Selected MCP server and fallback route/reason, if Context7 was unavailable.

## Troubleshooting

- No useful library match: retry with official package spelling, repository owner, npm name, or URL-derived ID.
- Query is too broad: split into separate focused calls.
- `query-docs` fails because ID is invalid: rerun `resolve-library-id`.
- No compatible Context7-capable MCP server: use `references/api-fallback.md` or upstream docs with `web_fetch`.
- Private repositories or teamspace docs require a Context7 API key and suitable access.
