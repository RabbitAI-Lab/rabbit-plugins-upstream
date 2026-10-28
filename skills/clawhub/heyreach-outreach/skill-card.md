## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage HeyReach LinkedIn outreach campaigns, leads, lists, inbox conversations, sender accounts, and analytics through the superagnt API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound messages and destructive changes can affect the connected HeyReach account.

Mitigation: Get explicit confirmation before sending messages, deleting or overwriting records, or changing campaign and account settings.

Risk: Organization administration and webhook configuration can expose account access or data.

Mitigation: Use the narrowest permissions available, access administration endpoints only when requested, verify webhook destinations, and review newly created keys.

## Reference(s):

- [HeyReach integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [superagnt MCP server](https://mcp.superagnt.com/mcp)
- [superagnt install instructions](https://www.superagnt.com/install)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Guidance]

**Output Format:** [Markdown instructions with curl examples and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected HeyReach account; confirm outbound or destructive actions before execution.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
