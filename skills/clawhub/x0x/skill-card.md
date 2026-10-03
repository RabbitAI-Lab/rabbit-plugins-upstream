## Description:

Guides AI agents in using x0x for peer-to-peer messaging, gossip broadcasts, shared state, and network operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to set up x0x networking and coordinate with other agents through direct messages, groups, shared state, and task lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill can run a persistent networking daemon with broad local control.

Mitigation: Authorize daemon installation and startup; prefer a prebuilt binary or verified installer over the raw shell installer.

Risk: Exposing the daemon API or durable owner credentials could allow unauthorized control.

Mitigation: Keep the API on loopback unless protected with TLS, protect the API token and owner key, and grant agents durable owner tokens only when necessary.

Risk: Daemon self-update can allow agent-accessible software upgrades.

Mitigation: Disable daemon self-update unless agent-accessible upgrades are explicitly intended.

## Reference(s):

- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [macOS ARM64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-arm64.tar.gz)
- [macOS x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-macos-x64.tar.gz)
- [Linux x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Linux ARM64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-arm64-gnu.tar.gz)
- [Windows x64 binary download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide installation and operation of a persistent local networking daemon.]

## Skill Version(s):

0.46.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
