## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can manage Instantly AI campaigns, leads, sending accounts, and outreach analytics through their connected account. The skill also documents account and workspace administration for tasks that explicitly require it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some operations can send messages, delete or overwrite records, or change account and workspace settings.

Mitigation: Use only endpoints needed for the request and confirm before sending, deleting, overwriting, or making account administration changes.

Risk: Authenticated requests use the Superagnt API connection and may involve the user's Instantly account, sensitive data, or vendor-side usage and billing.

Mitigation: Use an API key intended for this service, keep it private, and only use a key and connection the user is comfortable using.

## Reference(s):

- [Superagnt documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [API key setup](https://superagnt.com/r/ch-instantly-outreach-key)
- [Connections page](https://app.superagnt.com/dashboard/connections)
- [Superagnt MCP server](https://mcp.superagnt.com/mcp)
- [MCP client setup](https://www.superagnt.com/install)
- [Clawhub listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with API endpoint tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
