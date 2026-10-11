## Description:

Helps AI agents use x0x for peer-to-peer messaging, group collaboration, and shared data across computers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use this skill to install or connect to an x0x agent, exchange messages, join groups, and coordinate work over a peer-to-peer network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's software can start a persistent peer-to-peer daemon with remote execution, port forwarding, and self-update capabilities.

Mitigation: Obtain operator approval before installation or startup; enable only the capabilities needed and review access controls.

Risk: Unverified downloads or an exposed local API can put agent access and durable identity keys at risk.

Mitigation: Prefer reviewed or signature-verified installation, protect tokens and identity keys, and keep the API on loopback unless TLS and strong access controls are added.

Risk: Gossip messages and ordinary plaintext stores may expose sensitive data to other peers.

Mitigation: Keep sensitive data out of public gossip and plaintext stores; use private messaging or encrypted groups as appropriate.

## Reference(s):

- [x0x skill listing](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [x0x security and cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x operations](https://github.com/saorsa-labs/x0x/blob/main/docs/skill/operations.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed x0x CLI and, for most tasks, access to an authorized daemon.]

## Skill Version(s):

0.47.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
