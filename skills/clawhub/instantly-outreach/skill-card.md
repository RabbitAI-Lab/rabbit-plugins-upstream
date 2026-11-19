## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and sales operations teams use this skill to manage Instantly campaigns, leads, sending accounts, and outreach analytics through an AI agent. It can also support account administration, so use those capabilities only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious because it reports account-credit access and administrative or purchasing capabilities beyond its outreach description.

Mitigation: Review the full skill description and decide whether these capabilities are needed; use administration, billing, API-key, or purchasing operations only when explicitly requested. Provide the Superagnt API key only if you trust the service with it.

Risk: Campaign and account operations can send messages or change or delete user data and settings.

Mitigation: Use only the endpoints needed for the user's task, and get explicit confirmation before sending messages or making destructive changes.

## Reference(s):

- [Instantly integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [MCP server installation](https://www.superagnt.com/install)
- [Instantly MCP server](https://mcp.superagnt.com/mcp)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions depend on the user's connected Instantly account and API key.]

## Skill Version(s):

2.0.17 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
