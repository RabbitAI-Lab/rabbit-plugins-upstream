## Description:

Enables an AI agent to register an Atomic Mail inbox and read or send email through JMAP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomicmail](https://clawhub.ai/user/atomicmail)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can connect an agent to an Atomic Mail inbox to register an account, check messages, and send or reply to email when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local mail credentials and JWT files could expose inbox access if disclosed.

Mitigation: Keep the credential directory private; never commit credentials.json or JWT files.

Risk: An agent with inbox access could send mail or change mailbox state during an unattended check.

Mitigation: Review scheduled jobs and keep inbox checks read-only unless explicitly authorized to send or modify mail.

## Reference(s):

- [Atomic Mail skill on ClawHub](https://clawhub.ai/atomicmail/skills/atomicmail)
- [Atomic Mail](https://atomicmail.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Natural-language email summaries and instructions with shell commands; mail requests can return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scheduled inbox reports can be read-only; sending or changing mail requires authorization.]

## Skill Version(s):

0.3.31 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
