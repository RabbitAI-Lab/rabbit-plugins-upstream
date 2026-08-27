## Description:

Retrieves traceable public social account, content, trend, source URL, timestamp, pagination, and native metric data from supported platforms through the SignalDig Social MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public social-media account and content data for downstream research and analysis. It helps validate request parameters, select the correct SignalDig Social MCP retrieval tool, and return source data without making marketing, sentiment, performance, or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a separate SignalDig API key and social-growth-signals MCP server; without them it cannot retrieve live data.

Mitigation: Verify MCP server connection and available tools before retrieval, and stop rather than fabricating results when the server or credentials are unavailable.

Risk: Retrieval calls may use paid or live API capacity.

Mitigation: Keep tool approval enabled and review requested searches, pagination, and retries before running them.

Risk: Returned platform metrics and result sets can be mistaken for exhaustive coverage or performance judgments.

Mitigation: Preserve request boundaries, native metrics, source URLs, timestamps, and pagination state, and avoid scoring, sentiment labels, strategy recommendations, or claims of exhaustive coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jerrykik/skills/research-social-signals)
- [SignalDig homepage](https://signaldig.com/)
- [Setup Guide](references/setup-guide.md)
- [Social Retrieval Functional Contract](references/mcp-contract.md)
- [Social Tool Parameter Guide](references/parameter-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown summaries with retrieved public source data, request boundaries, and setup guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected social-growth-signals MCP server and SignalDig API key; preserves native metrics, URLs, timestamps, and pagination state without scoring or recommendations.]

## Skill Version(s):

1.4.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
