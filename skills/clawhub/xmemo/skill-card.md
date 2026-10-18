## Description:

Provides cloud-backed memory, task continuity, TODO tracking, and expense records for agents across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use XMemo to retain project context, restore work after restarts, manage TODOs, and track expenses across sessions and tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-backed memory and ledger entries may expose secrets or sensitive personal data.

Mitigation: Avoid storing secrets or sensitive personal data; review content before sending it to XMemo.

Risk: Plaintext local credential storage can expose account access to processes running as the same user.

Mitigation: Prefer XMEMO_KEY or a managed secret store over plaintext credential storage.

Risk: Ledger writes and delete commands can change or remove user records.

Mitigation: Review ledger and delete commands before approval, including the target and transaction details.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](artifact/references/memory-operations.md)
- [Authentication setup](artifact/references/auth-setup.md)
- [Ledger operations](artifact/references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall, task status, and ledger summaries depend on the user's XMemo account and permissions.]

## Skill Version(s):

1.1.44 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
