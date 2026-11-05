## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and developers can use the skill to manage Instantly campaigns, leads, sending accounts, and outreach analytics through an account connected by the user. Workspace administration and purchases should be limited to requests that explicitly call for them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can send outreach and modify or delete records; the documented API also includes workspace administration and purchasing actions.

Mitigation: Use limited account permissions, stay within the user's request, and get explicit confirmation before sending, deleting, changing sensitive settings, creating keys, or making purchases.

Risk: Webhooks and ongoing automation can continue to trigger account activity.

Mitigation: Review webhook destinations and active automation before enabling them.

## Reference(s):

- [Instantly AI integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with curl examples and JSON API parameter schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the user's SUPERAGNT_API_KEY and connected Instantly account; sensitive actions require explicit confirmation.]

## Skill Version(s):

2.0.13 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
