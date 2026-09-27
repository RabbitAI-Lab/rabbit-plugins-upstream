## Description:

Gives agents persistent, user-owned memory for recall, task continuity, TODOs, and optional expense tracking through XMemo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use XMemo to save and retrieve durable project context, resume interrupted tasks, track TODOs, and optionally manage expense records across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory queries and saved content are sent to the XMemo cloud service.

Mitigation: Use the service only when durable cloud memory is wanted; keep secrets and sensitive identifiers out of queries and saved content.

Risk: Browser sign-in can save a credential unencrypted for the local OS user.

Mitigation: Prefer XMEMO_KEY from a managed secret store; use plaintext login only after accepting local credential exposure.

Risk: Project instruction changes can enable future XMemo use automatically, and ledger writes or forget actions change stored records.

Mitigation: Approve AGENTS.md or CLAUDE.md memory sections explicitly, and review ledger writes and forget actions before execution.

## Reference(s):

- [XMemo ClawHub release](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Memory operations](references/memory-operations.md)
- [Authentication setup](references/auth-setup.md)
- [Ledger operations](references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text or JSON; Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory results and account diagnostics depend on the user's XMemo account and permissions.]

## Skill Version(s):

1.1.33 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
