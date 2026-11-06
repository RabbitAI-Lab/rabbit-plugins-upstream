## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage HeyReach campaigns, leads, and inbox conversations, and to retrieve outreach analytics through a connected account. It also supports syncing outreach activity into CRM or reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending messages and changing campaign, lead, or account state can affect the user's outreach activity.

Mitigation: Get explicit confirmation before sending messages or making destructive changes, and use only the endpoints needed for the request.

Risk: Organization administration can create API keys, invite members, or change workspace and account settings.

Mitigation: Use administrative endpoints only when explicitly requested and confirm before creating keys or changing team membership.

Risk: A webhook created without campaign filters can include events from every campaign.

Mitigation: Specify and verify the webhook destination and intended campaign filters before creating the subscription.

Risk: The supplied shell examples contain quoting that needs correction before use.

Mitigation: Correct and review shell quoting before running any example.

## Reference(s):

- [HeyReach integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [Superagnt API keys](https://superagnt.com/r/ch-heyreach-outreach-key)
- [HeyReach connection settings](https://app.superagnt.com/dashboard/connections)
- [MCP server setup](https://www.superagnt.com/install)
- [HeyReach Integration on ClawHub](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API requests and responses, with Markdown guidance and inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
