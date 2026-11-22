## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to manage HeyReach LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can perform outbound actions such as sending messages, and can modify or delete records.

Mitigation: Confirm with the user before sending, deleting, or overwriting, and limit actions to the requested endpoints.

Risk: The skill uses a SUPERAGNT_API_KEY with an external API service and the user's connected HeyReach account.

Mitigation: Use the key only if the user trusts the service, keep it in the environment variable, and avoid exposing it in messages or logs.

## Reference(s):

- [HeyReach integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [HeyReach MCP server](https://mcp.superagnt.com/mcp)
- [superagnt client installation](https://www.superagnt.com/install)
- [Connect a HeyReach account](https://app.superagnt.com/dashboard/connections)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [API calls, JSON, Guidance]

**Output Format:** [HTTPS API requests and JSON responses, with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.18 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
