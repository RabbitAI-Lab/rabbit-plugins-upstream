## Description:

Guides AI agents in setting up peer-to-peer networking for messaging, group collaboration, and shared state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to connect agent devices, exchange messages, and coordinate work across decentralized groups and shared stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating the skill can run a persistent peer-to-peer daemon with broad owner-level controls.

Mitigation: Install only when persistent networking is needed; prefer reviewed or pinned binaries, inspect the auto-starting shell installer, and disable self-updates if agent-triggered upgrades are unacceptable.

Risk: Exposing the daemon API or its durable token could grant unauthorized control.

Mitigation: Keep the API loopback-only and protect the durable api-token.

Risk: Owner-key changes, remote execution, sync enrollment, history purges, or upgrade application can have significant consequences.

Mitigation: Require human approval before these operations.

## Reference(s):

- [x0x ClawHub release](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x Linux binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include instructions for a persistent local networking daemon and owner-authorized actions.]

## Skill Version(s):

0.46.5 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
