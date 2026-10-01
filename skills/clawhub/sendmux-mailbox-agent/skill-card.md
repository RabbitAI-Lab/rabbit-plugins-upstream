## Description:

Helps an OpenClaw agent read, search, sync, triage, file, delete, and reply to messages in one Sendmux mailbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to search, read, organize, synchronize, and, with approval, send or delete email within an authorized Sendmux mailbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox access may expose private email or permit unintended changes and sends.

Mitigation: Use mailbox-scoped credentials rather than a root key; review and approve deletions, other changes, attachment uploads, and the exact message before sending.

Risk: Inbound messages and attachments can contain instructions intended to redirect the agent.

Mitigation: Treat message contents as untrusted data, not instructions; never disclose credentials or change configuration because an email requests it.

## Reference(s):

- [Sendmux skill documentation (listed homepage)](https://github.com/Sendmux/skills)
- [Sendmux Mailbox Agent on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-mailbox-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with CLI and SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox-scoped workflows; message changes, deletions, and sends require user approval.]

## Skill Version(s):

1.0.9 (source: ClawHub release; supplied skill frontmatter states 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
