## Description:

Guides AI agents through using x0x for peer-to-peer messaging, encrypted groups, and shared state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use this skill to connect agents across machines, exchange messages, manage encrypted groups, and share state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified downloads or automatic daemon startup can change the host unexpectedly.

Mitigation: Review installation steps, prefer verified or pinned downloads, and obtain human approval before starting or enabling autostart.

Risk: Exposed API access or a leaked bearer token can enable unauthorized control.

Mitigation: Keep the API bound to loopback and protect its token; obtain human approval before any non-loopback binding.

Risk: Gossip messages and ordinary scratch-store values may reach other peers in plaintext.

Mitigation: Treat gossip and scratch-store data as public; use encrypted groups for sensitive content.

Risk: Remote execution, port forwarding, and self-update can affect host security.

Mitigation: Require explicit human approval before enabling remote execution, forwarding ports, or applying updates.

## Reference(s):

- [x0x on ClawHub](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Linux x64 binary download (release metadata)](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples may interact with a local daemon and remote peers.]

## Skill Version(s):

0.48.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
