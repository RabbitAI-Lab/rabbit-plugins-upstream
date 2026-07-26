# Context7 API Fallback

Use this reference only when the preferred `mcporter` MCP workflow is unavailable, when testing direct Context7 integration, or when the task specifically asks for REST API calls.

## Authentication

All Context7 API requests require an API key in the `Authorization` header.

For this skill's fallback workflow, treat an unavailable `CONTEXT7_API_KEY` as a stop condition for REST calls and fetch upstream public documentation instead. The official API guide also mentions lower unauthenticated rate limits, but its authentication requirement and command examples are keyed; do not rely on anonymous access.

```bash
export CONTEXT7_API_KEY="YOUR_API_KEY"
```

Header:

```bash
Authorization: Bearer $CONTEXT7_API_KEY
```

Preflight before any REST call:

```bash
if [ -z "${CONTEXT7_API_KEY:-}" ]; then
  echo "Context7 REST fallback is unavailable; fetch upstream official documentation instead."
fi
```

API keys can be created from:

- `https://context7.com/dashboard`

## Search Library

Use this to find libraries by name before retrieving context.

```bash
curl "https://context7.com/api/v2/libs/search?libraryName=react&query=I%20need%20to%20manage%20state" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"
```

Expected use:

- Pick `results[0].id` or the best matching result.
- Prefer exact name, source reputation, code snippets, benchmark score, and version match.

MCP equivalent (after selecting `$context7_server` through `mcporter-workflow.md`):

```bash
mcporter call "$context7_server.resolve-library-id" \
  --args '{"libraryName":"React","query":"I need to manage state"}' \
  --output json
```

## Get Documentation Context

Use this to retrieve LLM-reranked documentation snippets for a library.

```bash
curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js&query=How%20to%20implement%20authentication%20with%20middleware&type=json" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"
```

Non-GitHub sources use the same endpoint:

```bash
curl "https://context7.com/api/v2/context?libraryId=/websites/uploadcare_com&query=image%20transformations&type=json" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"
```

Version-pinned examples:

```bash
curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js/v15.1.8&query=app%20router&type=json" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"

curl "https://context7.com/api/v2/context?libraryId=/vercel/next.js@v15.1.8&query=app%20router&type=json" \
  -H "Authorization: Bearer $CONTEXT7_API_KEY"
```

MCP equivalent (after selecting `$context7_server` through `mcporter-workflow.md`):

```bash
mcporter call "$context7_server.query-docs" \
  --args '{"libraryId":"/vercel/next.js","query":"How to implement authentication with middleware"}' \
  --output json
```

## Library ID Format

A library ID is the URL path on `context7.com`.

Common shapes:

- GitHub repository: `/vercel/next.js`
- GitLab, Bitbucket, or generic Git repo: `/<owner>/<repo>`
- Website: `/websites/uploadcare_com`
- llms.txt source: `/llmstxt/<source>`
- npm or package source: `/packages/<name>` or `/npm/<name>`
- Uploaded docs: `/docs/<name>`

Version pinning:

- `/owner/repo/<version>`
- `/owner/repo@<version>`

## Rate Limits

- With an API key: limits depend on plan.
- Do not attempt anonymous API fallback from this skill; use upstream public documentation when no key is available.
- `429` responses include `Retry-After`, `RateLimit-Limit`, `RateLimit-Remaining`, and `RateLimit-Reset`.

## Retry Algorithm

Retry only `429`, `500`, `503`, and `504`, with **at most three total requests** for one lookup:

1. After the first failure, wait for `Retry-After` when it is an integer from 1 to 30 seconds; otherwise wait 1 second.
2. After the second failure, use the same valid `Retry-After`; otherwise wait 2 seconds.
3. After the third failure, stop. State the final status and use upstream official documentation.

Never retry `400`, `401`, `403`, `404`, `409`, or `422` without a material change to the request. A `202` means the library is still being finalized; report that state instead of treating it as usable documentation.

## Error Handling

Common status codes:

- `202`: library accepted but not finalized; wait and retry later.
- `301`: library moved; use `redirectUrl`.
- `400`: invalid parameters.
- `401`: invalid API key; Context7 keys start with `ctx7sk`.
- `403`: access denied or plan/library permission issue.
- `404`: library does not exist.
- `409`: resource already exists.
- `422`: library too large or no code.
- `429`: rate limit exceeded.
- `500`, `503`, `504`: retry later with backoff.

Errors return JSON with `error` and `message`; redirects also include `redirectUrl`.

## State-Changing API Boundary

The Context7 API also includes endpoints for refresh, adding libraries, policies, private sources, and uploads. These mutate external Context7 state and require explicit user confirmation before use.

Normal documentation lookup should stay read-only:

- Search libraries.
- Get documentation context.
- Report source-backed snippets.

When REST fallback is used, report the `libraryId`, version-pin status, source URL or URLs from the response, and the reason the MCP path was unavailable.

## Official References

- Overview: `https://context7.com/docs/overview`
- API guide: `https://context7.com/docs/api-guide`
- GitHub repository: `https://github.com/upstash/context7`
