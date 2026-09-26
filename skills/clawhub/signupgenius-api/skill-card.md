## Description:

Helps agents access SignUpGenius sign-ups, groups, and RSVPs through shell-based API requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized SignUpGenius users can use this skill to retrieve signup and group information or prepare RSVP and slot changes from a shell without an MCP server. Confirm any changes before submitting them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated participant lookups may expose names and signup details from public pages.

Mitigation: Only access signup pages you are authorized to use and limit collection and sharing of participant details.

Risk: Login credentials, session tokens, cookies, and temporary files can expose account access if mishandled.

Mitigation: Treat credentials and session artifacts as secrets, avoid sharing them, and delete login artifacts after use.

## Reference(s):

- [SignUpGenius session-mode endpoint reference](artifact/references/sug-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides read requests and user-confirmed signup actions; retrieved data may contain personal information.]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
