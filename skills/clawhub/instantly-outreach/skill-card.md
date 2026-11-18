## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to manage Instantly campaigns, leads, sending accounts, and outreach analytics through a connected account. It also documents account and workspace administration capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the integration sends account and contact information through superagnt to the connected Instantly service.

Mitigation: Use the integration only with a service and account you trust, and review what information the requested API calls will send.

Risk: Some documented operations can send messages, delete or modify records, or change account and workspace settings.

Mitigation: Limit calls to the user's request and get explicit confirmation before outbound or destructive actions.

## Reference(s):

- [Instantly integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [Instantly API key setup](https://superagnt.com/r/ch-instantly-outreach-key)
- [superagnt connections page](https://app.superagnt.com/dashboard/connections)
- [MCP server](https://mcp.superagnt.com/mcp)
- [MCP client installation instructions](https://www.superagnt.com/install)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with curl examples; API responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided SUPERAGNT_API_KEY and a connected Instantly account; API calls may update account data or send messages.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
