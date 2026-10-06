## Description:

Guides agents in querying AllTrails trail information and a signed-in user's lists and activity using fpx through a browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AllTrails users can request read-only trail searches, details, reviews, photos, weather, and account activity without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in profile, saved-list, completed-trail, and activity-feed results may contain personal data.

Mitigation: Treat account results as personal data and share only what is necessary.

Risk: Captured headers or command output may expose account activity.

Mitigation: Avoid sharing captured headers or raw command output; use the browser bridge only with an account you control.

## Reference(s):

- [AllTrails endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account-specific results require a signed-in browser tab.]

## Skill Version(s):

3.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
