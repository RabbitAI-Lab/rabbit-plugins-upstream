## Description:

Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, preserve restart continuity, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use XMemo Memory to persist user-owned memories across sessions, recall or search project context, preserve task handoffs, manage TODOs, record expenses, and diagnose XMemo authentication when native MCP tools are not configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standalone runtime can store a local XMemo credential as an unencrypted user file when plaintext storage is explicitly allowed.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local user-file trust boundary.

Risk: Agents may store secrets, sensitive personal data, or private customer data as durable memories if users provide that content.

Mitigation: Do not save secrets or sensitive data unless explicitly requested and the memory tool supports the required privacy policy.

Risk: Authenticated commands sent to a custom service origin can expose credentials to that origin.

Mitigation: Use the default https://xmemo.dev service or only trusted HTTPS custom origins; plain HTTP is limited to localhost or loopback development.

Risk: Temporary access has reduced capability and lifetime compared with a formal account.

Mitigation: Use formal login by default; reserve temporary registration for unattended use or explicit registration decline, and disclose the item and expiry limits.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo](https://xmemo.dev)
- [ClawHub XMemo Skill](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands can emit compact text or JSON output; normal human-facing restart output is bounded to status, ID, and time fields.]

## Skill Version(s):

1.1.7 (source: server release evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
