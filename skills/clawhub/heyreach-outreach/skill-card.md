## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and outreach teams use this skill to manage HeyReach campaigns and leads, triage inbox conversations, and retrieve outreach analytics through their connected account. It can also make account and workspace changes when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requests to an external API using your superagnt API key.

Mitigation: Install only if you trust superagnt and are comfortable using your key with its service.

Risk: The connected API can expose organization and workspace administration, API-key creation, outbound messages, and destructive changes.

Mitigation: Use only the endpoints needed for the request, and get explicit confirmation before sending, deleting, overwriting, creating keys, or changing team membership.

## Reference(s):

- [HeyReach Integration Documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [superagnt API Key Setup](https://superagnt.com/r/ch-heyreach-outreach-key)
- [Connected Accounts](https://app.superagnt.com/dashboard/connections)
- [MCP Installation Instructions](https://www.superagnt.com/install)
- [MCP Server](https://mcp.superagnt.com/mcp)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Guidance, Text]

**Output Format:** [Markdown instructions with curl examples and JSON API parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can perform requested outreach, account, and workspace operations through the connected HeyReach account.]

## Skill Version(s):

2.0.17 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
