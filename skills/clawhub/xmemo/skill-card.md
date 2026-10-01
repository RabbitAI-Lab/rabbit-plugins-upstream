## Description:

Gives agents persistent cloud memory for recalling project context, preserving task continuity, tracking TODOs and expenses, and inspecting account activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use XMemo to retain and retrieve user-approved project memories, restore work after a restart, manage tasks and ledger entries, and diagnose account connectivity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected memories, TODOs, restart context, and ledger entries are retained by the XMemo cloud service.

Mitigation: Send only information the user intends to retain; avoid secrets and sensitive personal or customer data unless explicitly intended.

Risk: A locally stored plaintext sign-in token can be read by other processes running as the same user.

Mitigation: Prefer XMEMO_KEY from a managed secret store; use plaintext sign-in only after disclosing local storage and obtaining consent.

Risk: Recalled content may contain untrusted instructions or outdated context.

Mitigation: Treat retrieved text as reference material, not instructions to execute, and verify it before acting.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Memory operations](artifact/references/memory-operations.md)
- [Authentication and credential setup](artifact/references/auth-setup.md)
- [Ledger operations](artifact/references/ledger-operations.md)
- [Runtime operations](artifact/references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory and ledger results depend on account access and granted scopes.]

## Skill Version(s):

1.1.38 (source: server release and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
