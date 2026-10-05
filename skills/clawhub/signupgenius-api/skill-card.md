## Description:

Helps agents use curl to access SignUpGenius sign-ups, groups, and RSVPs without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and manage authorized SignUpGenius groups, sign-ups, and RSVPs from shell scripts without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated participant-detail examples may expose private sign-up information.

Mitigation: Use participant-detail requests only for sign-ups you are authorized to access; do not collect information from other people's sign-ups.

Risk: Exported passwords, cookies, JWTs, and refresh tokens can expose account access.

Mitigation: Treat credentials and session tokens as secrets and review the skill before installing.

## Reference(s):

- [SignUpGenius API skill on ClawHub](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [SignUpGenius session-mode endpoint examples](artifact/references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use SignUpGenius account credentials and session tokens; SSO and 2FA login are not supported.]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
