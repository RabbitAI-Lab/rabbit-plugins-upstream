## Description:

Persistent, user-owned agent memory for saving, recalling, and managing information across sessions, including continuity, TODOs, expenses, account diagnostics, and read-only Cloud Skill access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use XMemo to save and retrieve durable personal context across sessions, coordinate TODOs and ledger entries, and restore task continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is suspicious because scan coverage was incomplete and raised questions about tool scope and persistent effects; it did not establish malicious intent.

Mitigation: Follow the security guidance: defer installation until the author clarifies the tool scope and Dream-run digest behavior, and the executable files can be fully inspected.

Risk: Interactive login can save an authentication token unencrypted in a local credential file.

Mitigation: Prefer XMEMO_KEY from a managed secret store. Use local plaintext storage only with explicit consent on a secure, single-user system.

## Reference(s):

- [XMemo on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Authentication and Credential Setup](artifact/references/auth-setup.md)
- [Memory Operations](artifact/references/memory-operations.md)
- [Standalone Runtime and Execution Guide](artifact/references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Command-line text or JSON responses, with Markdown usage and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network-backed; requires Node.js 22.22.0 or later and an XMemo credential. Some operations change stored memory or ledger data.]

## Skill Version(s):

1.1.52 (source: CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
