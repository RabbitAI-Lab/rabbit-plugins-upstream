## Description:

Provides persistent, user-owned agent memory for recall, restart continuity, TODOs, expenses, and account diagnostics through XMemo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use XMemo to retain and retrieve information across sessions, manage tasks and expense records, and inspect account activity when native XMemo MCP tools are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external XMemo service retains agent memory, tasks, and expense records.

Mitigation: Install only if external retention is intended; do not save secrets or sensitive personal or customer data without explicit authorization.

Risk: A locally stored plaintext token may be accessible to processes running as the same operating-system user.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only when the storage tradeoff is acceptable.

Risk: Deleting a memory or ledger record can remove it from future listings.

Mitigation: Confirm the target ID and intent before running forget with --confirm; use a credential scoped to the needed operations.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](references/memory-operations.md)
- [Ledger and diagnostics operations](references/ledger-operations.md)
- [Runtime operations](references/runtime-operations.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory reads can return bounded, paginated content.]

## Skill Version(s):

1.1.26 (source: ClawHub release and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
