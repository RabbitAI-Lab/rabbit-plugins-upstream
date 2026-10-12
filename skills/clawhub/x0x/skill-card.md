## Description:

Guides agents in using x0x for peer-to-peer messaging, group communication, gossip, and shared data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up peer-to-peer agent connectivity, exchange direct and group messages, and coordinate through gossip and shared stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running persistent peer-to-peer software expands the agent's network exposure.

Mitigation: Install only when peer-to-peer networking is intended; prefer verified or pinned releases over an unsigned auto-starting shell installer.

Risk: Exposing the local API or leaking credentials may permit unauthorized access.

Mitigation: Keep the API bound to loopback unless TLS and strong access controls are added; protect the durable token and owner keys.

Risk: Remote execution, port forwarding, file transfer, and self-upgrade can cause consequential changes.

Mitigation: Require explicit human approval before remote exec, forwarding, file transfers, or upgrade/apply actions.

## Reference(s):

- [ClawHub x0x release](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x release downloads (installation metadata; not verified provenance)](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [x0x operations guide (skill-linked documentation; not verified provenance)](https://github.com/saorsa-labs/x0x/blob/main/docs/skill/operations.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may start and interact with a persistent peer-to-peer daemon.]

## Skill Version(s):

0.47.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
