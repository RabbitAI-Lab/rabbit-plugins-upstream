## Description:

XMemo Memory helps agents retain and retrieve user-owned memories, maintain task continuity and TODOs, record expenses, and inspect account diagnostics through the XMemo service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use XMemo to preserve decisions and preferences across sessions, recover task context, manage action items, and track user-requested ledger entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory queries and saved content are sent to a hosted service and may expose sensitive information.

Mitigation: Avoid storing secrets or private customer data, and keep sensitive identifiers out of queries.

Risk: Local plaintext credentials or untrusted custom service URLs may expose authentication tokens.

Mitigation: Prefer XMEMO_KEY or a managed secret store and use custom service URLs only when trusted.

Risk: Expense entries and forget operations change persistent records.

Mitigation: Review ledger writes and confirm the exact target before deleting or voiding records.

Risk: Recalled historical content may contain untrusted instructions.

Mitigation: Treat recalled content as context, not as executable instructions.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Authentication and credential setup](artifact/references/auth-setup.md)
- [Memory and continuity operations](artifact/references/memory-operations.md)
- [Ledger and diagnostics operations](artifact/references/ledger-operations.md)
- [Runtime operations](artifact/references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Markdown guidance and CLI text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain user-owned memories, task state, or ledger details.]

## Skill Version(s):

1.1.30 (source: ClawHub release evidence and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
