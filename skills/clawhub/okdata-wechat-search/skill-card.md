## Description:

Search public WeChat Search results, official accounts, Mini Programs, related queries, and WeChat Index data through the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content researchers can search public WeChat articles, videos, official accounts, and Mini Programs, explore related query suggestions, and review recent WeChat Index trends. The skill uses the paid okdata service, so users should consider query privacy and per-call costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to an external service.

Mitigation: Avoid sending sensitive query content and consider whether the query is appropriate for the named service.

Risk: API calls can incur per-call charges.

Mitigation: Estimate the number and cost of calls before use, and set a maximum price for each call.

## Reference(s):

- [okdata WeChat API documentation](https://okdata.online/zh/apis/wechat/)
- [okdata remote MCP endpoint](https://api.okdata.online/mcp)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [Structured search and index data with text or Markdown summaries as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results cover public WeChat data; API requests are paid per call.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
