## Description:

x0x provides secure computer-to-computer networking for AI agents, including gossip broadcast, direct messaging, CRDTs, group encryption, post-quantum encryption, and NAT traversal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent builders use x0x to install and operate a local peer-to-peer networking daemon for direct messaging, gossip/pub-sub, encrypted groups, replicated CRDT state, file transfer, local port forwarding, and tightly gated remote command execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local daemon can manage identities, exchange data, forward local ports, and optionally allow remote command execution.

Mitigation: Install only when those peer-to-peer capabilities are intended, keep remote execution and forwarding disabled by default, and enable them only with exact ACLs for trusted peers.

Risk: The local API token authorizes daemon operations.

Mitigation: Protect the API token and avoid exposing durable tokens in URLs; use short-lived session tokens where the artifact documents browser or WebSocket access.

Risk: Install and update workflows download executable binaries.

Mitigation: Prefer reviewed or verified install and update paths, and review downloaded installer scripts before running them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jimcollinson/skills/x0x)
- [Security & Cryptography](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [Full API Reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [SDK Quickstart](https://github.com/saorsa-labs/x0x/blob/main/docs/sdk-quickstart.md)
- [Remote Exec Documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/exec.md)
- [Upgrade System](https://github.com/saorsa-labs/x0x/blob/main/docs/upgrade-system.md)
- [Linux x64 GNU Release Archive](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API Calls]

**Output Format:** [Markdown with inline bash, JSON, and TOML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for download/install workflows; the installed x0x and x0xd binaries expose CLI, REST, SSE, and WebSocket interfaces.]

## Skill Version(s):

0.39.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
