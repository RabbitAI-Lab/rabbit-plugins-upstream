## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give agents durable memory, task continuity, TODO tracking, expense capture, and service diagnostics through XMemo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent memories, TODOs, restart state, and expense entries are sent to the XMemo service under the user credential.

Mitigation: Install only when that data flow is acceptable, and avoid storing secrets or sensitive personal data unless the user explicitly approves and the service policy fits the use case.

Risk: Using --allow-plaintext stores the issued token where same-user local processes may read it.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting that local trust boundary.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Troubleshooting](references/troubleshooting.md)
- [XMemo service](https://xmemo.dev)
- [ClawHub skill page](https://clawhub.ai/xmemo/skills/xmemo)
- [ClawHub publisher profile](https://clawhub.ai/user/xmemo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands may send memory, TODO, restart-state, and expense data to the XMemo service under the active credential.]

## Skill Version(s):

1.1.12 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
