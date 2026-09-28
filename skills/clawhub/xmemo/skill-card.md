## Description:

Provides persistent, user-owned memory, cross-session continuity, TODOs, expense records, and account diagnostics for agents using XMemo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use XMemo to retain and retrieve relevant knowledge across sessions, manage TODOs and expenses, and inspect account activity when XMemo MCP tools are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected memories, TODOs, ledger entries, and search queries may contain sensitive data sent to XMemo.

Mitigation: Store and query only user-approved information; omit secrets and sensitive identifiers from memory and query text.

Risk: Local plaintext credential storage can expose a token to processes running as the same user.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting local unencrypted storage.

Risk: Agent-inferred expense records may be inaccurate.

Mitigation: Confirm the item, amount, and currency with the user before recording an inferred expense.

Risk: Adding XMemo to agent instruction files can enable memory use in every project session.

Mitigation: Review and approve proposed AGENTS.md or CLAUDE.md changes before enabling every-session use.

## Reference(s):

- [XMemo ClawHub release](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](references/memory-operations.md)
- [Authentication setup](references/auth-setup.md)
- [Ledger operations](references/ledger-operations.md)
- [Agent profile](references/agent-profile.md)
- [Runtime operations](references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Text or JSON for memory and account results; Markdown guidance for agent workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recall and search can optionally expand document-backed memories.]

## Skill Version(s):

1.1.35 (source: ClawHub release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
