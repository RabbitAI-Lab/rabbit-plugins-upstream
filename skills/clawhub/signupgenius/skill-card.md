## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect SignUpGenius sign-ups, groups, available slots, and participant information, and to perform limited account actions such as adding group members, RSVPing, claiming slots, or releasing slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access SignUpGenius session cookies, direct-login credentials, or a Pro API key.

Mitigation: Install only when you are comfortable giving the agent access to your SignUpGenius account context and credentials.

Risk: The skill can perform write actions such as adding group members, RSVPing, claiming slots, and releasing slots.

Mitigation: Require explicit user confirmation before RSVP, claim, release, or group-member changes.

Risk: The skill can retrieve participant names from public sign-up sheets.

Mitigation: Review privacy expectations before using participant-listing tools or sharing their output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SignUpGenius session cookies, direct-login credentials, or a Pro API key depending on the requested operation.]

## Skill Version(s):

1.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
