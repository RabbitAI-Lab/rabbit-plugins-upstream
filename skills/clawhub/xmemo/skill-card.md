## Description:

Gives agents persistent, user-owned memory for recalling decisions, continuing tasks across sessions, and managing TODOs and expenses through XMemo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xmemo](https://clawhub.ai/user/xmemo)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use XMemo to retain and retrieve project context across sessions, track action items and expenses, and restore task continuity with an account-backed cloud memory service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive information may persist in the account-backed cloud memory service.

Mitigation: Do not save secrets or sensitive personal data; store only information appropriate for persistent memory.

Risk: Plaintext local credential storage may expose account access to processes running as the same user.

Mitigation: Prefer XMEMO_KEY from a managed secret store over plaintext local storage.

Risk: A custom service URL may receive standard credentials.

Mitigation: Use custom base URLs only for trusted hosts.

## Reference(s):

- [XMemo Memory on ClawHub](https://clawhub.ai/xmemo/skills/xmemo)
- [Authentication and credential setup](references/auth-setup.md)
- [Memory operations](references/memory-operations.md)
- [Runtime operations](references/runtime-operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory and account operations require an XMemo account and appropriate credentials.]

## Skill Version(s):

1.1.40 (source: ClawHub release evidence and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
