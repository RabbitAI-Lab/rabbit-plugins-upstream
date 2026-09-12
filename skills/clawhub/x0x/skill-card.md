## Description:

Secure computer-to-computer networking for AI agents with gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT OR Apache-2.0

## Use Case:

Developers and agent operators use this skill to install, run, and operate x0x networking for peer discovery, direct messages, encrypted groups, CRDT task or key-value state, delegation, voice, and controlled remote operations across agent machines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and operates a persistent networking daemon and CLI with broad local API capabilities.

Mitigation: Install only after human approval, prefer pinned and checksum- or signature-verified release paths, and keep daemon startup and autostart choices explicit.

Risk: Binding the API beyond loopback exposes bearer-token-protected daemon endpoints without built-in TLS or access controls described in the evidence.

Mitigation: Keep the API bound to loopback unless a reviewed deployment adds TLS, access controls, token protection, and operational monitoring.

Risk: Remote exec, self-update, owner-key, device-enrollment, and history-purge actions can materially affect the host or trusted network.

Mitigation: Require explicit human approval for those actions and use trust, ACL, token, and owner-key controls before enabling them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Security and cryptography documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Symphony integration documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Linux x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)
- [Windows x64 release download](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-windows-x64.zip)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, REST examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers daemon setup, local API use, identity handling, encrypted groups, CRDT state, delegation, diagnostics, updates, and operational safeguards.]

## Skill Version(s):

0.42.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
