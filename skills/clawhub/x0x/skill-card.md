## Description:

Secure computer-to-computer networking for AI agents - gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal for decentralized applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to install or attach to an x0x daemon, create agent identities, discover peers, and exchange direct or group messages. It also guides agents through CRDT-backed tasks and stores, tailnet forwarding, relay operation, remote execution controls, upgrades, diagnostics, and local API configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables a persistent peer-networking daemon with local identity keys and a durable control token.

Mitigation: Keep the REST API bound to loopback, protect the durable API token, and treat session tokens as secrets.

Risk: Remote execution, forwarding, relay operation, and daemon self-update controls can expand agent authority.

Mitigation: Disable or tightly gate exec, forwarding, relay, and daemon self-update unless they are required, and review trust and ACL settings before use.

Risk: Latest-download and script-based installs can change over time.

Mitigation: Prefer pinned or independently verified release artifacts and review install scripts before execution.

Risk: Gossip pub/sub payloads are readable by relaying peers.

Mitigation: Use gossip topics only for data acceptable to publish openly; use direct messages or encrypted groups for private communication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x repository](https://github.com/saorsa-labs/x0x)
- [Saorsa Labs](https://saorsalabs.com)
- [Security and Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Symphony Integration](https://github.com/saorsa-labs/x0x/blob/main/docs/symphony-integration.md)
- [Remote Exec](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [Linux x64 GNU release artifact](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, REST examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform-specific installation guidance and operational safety notes.]

## Skill Version(s):

0.41.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
