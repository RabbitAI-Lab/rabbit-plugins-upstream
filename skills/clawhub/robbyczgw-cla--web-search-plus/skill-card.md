## Description: <br>
Web Search Plus provides multi-provider web search and URL extraction with auto-routing, freshness and news filters, locale defaults, result-quality filtering, and local caching controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to run current web searches, gather research-oriented results, and extract page content through configured provider APIs from an OpenClaw-style runtime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and extraction URLs are sent to configured third-party provider APIs. <br>
Mitigation: Use an explicit provider for sensitive work, prefer a self-hosted SearXNG instance when appropriate, and avoid sending sensitive queries unless the selected provider is acceptable. <br>
Risk: Extraction of private or internal URLs can disclose those URLs to an external provider if private URL access is intentionally enabled. <br>
Mitigation: Keep private URL extraction disabled by default, rely on the built-in SSRF protections, and enable private URL access only for trusted networks and reviewed workflows. <br>
Risk: Local caching can persist queries, results, provider failure history, and provider performance samples. <br>
Mitigation: Use WSP_DISABLE_CACHE=1 or --no-cache when caching is not appropriate, clear cache data when needed, and protect config.json and API keys. <br>


## Reference(s): <br>
- [Web Search Plus ClawHub Page](https://clawhub.ai/robbyczgw-cla/skills/web-search-plus) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>
- [Hermes Web Search Plus](https://github.com/robbyczgw-cla/hermes-web-search-plus) <br>
- [Web Search Plus MCP](https://github.com/robbyczgw-cla/web-search-plus-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [CLI-oriented text or Markdown with structured JSON metadata from search and extraction scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include provider routing, freshness, locale, result-filter, cache, and extraction diagnostics; extracted pages can be truncated to a configurable character limit.] <br>

## Skill Version(s): <br>
3.3.0 (source: frontmatter, package.json, CHANGELOG released 2026-07-05, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
