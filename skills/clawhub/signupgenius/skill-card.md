## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SignUpGenius sign-ups, groups, slots, participant reports, and their own commitments, with limited write actions for adding group members, RSVP changes, and claiming or releasing slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access SignUpGenius account/session data and public participant information.

Mitigation: Install only after review, keep secret-bearing MCP configuration out of repositories, and prefer pinned reviewed package versions.

Risk: Some tools can change sign-up or group state, including RSVP, slot claim or release, and group-member changes.

Mitigation: Require explicit user confirmation before write actions and review previews before confirming slot changes.

Risk: Direct-login mode may involve reusable account credentials.

Mitigation: Avoid storing passwords in project configuration and use session or key-based modes where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with MCP tool guidance and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a signed-in SignUpGenius session, direct-login credentials, or a Pro API key depending on the requested operation.]

## Skill Version(s):

1.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
