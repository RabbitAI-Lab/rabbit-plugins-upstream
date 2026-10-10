## Description:

Unified multi-provider web search and URL extraction skill with intelligent auto-routing, freshness filters, locale-aware defaults, spam and mirror filtering, adaptive routing, local caching, and privacy options across configured provider APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search the web, route queries across configured search providers, extract URL content, and gather source-grounded research results while controlling provider choice and local caching behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid provider keys and provider configuration may be stored or sent more broadly than expected.

Mitigation: Review the skill before installing with paid provider keys, prefer environment variables or a protected secrets store, and keep any config.json file owner-readable only.

Risk: Sensitive search queries and extraction URLs can be transmitted to configured third-party providers.

Mitigation: Use explicit provider selection for sensitive work, choose self-hosted SearXNG when appropriate, and avoid configuring custom provider endpoints unless they are trusted.

Risk: Local cache entries may retain sensitive queries, results, provider failures, or performance history.

Mitigation: Disable caching for sensitive queries or clear the cache after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/web-search-plus)
- [README](artifact/README.md)
- [FAQ](artifact/FAQ.md)
- [Troubleshooting](artifact/TROUBLESHOOTING.md)
- [Example configuration](artifact/config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-like search and extraction results, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider routing metadata, extraction text, citations or source links, quality diagnostics, and cache-related guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter, package.json, README, and changelog report 3.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
