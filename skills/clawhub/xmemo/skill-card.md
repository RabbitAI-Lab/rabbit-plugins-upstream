## Description:

Helps agents remember and retrieve durable context, maintain task continuity and TODOs, and manage expenses through the XMemo cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can retain project decisions and preferences across sessions, retrieve relevant memories, coordinate TODOs, preserve restart context, and track expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected memories, TODOs, restart state, and ledger entries are sent to the XMemo service.

Mitigation: Use the service only for information you intend to share; do not store secrets or sensitive personal data as memories.

Risk: Device login can leave an unencrypted token in the user's home directory.

Mitigation: Prefer XMEMO_KEY or a managed secret store; use device login only when local credential storage is acceptable.

Risk: Ledger write and delete commands can change financial records.

Mitigation: Review the intended transaction and identifier before recording or confirming a deletion.

## Reference(s):

- [XMemo Skill on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Authentication setup](references/auth-setup.md)
- [Memory operations](references/memory-operations.md)
- [Ledger operations](references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with command-line examples and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory, TODO, restart, and ledger results depend on account access and the XMemo service.]

## Skill Version(s):

1.1.45 (source: ClawHub release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
