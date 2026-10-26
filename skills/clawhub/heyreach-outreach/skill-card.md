## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales operations teams and developers use this skill to manage HeyReach LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics through a connected HeyReach workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An over-scoped or exposed API key could allow access to outreach data and account actions.

Mitigation: Use narrowly scoped credentials and protect the key.

Risk: Campaign, inbox, and account operations can send outreach or make consequential changes, including destructive or administrative actions.

Mitigation: Require explicit user confirmation before outbound, destructive, or sensitive administrative actions.

Risk: Webhook subscriptions can send account events to configured destinations for a configured duration.

Mitigation: Review webhook destinations and duration before creating or changing subscriptions.

## Reference(s):

- [HeyReach Integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [MCP install guide](https://www.superagnt.com/install)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with curl commands and JSON API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected HeyReach account and SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.8 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
