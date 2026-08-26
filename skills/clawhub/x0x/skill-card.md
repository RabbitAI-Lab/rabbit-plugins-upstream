## Description:

x0x provides secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use x0x to install and operate secure peer-to-peer networking for AI agents, including gossip broadcast, direct messaging, replicated CRDT state, group encryption, and local REST/WebSocket integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and starts trusted local peer-to-peer networking software with a daemon and local API.

Mitigation: Install only when this networking capability is intended, start the daemon explicitly, and avoid autostart unless persistent operation is required.

Risk: Local API tokens, remote execution, and port-forward settings can expose sensitive capabilities if mishandled.

Mitigation: Protect the local api-token, review trust and ACL settings before enabling remote execution or forwards, and keep remote capabilities limited to trusted peers.

Risk: Automatic binary replacement may conflict with environments that require manual change review.

Mitigation: Use check-only upgrade mode when manual review is required before applying an update.

## Reference(s):

- [ClawHub x0x Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Saorsa Labs x0x Repository](https://github.com/saorsa-labs/x0x)
- [x0x Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [x0x API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [x0x SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [x0x Tailnet Tracking Issue](https://github.com/saorsa-labs/x0x/issues/132)
- [Saorsa Labs](https://saorsalabs.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, configuration examples, JSON payloads, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation, daemon operation, REST/WebSocket, trust, forwarding, and orchestration guidance for an agent.]

## Skill Version(s):

0.39.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
