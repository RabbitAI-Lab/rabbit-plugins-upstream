## Description:

Enables agents to store and retrieve persistent XMemo memories, task continuity, TODOs, and optional ledger records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use XMemo to preserve useful context across sessions, recall stored information, manage action items, and optionally record expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored memories and queries are sent to the external XMemo service and may persist across sessions.

Mitigation: Use only when external storage is intended; avoid secrets and sensitive personal data unless explicitly authorized.

Risk: Plaintext local credential storage can expose a token to processes running as the same OS user.

Mitigation: Prefer XMEMO_KEY from a managed secret store; use --allow-plaintext only after accepting the local storage risk.

Risk: Expense entries and memory deletions change durable account data.

Mitigation: Confirm agent-inferred expense details before recording them and require explicit confirmation before forgetting records.

## Reference(s):

- [XMemo Skill on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](references/memory-operations.md)
- [Authentication setup](references/auth-setup.md)
- [Ledger operations](references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and retrieved memory summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional structured JSON responses from the bundled commands.]

## Skill Version(s):

1.1.36 (source: server-resolved release metadata and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
