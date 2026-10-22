## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Outreach teams and developers use this skill to manage connected HeyReach campaigns, leads, conversations, sender accounts, and reporting through superagnt. Authorized administrators can also manage workspace settings and access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Organization-level access can create API keys, invite users, and change workspace membership.

Mitigation: Use a least-privileged key; avoid organization-scoped credentials unless administration is intended, and confirm sensitive administration actions explicitly.

Risk: Outbound messages, record deletion, and webhook creation can affect contacts or external systems.

Mitigation: Require explicit user confirmation before sending messages, deleting records, or creating webhooks.

Risk: A broad connected account can expose more HeyReach operations than the task requires.

Mitigation: Review the connection before installation and use only the endpoints needed for the user's request.

## Reference(s):

- [HeyReach integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [Superagnt connection setup](https://app.superagnt.com/dashboard/connections)
- [Superagnt API key setup](https://superagnt.com/r/ch-heyreach-outreach-key)
- [Superagnt MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [HeyReach Integration on ClawHub](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline curl commands and API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may be JSON; actions affect the user's connected HeyReach account.]

## Skill Version(s):

2.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
