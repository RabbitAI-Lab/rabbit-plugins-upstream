## Description:

Guides AI agents in using secure peer-to-peer networking for messaging, group collaboration, and shared state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use x0x to connect computers for direct messaging, public gossip, encrypted groups, and collaborative tasks through a persistent peer-to-peer daemon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and starting the persistent networking daemon exposes ongoing peer-to-peer connectivity.

Mitigation: Install only when the daemon is needed; prefer a manually reviewed binary or signature-checking installer and authorize daemon startup explicitly.

Risk: Exposing the REST API or leaking the durable token or owner key could allow unauthorized control.

Mitigation: Keep the API bound to loopback and protect the durable token and owner key.

Risk: Gossip topic messages are visible to relaying peers.

Mitigation: Do not publish private data on gossip topics; use direct messages or encrypted groups instead.

Risk: Remote command execution and daemon self-updates have elevated operational impact.

Mitigation: Leave remote execution and self-update disabled unless intentionally administering them.

## Reference(s):

- [ClawHub x0x skill](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x release downloads](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.46.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
