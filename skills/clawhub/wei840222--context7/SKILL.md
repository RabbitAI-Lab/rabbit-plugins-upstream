---
name: context7
description: "Retrieve current, source-backed documentation for libraries, frameworks, SDKs, APIs, developer tools, open-source projects, and GitHub projects. Use for version-specific usage, setup, migrations, troubleshooting, architecture or feature understanding, and code examples when up-to-date official documentation matters."
metadata:
  openclaw:
    emoji: "📚"
    requires:
      bins:
        - mcporter
        - jq
        - curl
  related-skills:
    mcporter: to discover and call a Context7-capable MCP server through `mcporter`.
    deepwiki: for source-backed architecture and implementation research on a specific public GitHub repository when general documentation is insufficient.
---

# Context7 Skill

Use this skill when the task needs current library or framework documentation, version-specific API usage, setup guidance, code examples, or troubleshooting for a programming package.

## Core Rule

Use the `mcporter` skill to discover a configured Context7-capable MCP server, then call it by the selected server name. Do not require a particular gateway, server name, URL, credential, or native Context7 wrapper syntax.

## Tool Choice

1. Use `Context7-resolve-library-id` first when the user names a package, framework, product, or library without an exact Context7 ID.
2. Use `Context7-query-docs` when you have a Context7-compatible `libraryId`.
3. Skip resolution only when the user already provides a valid ID like `/vercel/next.js`, `/vercel/next.js/v15.1.8`, or `/vercel/next.js@v15.1.8`.
4. Keep each docs query scoped to one concept. Split broad requests into separate calls.

## Preflight and Library Selection

1. On the first Context7 lookup in a task, first verify that `mcporter` is installed, then run the bounded capability discovery in `references/mcporter-workflow.md`. Select a healthy configured server only when it exposes both library-resolution and docs-query tools.
2. Select an exact library-name match before comparing documentation coverage, source reputation, benchmark score, and version fit.
3. When two candidates are materially ambiguous, name the top candidates and the selection reason in the answer. Do not silently choose a different package with a similar name.
4. When the user supplies a version-pinned ID, preserve that pin. If it is not indexed, say so before using an unpinned candidate.

## Quick Commands

```bash
mcporter list --schema --json --timeout 7000

mcporter call <context7-server>.resolve-library-id \
  --args '{"libraryName":"Next.js","query":"How to implement middleware authentication"}' \
  --output json

mcporter call <context7-server>.query-docs \
  --args '{"libraryId":"/vercel/next.js","query":"How to implement middleware authentication with redirects"}' \
  --output json
```

## Workflow

1. Identify the library and the exact task.
2. Resolve the library ID unless an ID was already supplied.
3. Pick the best ID using name match, documentation coverage, source reputation, benchmark score, and version fit.
4. Query docs with a focused natural-language question.
5. Answer from returned snippets and include their source URLs. Call out version-sensitive behavior explicitly.

## Failure and Fallback

1. Preserve the discovery lookup trace for the task. If discovery finds no healthy Context7-capable server, report its machine-readable reason and state that the MCP lookup is unavailable. If the selected server call fails, try each remaining `candidateServers` entry once, then report every attempted server and failure before using the next fallback. Do not imply that Context7 returned documentation.
2. If a supplied `libraryId` is rejected, rerun `Context7-resolve-library-id` with the library name. Do not silently replace a user-supplied version pin; state when the exact version is not indexed.
3. Use the direct REST fallback only when `CONTEXT7_API_KEY` is available. Otherwise, retrieve the relevant upstream official documentation with the runtime's web-fetch capability and cite the fetched URL.
4. On `429`, `500`, `503`, or `504` from the REST API, follow the backoff guidance in `references/api-fallback.md`. On `401`, `403`, or `404`, explain the failed condition and do not retry blindly.

## Response Contract

For every successful lookup, state the selected `libraryId`, selected MCP server, whether it was version-pinned, and the returned source URL or URLs. When resolution was ambiguous, include the deciding factor. When a fallback was used, state `MCP unavailable`, `REST fallback`, or `upstream official docs` and why.

## Safety and Decision Checkpoint

- Do not send private code, credentials, or proprietary snippets in a Context7 query.
- Do not use native Context7 wrapper syntax or present a memory-only answer as retrieved documentation.
- Do not combine unrelated concepts in one query.
- 🔴 **CHECKPOINT:** Before querying private or teamspace documentation, or sending any user-provided code excerpt, obtain the user's confirmation.
- 🔴 **CHECKPOINT:** Before producing an execution plan for a production authentication/security change, migration, or potentially destructive operation, verify the exact version against an official source URL and obtain the user's confirmation. If no official source is available, label the conclusion `unverified` rather than presenting it as settled.

## Coverage and Limits

- Context7 retrieves current documentation and code examples for libraries, websites, package docs, llms.txt sources, uploaded docs, and other indexed sources.
- Library IDs usually use `/owner/repo`, `/<source>/<id>`, `/packages/<name>`, `/npm/<name>`, `/websites/<domain>`, `/llmstxt/<source>`, or `/docs/<name>`.
- Version pinning supports `/owner/repo/<version>` and `/owner/repo@<version>`.
- Context7 data is community-contributed; verify important behavior against returned source URLs or upstream docs when risk is high.
- API keys unlock higher rate limits and private/teamspace features, but a configured Context7-capable MCP server should remain the default path.

## Detailed References

Use `references/mcporter-workflow.md` for command patterns, field shapes, query design, and source-backed answer patterns.

Use `references/api-fallback.md` only when the MCP path through `mcporter` is unavailable, when validating a direct Context7 API integration, or when the task specifically asks for REST API calls.

## Official Documents

These are the official documents this skill was built from:

- `https://context7.com/docs/overview`
- `https://context7.com/docs/api-guide`
- `https://github.com/upstash/context7`
