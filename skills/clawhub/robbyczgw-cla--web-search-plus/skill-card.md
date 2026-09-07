## Description:

Web Search Plus provides source-only multi-provider web search and URL extraction with auto-routing across configured providers, freshness and news filters, locale-aware defaults, quality filtering, and local result caching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to retrieve current web sources, run multi-provider research searches, and extract page content for grounding OpenClaw-style workflows. It is useful when an agent needs ranked URLs or extracted text rather than model-written answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and extraction URLs may be sent to the selected third-party provider.

Mitigation: Choose providers explicitly for sensitive work, use self-hosted SearXNG when appropriate, and avoid submitting internal or private URLs for extraction.

Risk: The setup flow can save API keys locally even though the main skill text says keys are not persisted.

Mitigation: Prefer environment variables for provider credentials, or protect config.json carefully when using the setup wizard.

Risk: Cached queries, results, provider failures, and performance samples can expose sensitive search activity on disk.

Mitigation: Disable caching with WSP_DISABLE_CACHE=1 or --no-cache for sensitive work, and clear existing cache files when needed.

## Reference(s):

- [Web Search Plus ClawHub listing](https://clawhub.ai/robbyczgw-cla/skills/web-search-plus)
- [hermes-web-search-plus](https://github.com/robbyczgw-cla/hermes-web-search-plus)
- [web-search-plus-mcp](https://github.com/robbyczgw-cla/web-search-plus-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with shell commands; CLI output may be text, JSON, or markdown depending on mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-only output: ranked URLs and extracted page text; no model-written answers.]

## Skill Version(s):

4.0.0 (source: frontmatter, package.json, CHANGELOG, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
