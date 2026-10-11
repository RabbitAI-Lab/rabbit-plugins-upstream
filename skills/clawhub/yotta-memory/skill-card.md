## Description:

Provides file-based, access-controlled memory for AI agents to retain and retrieve context across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to restore context at the start of work, retain important facts and commitments, and search or review memory across sessions while separating shared from private records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored memory may contain sensitive personal or project information.

Mitigation: Review what is retained and keep private memory and credentials out of shared records.

Risk: LAN access or disabling authentication can expose memory or credentials.

Mitigation: Prefer local stdio or loopback access, avoid --no-auth, and rotate any token exposed over an untrusted network.

Risk: Agent-driven MCP configuration changes or autostart setup can change system behavior.

Mitigation: Review and approve MCP configuration and LAN enable/autostart changes before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Plain text or Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory actions may create or update local files.]

## Skill Version(s):

0.22.8 (source: ClawHub release, SKILL.md, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
