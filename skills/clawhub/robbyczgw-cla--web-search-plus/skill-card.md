## Description:

Search the web and extract URLs with routing across Serper, Brave, Tavily, Querit, Linkup, Exa, Firecrawl, You.com, SearXNG, SerpBase, and Keenable, returning ranked sources and page text with freshness filters and research support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to retrieve ranked web sources, extract page content, and gather source-only research material across configurable search providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and extraction URLs may be sent to whichever third-party provider is configured or selected.

Mitigation: Choose a provider explicitly for sensitive work, review each provider's handling terms, or use a self-hosted SearXNG instance when appropriate.

Risk: Search results, provider failure history, and provider performance samples can be cached locally.

Mitigation: Use --no-cache for a single sensitive run or WSP_DISABLE_CACHE=1 to disable caching globally.

Risk: Setup can store provider API keys locally.

Mitigation: Prefer environment variables for keys, or restrict config.json permissions after running setup.

Risk: Submitting internal or private URLs for extraction can disclose them to external extraction providers.

Mitigation: Keep the default private URL protections enabled and avoid extracting internal URLs unless the network and provider path are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/web-search-plus)
- [README.md](README.md)
- [FAQ.md](FAQ.md)
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- [config.example.json](config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [CLI text and Markdown-style results with ranked source URLs, extracted page text, and provider metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-only output; no model-written answer synthesis is produced by the skill.]

## Skill Version(s):

4.3.1 (source: frontmatter, package.json, CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
