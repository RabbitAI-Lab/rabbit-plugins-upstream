## Description:

Guides developers through accessing SignUpGenius sign-ups, groups, and RSVPs with curl using an email-and-password session instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other SignUpGenius account users can retrieve sign-ups and group data or prepare RSVP and slot actions with shell commands when an MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session credentials and tokens can grant access to the SignUpGenius account.

Mitigation: Treat passwords, JWTs, refresh tokens, session cookies, cookie jars, and copied commands as secrets; do not expose them in logs or shared files.

Risk: Public endpoints may reveal participant names and identifiers, including for sign-ups that hide names in another view.

Mitigation: Use participant lookup only with clear permission and limit collection and sharing of personal data.

Risk: RSVP, claim, release, and group-member requests can change live sign-up data.

Mitigation: Require explicit user confirmation before any write and verify that a release targets the signed-in member's own entry.

## Reference(s):

- [SignUpGenius session-mode endpoint guide](references/sug-endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve JSON account and sign-up data or submit account changes.]

## Skill Version(s):

2.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
