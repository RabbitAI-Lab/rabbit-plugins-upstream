## Description:

Provides persistent, user-owned cloud memory for agents to recall context, preserve task continuity, manage TODOs and optional expenses, and inspect account diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use XMemo to retain and retrieve durable project context, preferences, and tasks across sessions, with optional expense tracking and account diagnostics when the cloud service is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory and optional ledger data are sent to the XMemo cloud service.

Mitigation: Use the service only when intended; avoid storing secrets or sensitive personal or customer data unless explicitly authorized.

Risk: Plaintext sign-in stores the account token unencrypted under the user's home directory.

Mitigation: Prefer XMEMO_KEY from a managed secret store; use --allow-plaintext only with awareness of local access to the token.

Risk: Memory and ledger delete commands can remove user records.

Mitigation: Check the target ID and obtain explicit confirmation before running confirmed delete commands.

## Reference(s):

- [XMemo skill on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [XMemo service](https://xmemo.dev)
- [Authentication setup](references/auth-setup.md)
- [Memory operations](references/memory-operations.md)
- [Ledger operations](references/ledger-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown with CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-backed results depend on account access and authorized scopes.]

## Skill Version(s):

1.1.41 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
