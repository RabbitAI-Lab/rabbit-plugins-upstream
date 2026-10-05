## Description:

Helps agents read SignUpGenius sign-ups, slots, groups, and reports, and manage group members, RSVPs, and slot registrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SignUpGenius users and organizers use this skill to check sign-up availability and participants, review their groups and events, and make sign-up or group changes with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to account credentials or browser-session cookies can expose a SignUpGenius account.

Mitigation: Prefer project-scoped configuration and avoid plaintext password mode when possible; grant account access only if comfortable with it.

Risk: Group, RSVP, claim, and release actions can change sign-ups; the skill's write-action overview is incomplete.

Mitigation: Review the requested change and require user approval before completing a write action.

Risk: Public-sheet listings can reveal participant names.

Mitigation: Treat participant information as sensitive and share it only where appropriate.

Risk: Setup relies on an external npm package and, in browser-session mode, an extension.

Mitigation: Review the package and extension before installing or granting access.

## Reference(s):

- [ClawHub signupgenius release](https://clawhub.ai/chrischall/skills/signupgenius)
- [signupgenius-mcp package](https://www.npmjs.com/package/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration, Shell commands]

**Output Format:** [Markdown with JSON configuration examples and tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include participant details; some tools change sign-ups after confirmation.]

## Skill Version(s):

2.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
