## Description:

Read sign-up sheets, slot reports, and groups on SignUpGenius, and add members to your groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and organizers use this skill to inspect SignUpGenius profiles, groups, invitations, public slots, and owner-scoped reports. It also supports limited account changes such as adding group members, RSVPing, claiming slots, and releasing the signed-in user's own slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access SignUpGenius account sessions, credentials, cookies, or API keys.

Mitigation: Treat all cookies, passwords, and API keys as secrets, and avoid logging or sharing them.

Risk: The skill can make real account changes such as RSVPs, slot claims, slot releases, and group-member additions.

Mitigation: Require explicit user confirmation before any write action.

Risk: The server security summary reports that the skill undercounts its write actions.

Mitigation: Review the available tools before deployment and apply a confirmation policy to each operation that changes SignUpGenius state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)
- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with JSON configuration examples and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SignUpGenius session cookies, account credentials, or a Pro API key depending on the selected authentication mode.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
