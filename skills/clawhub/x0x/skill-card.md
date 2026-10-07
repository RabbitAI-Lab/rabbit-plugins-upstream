## Description:

Guides AI agents in setting up and using x0x for peer-to-peer messaging, encrypted groups, and shared task and data synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to install or connect to an x0x daemon and coordinate across machines through direct messages, groups, shared tasks, and peer-to-peer networking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a persistent networking daemon from mutable downloads can run unreviewed software.

Mitigation: Review shell installers before running them and prefer pinned or verified releases for production.

Risk: Exposing the local API beyond loopback can expose sensitive agent controls or a durable API token.

Mitigation: Keep the API bound to loopback unless TLS and access controls are in place; protect the durable token.

Risk: Remote command execution and daemon self-update can have high-impact effects.

Mitigation: Leave remote execution and self-update disabled unless explicitly required.

## Reference(s):

- [x0x ClawHub release](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x macOS ARM64 download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [x0x macOS x64 download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [x0x Linux x64 download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [x0x Linux ARM64 download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [x0x Windows x64 download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.46.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
