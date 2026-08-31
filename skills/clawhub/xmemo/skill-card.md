## Description:

Persistent, user-owned memory for agents that use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use XMemo Memory to persist and recall project context, task state, TODOs, and expense entries across sessions when native XMemo MCP tools are unavailable or a standalone runtime is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected memories, TODOs, restart context, and expense entries to XMemo.

Mitigation: Install and use it only when that data sharing is intended; avoid saving secrets or sensitive personal or customer data unless explicitly approved.

Risk: Credential-writing flows can store an unencrypted token in the current user's XMemo directory when --allow-plaintext is used.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only on trusted machines where same-user local processes and backups are acceptable.

Risk: Custom service origins receive the active credential for authenticated commands.

Mitigation: Use only trusted HTTPS origins, and rely on localhost HTTP only for loopback development.

## Reference(s):

- [XMemo Skill Page](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo Service](https://xmemo.dev)
- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands can emit compact human-readable text or redacted JSON; network requests default to a 30-second timeout and reject responses larger than 8 MiB.]

## Skill Version(s):

1.1.14 (source: server release evidence, CHANGELOG, runtime constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
