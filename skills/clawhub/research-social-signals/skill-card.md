## Description:

Retrieves traceable public posts, profiles, trends, pagination state, and native metrics from X, Reddit, Xiaohongshu, Zhihu, LinkedIn, and WeChat through the SignalDig Social Data MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public social account, post, trend, metric, and pagination evidence for downstream social research. It validates parameters and preserves retrieval boundaries without producing sentiment, performance, content, marketing, or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrieval requests are sent to an external SignalDig MCP service under the user's API key.

Mitigation: Install only when this data flow is acceptable, store the API key outside project files, and use an environment variable or client secret mechanism where available.

Risk: Unavailable MCP tools or failed authentication could lead to misleading fabricated results if ignored.

Mitigation: Stop when the required SignalDig MCP capability is unavailable or unauthenticated, and report that no results were retrieved.

Risk: Public social metrics can be overinterpreted as sentiment, quality, conversion, or strategic recommendation signals.

Mitigation: Return traceable source data, native metrics, request parameters, and pagination boundaries without making automated decisions or recommendations.

Risk: Search and pagination results may be partial, ranking-dependent, or bounded by platform access limits.

Mitigation: Preserve effective query parameters, time windows, identifiers, result counts, and continuation state, and avoid claims of exhaustive or representative coverage.

## Reference(s):

- [SignalDig](https://signaldig.com/)
- [Setup Guide](references/setup-guide.md)
- [Social Retrieval Functional Contract](references/mcp-contract.md)
- [Social Tool Parameter Guide](references/parameter-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-social-signals)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured retrieval summaries and source data fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected SignalDig Social Data MCP and API key; preserves source identifiers, URLs, timestamps, native metrics, request parameters, and pagination state.]

## Skill Version(s):

1.6.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
