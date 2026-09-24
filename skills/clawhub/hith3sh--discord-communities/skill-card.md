## Description:

Manage Discord guilds, channels, messages, members, roles, and application commands - powered by ClawLink.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hith3sh](https://clawhub.ai/user/hith3sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect OpenClaw to Discord through ClawLink and manage Discord guilds, channels, messages, members, roles, application commands, entitlements, and role connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on ClawLink as an external OAuth broker with persistent Discord access.

Mitigation: Install only after reviewing requested Discord OAuth scopes, ClawLink authorization, and revocation steps.

Risk: Some Discord actions can leave guilds, change profile data, edit command permissions, consume entitlements, or delete role-connection and entitlement data.

Mitigation: Require explicit user confirmation before running high-impact or destructive Discord actions.

Risk: The security verdict flags the release as suspicious because it asks users to trust an unversioned external plugin and hosted broker.

Mitigation: Review and approve the ClawLink plugin and service trust boundary before connecting production Discord accounts or servers.

## Reference(s):

- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=discord-communities)
- [ClawLink Discord Dashboard](https://claw-link.dev/dashboard?add=discord)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ClawLink pairing and Discord OAuth authorization before Discord tools are available.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
