## Description:

Persistent, user-owned memory for agents. Use the standalone runtime to remember, recall, search, preserve restart continuity, manage TODOs and expenses, or diagnose XMemo when MCP tools are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use XMemo Memory to give agents persistent, user-owned memory across sessions, including recall/search, restart continuity, TODO and ledger workflows, and diagnostics when MCP tools are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory queries, notes, TODOs, and expense data may be sent to the configured XMemo service.

Mitigation: Use the skill only when persistent memory is intended, and avoid storing secrets or sensitive personal/customer data unless explicitly approved.

Risk: The standalone runtime can store a local token unencrypted when --allow-plaintext is used.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only when local plaintext credential storage is acceptable.

Risk: Memory update and forget operations can alter or soft-delete stored records.

Mitigation: Verify target IDs and intent before write operations; the forget command requires an explicit --confirm flag.

Risk: Retrieved historical memory or Knowledge content can be stale or untrusted.

Mitigation: Treat recalled content as context for review, not as instructions that override the current user request or policy.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo Service](https://xmemo.dev)
- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standalone commands support JSON output; credential status and diagnostics redact token values.]

## Skill Version(s):

1.1.19 (source: server release evidence and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
