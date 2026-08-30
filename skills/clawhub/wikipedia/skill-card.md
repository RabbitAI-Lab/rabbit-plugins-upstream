## Description:

Access Wikipedia via MCP to search articles, retrieve summaries and extracts, fetch random facts, featured articles, historical events, categories, links, pageviews, and current events across ten supported languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this MCP skill to give agents read-only Wikipedia lookup capabilities for research, content hooks, taxonomy discovery, popularity checks, and current or historical context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia queries and requested article titles are sent to Wikimedia services.

Mitigation: Install only where this public API network use is acceptable, and avoid sending sensitive queries through the skill.

Risk: The dependency range allows any requests version greater than or equal to 2.28.0.

Mitigation: Install in an environment that resolves a current patched requests version, or use a lockfile or tighter dependency range.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)
- [Wikimedia Pageviews API endpoint](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and plain-text responses returned from MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include source article links, thumbnails, daily pageview counts, and language-specific Wikipedia results.]

## Skill Version(s):

1.1.7 (source: server release metadata; artifact frontmatter and server report 1.1.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
