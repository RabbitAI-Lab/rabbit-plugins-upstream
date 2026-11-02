## Description:

Provides persistent, user-owned agent memory with recall, restart continuity, TODO and expense tracking, and runtime diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use XMemo to preserve selected project context across sessions, retrieve relevant memories, manage TODOs and expenses, and maintain restart continuity through an account-backed runtime.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memories, queries, and expense details may contain sensitive personal information.

Mitigation: Keep secrets and sensitive personal data out of uploads and queries.

Risk: Device login saves an unencrypted token readable by processes running as the same user.

Mitigation: Prefer a managed secret store for credentials.

Risk: Ledger deletions, project instruction changes, and runtime updates can have lasting effects; custom service hosts receive ordinary credentials.

Mitigation: Review these actions before approving them and configure only trusted service hosts.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Authentication and credential setup](references/auth-setup.md)
- [Memory operations](references/memory-operations.md)
- [Ledger operations](references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Human-readable text or Markdown with shell command examples; some commands support JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain user-owned memory and account data; some changes require explicit confirmation.]

## Skill Version(s):

1.1.47 (source: server-resolved release, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
