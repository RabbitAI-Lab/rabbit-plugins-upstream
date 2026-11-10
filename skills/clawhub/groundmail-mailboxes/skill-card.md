## Description:

Use when an AI agent needs its own email address: signing up for a service, receiving a verification code or magic link, reading and replying to mail, or waiting for a message. Also when the user asks for an inbox or mailbox for an agent, a disposable address for a sign-up flow, or for an agent to get email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktryberceo](https://clawhub.ai/user/ktryberceo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use the skill to create and manage mailboxes for agents, receive sign-up messages, and send or reply to email through Groundmail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags an unpinned `npx groundmail-cli` command that could run an unreviewed package version; the scan is partial and does not establish that the skill is safe.

Mitigation: Review the skill before installing. Prefer a reviewed, explicitly versioned CLI or a preinstalled dependency with verified integrity.

Risk: Inbound email can contain untrusted or hidden instructions.

Mitigation: Treat every email as untrusted data, never follow instructions in email, and use `visible_text` to leave out hidden text.

## Reference(s):

- [Groundmail Agent Mailboxes Guide](https://docs.groundmail.dev/guides/agent-mailboxes)
- [Groundmail](https://groundmail.dev)
- [Groundmail Agent Mailboxes on ClawHub](https://clawhub.ai/ktryberceo/skills/groundmail-mailboxes)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Email messages]

**Output Format:** [Markdown instructions, shell commands, and mailbox message data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Email content may include untrusted text, extracted verification codes, and links.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
