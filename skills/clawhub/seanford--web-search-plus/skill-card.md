## Description: <br>
Web Search Plus provides multi-provider web search and URL content extraction with auto-routing, freshness and news filters, locale-aware defaults, result-quality filtering, and configurable local caching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to search the current web, collect source-grounded research results, and extract URL content through a chosen or automatically routed provider. It is suited to workflows that need configurable provider selection, freshness controls, locale handling, and cache controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and extraction URLs may be sent to third-party provider APIs. <br>
Mitigation: Use an explicit provider for sensitive work, choose a self-hosted SearXNG instance when appropriate, and review each provider's privacy and retention terms before sending sensitive queries. <br>
Risk: Search results, queries, provider failures, and provider performance history may be cached locally. <br>
Mitigation: Use per-call no-cache options, set WSP_DISABLE_CACHE=1 when caching is not acceptable, relocate the cache with WSP_CACHE_DIR, or clear cached data after use. <br>
Risk: Submitting internal or private URLs for extraction can expose those URLs to an external extraction provider. <br>
Mitigation: Avoid extracting private URLs; rely on the default private-network and metadata-endpoint blocking, and only enable private URL extraction for trusted environments. <br>
Risk: Provider API keys may be exposed if users store them in local configuration files. <br>
Mitigation: Prefer environment-only credentials for sensitive keys and avoid storing provider API keys in config.json. <br>


## Reference(s): <br>
- [Web Search Plus on ClawHub](https://clawhub.ai/seanford/skills/web-search-plus) <br>
- [README](artifact/README.md) <br>
- [FAQ](artifact/FAQ.md) <br>
- [Troubleshooting](artifact/TROUBLESHOOTING.md) <br>
- [Example Configuration](artifact/config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; search and extraction commands can produce text, Markdown, or JSON-style structured results depending on options.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on configured provider credentials or SearXNG instance; local caching is enabled by default and can be bypassed or disabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact source files report 3.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
