## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage HeyReach campaigns, leads, lists, inbox conversations, and outreach analytics from an AI agent. It can also support workflows that send messages, change workspace records, manage webhooks, or administer organization settings when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound messages, deletions, updates, and administrative changes can affect the connected HeyReach workspace.

Mitigation: Use only the endpoints needed for the user's request and get explicit confirmation before sending messages, deleting or overwriting records, or making administrative changes.

Risk: Campaign, lead, and inbox data pass through superagnt, and webhook destinations can receive event data.

Mitigation: Connect only the HeyReach permissions needed, keep SUPERAGNT_API_KEY private, and review webhook destinations before approving them.

## Reference(s):

- [HeyReach Integration Documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [HeyReach MCP Server](https://mcp.superagnt.com/mcp)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance, Analysis]

**Output Format:** [HeyReach API response data, typically JSON, with concise text summaries or guidance when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content depends on the requested operation and the connected HeyReach account; may include campaign, lead, inbox, analytics, webhook, or workspace data.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
