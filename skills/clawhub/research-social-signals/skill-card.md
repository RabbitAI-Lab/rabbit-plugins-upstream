## Description:

Retrieves traceable public social media account and content data from X, Reddit, Xiaohongshu, Zhihu, LinkedIn, and WeChat Official Accounts through the SignalDig Social MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public social posts, account profiles, source URLs, timestamps, pagination state, and native metrics for downstream research or decision support. It preserves retrieval boundaries and avoids scoring, sentiment, content strategy, or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill cannot retrieve live results unless the SignalDig MCP server is connected and authenticated.

Mitigation: Verify the social-growth-signals tools are visible before retrieval; stop rather than generating source data when the tools are unavailable.

Risk: Requests send public social search terms, profile URLs, account identifiers, and API-key authorization to SignalDig's MCP service.

Mitigation: Configure the API key through client secrets or environment variables, avoid placing it in project files or chats, and rely on tool approval prompts for each retrieval.

Risk: Social-platform results are bounded by platform access, query filters, ranking, pagination, and current availability, so they may be partial or non-representative.

Mitigation: Return exact request parameters, source URLs, timestamps, native metrics, pagination state, and retrieval errors; avoid claims of exhaustive coverage.

Risk: Downstream users may mistake retrieved metrics for sentiment, quality, reach, or business recommendations.

Mitigation: Keep platform-native metrics distinct, treat missing metrics as unknown, and avoid scoring, sentiment labels, strategy, or account-performance judgments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-social-signals)
- [SignalDig Homepage](https://signaldig.com/)
- [SignalDig Social MCP Endpoint](https://mcp.signaldig.com/data/social/mcp)
- [Setup Guide](references/setup-guide.md)
- [Social Tool Parameter Guide](references/parameter-guide.md)
- [Social Retrieval Functional Contract](references/mcp-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or structured text with source data, request boundaries, pagination state, native metrics, and safe retrieval errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected social-growth-signals MCP server and SignalDig API key; live results are bounded by platform APIs, query and filter choices, pagination, and returned public data.]

## Skill Version(s):

1.6.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
