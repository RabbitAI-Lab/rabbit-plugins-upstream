## Description:

Persistent user-owned memory for agents with standalone runtime execution. Use when an agent should remember, recall, search memory, preserve restart continuity, manage TODOs, record expenses, diagnose XMemo auth, or operate XMemo even when MCP tools are not configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give agents durable XMemo-backed memory, task handoff continuity, TODO tracking, expense recording, and auth/service diagnostics across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may store secrets, tokens, sensitive personal data, or customer data in durable memory.

Mitigation: Do not store secrets or sensitive data unless that use is explicitly approved and appropriate for the memory policy.

Risk: Using --allow-plaintext stores a local credential file that processes running as the same operating-system user may read.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use --allow-plaintext only after accepting the local storage boundary.

Risk: Authenticated commands sent to a custom service origin may disclose credentials to that origin.

Mitigation: Use the default XMemo service or only trusted HTTPS origins; plain HTTP should remain limited to localhost or loopback development.

## Reference(s):

- [XMemo Skill Operations](references/operations.md)
- [XMemo Skill Troubleshooting](references/troubleshooting.md)
- [XMemo hosted service](https://xmemo.dev)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; command outputs may be plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credential values are not printed; recall/search support compact output, and JSON responses are intended for trusted callers.]

## Skill Version(s):

1.1.9 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
