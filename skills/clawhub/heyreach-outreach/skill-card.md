## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and AI workflow builders use this skill to manage HeyReach outreach campaigns, leads, inbox conversations, webhooks, organization settings, and analytics through Superagnt-backed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes organization administration, API-key creation, webhook changes, workspace changes, and message sending beyond ordinary outreach tasks.

Mitigation: Install only when the user trusts Superagnt with the HeyReach workspace, and require explicit confirmation before admin, destructive, or outbound actions.

Risk: Calls operate through the user's connected HeyReach credentials, so account permissions, vendor-side rate limits, billing, and workspace scope apply.

Mitigation: Limit each action to the user's stated task, confirm the target workspace and account before changes, and review API responses for connection or permission errors.

## Reference(s):

- [Superagnt HeyReach Documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [ClawHub Skill Listing](https://clawhub.ai/superagnt/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with inline bash commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API usage; MCP-capable clients may use the documented MCP server instead.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
