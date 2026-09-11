## Description:

Research-grade Tavily web search for OpenClaw using native Node.js with zero dependencies, supporting deep web research, multi-URL extraction, estimated Tavily credit tracking, response caching, usage-log review, and 429 backoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jwestburg](https://clawhub.ai/user/jwestburg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need Tavily-backed web search, content extraction from selected public URLs, usage statistics, and cache inspection or cleanup within OpenClaw workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected search queries or extract URLs are sent to Tavily for external processing.

Mitigation: Classify privacy sensitivity before search or extract, and do not send sensitive material unless external Tavily processing is approved.

Risk: Usage logs and cache entries may store non-sensitive research context locally.

Mitigation: Use --no-log --no-cache for sensitive but approved external research and separate OS/OpenClaw profiles when Tavily account isolation matters.

Risk: Cached responses may become stale for freshness-critical research.

Mitigation: Use --no-cache or an appropriate --ttl value when fresh results are required.

Risk: The cache clear command deletes local cached response files.

Mitigation: Run cache clear only after explicit approval; the artifact documents deletion of expected hash-named cache JSON files under the skill-specific cache directory.

## Reference(s):

- [Tavily Search Pro Contract](references/tavily-pro-contract.md)
- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/tavily-search-pro-native-node)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown-oriented agent guidance and CLI output, with optional JSON for search, extract, stats, and cache information.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TAVILY_API_KEY for outbound search and extract calls; cache and usage logging can be disabled with flags when appropriate.]

## Skill Version(s):

1.0.36 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
