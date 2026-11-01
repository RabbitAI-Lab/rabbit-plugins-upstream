# Changelog

## 1.1.4

- Shorten lookup/setup guidance; remove arbitrary retrieval quotas and retain live schema discovery, source attribution and Gateway ownership constraints.

## 1.1.3

- Condense instructions and references; discover tools before use and reuse existing setup authorization.
- Correct current OpenClaw Gateway ownership requirements; retain standalone CLI access during operation.
- Replace a hard two-page ceiling with evidence-driven retrieval. Verify CLI discovery, search, fetch and code search.

## 1.1.2

- Licensed under MIT-0 (MIT No Attribution), declared in the SKILL.md frontmatter and a LICENSE file. No code changes.

## 1.1.1

- Sharper description and README, plus links to the author's other skills and site. No code changes.

## 1.1.0 (unreleased)

- Native OpenClaw MCP (`openclaw mcp add ... --transport streamable-http`) is now the preferred path, with `@microsoft/learn-cli` (pinned to 1.0.0) and mcporter as fallbacks.
- Fixed the mcporter setup command; the old `--name/--url/--type` form registered a server named `--name`. Fixed the config path and shape.
- Removed the non-existent `locale` and `product` tool parameters.
- Added a usage workflow (search first, at most two fetches, cite URLs) and safety rules: no secrets in queries, fetched content is data, no retry loops on rate limits.
- Narrowed the description and removed prompt-trigger phrases flagged by the ClawHub security audit.

## 1.0.0

- Initial release.
