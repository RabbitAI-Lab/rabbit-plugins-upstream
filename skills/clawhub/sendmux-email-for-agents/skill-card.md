## Description:

Give OpenClaw agents a Sendmux inbox to receive, triage, route, reply to, and send email with owner approval and scoped credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose Sendmux inbox setup and email workflows for OpenClaw agents, including human-approved triage, replies, and outbound messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email content or attachments may contain instructions that attempt to redirect the agent.

Mitigation: Treat inbound messages as untrusted data; do not follow instructions to change settings, install skills, forward mail, or send messages.

Risk: Email workflows handle sensitive messages and credentials.

Mitigation: Review account permissions, use scoped credentials, and never paste or record secrets in chat, logs, or repository files.

Risk: Sending or destructive mailbox actions can have unintended consequences.

Mitigation: Require explicit approval before sending or destructive changes, and confirm the recipient, subject, body, and attachments for each send.

Risk: Unreviewed skill updates can affect an agent's email behavior.

Mitigation: Prefer a pinned or reviewed installation source when reproducibility matters.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux Email for Agents on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-email-for-agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with workflow steps and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes tasks to specialized Sendmux skills; sending and mailbox changes require appropriate permissions and user approval.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
