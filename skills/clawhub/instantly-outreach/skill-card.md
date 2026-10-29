## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and developers can use the skill to manage Instantly campaigns and leads, review outreach analytics, and configure connected account workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign sends and account, lead, or other data changes can affect the connected Instantly workspace.

Mitigation: Require explicit user confirmation before sending messages or making destructive changes.

Risk: The integration can access sensitive account and administrative features, including billing, API keys, and purchases.

Mitigation: Use a minimally privileged connection and perform administrative actions only when explicitly requested; confirm purchases, billing changes, and key creation.

Risk: Automations and webhooks can continue acting after setup.

Mitigation: Track active automations and webhooks and review their scope and activity.

Risk: Some curl examples may need correction before use.

Mitigation: Review and correct command quoting before running examples.

## Reference(s):

- [Instantly integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [superagnt MCP server](https://mcp.superagnt.com/mcp)
- [Connect an Instantly account](https://app.superagnt.com/dashboard/connections)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown instructions with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
