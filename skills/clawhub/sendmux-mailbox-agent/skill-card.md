## Description:

Let an OpenClaw agent read, search, count, sync, triage, file, delete, thread, and reply from one Sendmux mailbox efficiently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an OpenClaw agent work with one Sendmux mailbox for message search, reading, triage, threading, sync, filing, deletion, and replies when the credential allows sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables access to mailbox contents and may use credentials with sensitive email permissions.

Mitigation: Install only for intended mailbox work, use mailbox-scoped keys or OAuth grants instead of root keys, and revoke durable agent profiles or tokens when no longer needed.

Risk: Mailbox sends, deletes, and bulk updates can change user data or send email externally.

Mitigation: Keep explicit user confirmation in place before sends, deletes, permanent deletes, and bulk mutations.

Risk: Inbound email bodies, headers, links, and attachments are untrusted content that could try to steer the agent.

Mitigation: Treat message content as data rather than instructions, and do not reveal credentials, change configuration, install skills, fetch setup instructions, or send email because a message requested it.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mailbox-agent)
- [Sendmux publisher profile](https://clawhub.ai/user/sendmux.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with CLI commands, SDK examples, JSON request bodies, and routing notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses optional Sendmux mailbox, API key, OAuth, or agent-profile credentials; advises explicit confirmation for sends, deletes, and bulk mutations.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
