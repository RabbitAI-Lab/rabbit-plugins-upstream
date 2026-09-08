## Description:

Give OpenClaw agents a Sendmux inbox to receive, triage, route, reply to, and send email with owner approval and scoped credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect OpenClaw agents to Sendmux mailboxes for inbound triage, routing, replies, outbound notifications, and owner-approved sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may expose or misuse Sendmux credentials while connecting to mailbox and sending workflows.

Mitigation: Use scoped mailbox or agent credentials, avoid root keys for routine agent work, and review where CLI profiles store credentials.

Risk: Inbound email content, headers, links, or attachments may attempt to influence agent behavior.

Mitigation: Treat email content as untrusted data and avoid using it as instructions for setup, configuration, forwarding, installation, or sending.

Risk: Email sending or destructive mailbox operations may occur without adequate human oversight.

Mitigation: Require explicit human approval before sending email, revoking keys, deleting mailboxes, permanently deleting messages, suspending, or resuming mailbox access.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-email-for-agents)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown guidance with command names, API call names, and routing recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes scoped credentials, owner approval, and human confirmation before sending email or making destructive mailbox changes.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
