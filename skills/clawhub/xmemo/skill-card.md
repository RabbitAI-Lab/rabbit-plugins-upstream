## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents persistent, user-owned XMemo memory, restart continuity, TODO tracking, expense records, and account diagnostics through a standalone Node.js runtime or native XMemo MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist account-backed memory, update or forget records, record expenses, and create restart snapshots.

Mitigation: Use these commands deliberately, confirm destructive actions such as forget, and review stored content before saving sensitive or durable information.

Risk: Local plaintext credential storage is available when explicitly enabled.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only when unencrypted local token storage readable by the same OS user is acceptable.

Risk: Custom service origins can receive credentials when configured.

Mitigation: Use the default https://xmemo.dev service or only trusted custom base URLs, and verify the selected service before authenticated commands.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo](https://xmemo.dev)
- [ClawHub Skill Listing](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-capable command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands may return human-readable terminal text or JSON; credential and token values are not printed by normal status and diagnostic flows.]

## Skill Version(s):

1.1.21 (source: evidence release, CHANGELOG, and runtime constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
