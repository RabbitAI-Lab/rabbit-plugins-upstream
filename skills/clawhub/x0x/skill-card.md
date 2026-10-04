## Description:

Guides agents in setting up and using peer-to-peer networking for messaging, collaboration, and shared state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect peers, exchange direct or group messages, broadcast updates, and coordinate shared tasks through x0x.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing x0x starts a persistent peer-to-peer networking daemon.

Mitigation: Install and start it only with the owner's authorization and after reviewing the daemon's networking behavior.

Risk: Remote execution and self-update capabilities can expand the impact of misuse.

Mitigation: Disable remote execution and self-update unless they are needed.

Risk: Exposing the REST API or durable API token can permit unauthorized access.

Mitigation: Keep the API bound to loopback and protect the durable token.

Risk: Gossip topics are readable by relaying peers, and an unsigned shell installer may not verify downloaded software.

Mitigation: Treat gossip as public and prefer verified or pinned releases over the unsigned shell installer.

## Reference(s):

- [ClawHub x0x release](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Linux x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions may start or configure a persistent peer-to-peer daemon.]

## Skill Version(s):

0.46.1 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
