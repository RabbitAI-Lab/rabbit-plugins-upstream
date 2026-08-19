## Description:

Persistent user-owned memory for agents with standalone runtime execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents persistent memory across sessions, including recall, search, task handoff, TODO management, expense recording, and authentication diagnosis for XMemo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plaintext credential storage can expose the local XMemo token to processes running as the same operating-system user.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local trust boundary.

Risk: Agents may save secrets or sensitive personal or customer data into persistent memory.

Mitigation: Do not save secrets, cookies, private keys, or sensitive personal/customer data unless the user explicitly intends to store it in XMemo.

Risk: Authenticated commands sent to a custom service origin disclose the active credential to that host.

Mitigation: Use only trusted HTTPS origins for authenticated commands; plain HTTP is limited to localhost or loopback development.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands require Node.js 20 or newer, network access to XMemo, and a credential for authenticated operations.]

## Skill Version(s):

1.1.10 (source: server evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
