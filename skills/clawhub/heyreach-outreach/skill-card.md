## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and sales operations teams use the skill to manage HeyReach outreach campaigns, leads, conversations, and analytics through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup check contacts Superagnt's credits endpoint, which is outside the stated HeyReach outreach purpose, and API calls use the Superagnt key.

Mitigation: Review whether the credits lookup and external API use fit your needs; provide the key only when you are comfortable using it with this service.

Risk: Available operations can send messages, delete or change records, and administer organization settings.

Mitigation: Use only endpoints needed for the request, and get explicit confirmation before outbound or destructive actions, creating API keys, or changing team membership.

## Reference(s):

- [HeyReach Integration Documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [Connect a HeyReach account](https://app.superagnt.com/dashboard/connections)
- [MCP server setup](https://www.superagnt.com/install)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON]

**Output Format:** [curl requests with JSON payloads and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the requested operation and data in the connected HeyReach account.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
