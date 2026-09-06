## Description:

Monitor Reddit, Hacker News, X, and Bluesky for keyword mentions of a product or website using the RedReplier API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor product or brand mentions, review AI-scored social leads, manage monitored websites and keywords, and triage mentions through RedReplier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access RedReplier account data and manage social mention leads through an API token.

Mitigation: Use a dedicated, revocable REDREPLIER_API_KEY token and revoke or rotate it when agent access is no longer needed.

Risk: Billing activation and website deletion are high-impact API actions described in the raw documentation.

Mitigation: Require explicit user confirmation before those actions; preview billing activation first and identify websites by domain before deletion.

Risk: AI relevance scores and explanations can be imperfect for lead triage.

Mitigation: Review the source content, relevance score, and relevance reason before approving or rejecting mentions.

Risk: Repeated API calls can hit RedReplier rate limits or consume AI quota for explanation generation.

Mitigation: Respect RateLimit and Retry-After responses, avoid retry loops, and use mention explanations selectively.

## Reference(s):

- [RedReplier API Reference](artifact/references/api-reference.md)
- [RedReplier Mention Filtering](artifact/references/mention-filtering.md)
- [RedReplier](https://redreplier.com)
- [Openclaw Redreplier on ClawHub](https://clawhub.ai/tarasshyn/skills/redreplier)
- [RedReplier MCP Server](https://github.com/RedReplier/redreplier-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and curl-style shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a REDREPLIER_API_KEY token; agent workflows should respect rate limits and ask for confirmation before high-impact account changes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
