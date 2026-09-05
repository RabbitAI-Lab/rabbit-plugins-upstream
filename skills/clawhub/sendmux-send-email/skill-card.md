## Description:

Send one or many emails through Sendmux using approved mailbox or agent credentials, idempotency keys, attachments, MCP, CLI, SDKs, or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when an agent needs to prepare Sendmux email-sending commands, API calls, SDK code, or MCP tool usage with confirmed recipients, message content, credentials, idempotency, and attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could send email to unconfirmed recipients or with unapproved message content.

Mitigation: Require review of every recipient, sender, subject, body, batch list, and attachment before allowing a send.

Risk: Sendmux credentials could be exposed if a user pastes secrets into chat.

Mitigation: Use scoped or revocable Sendmux credentials and do not ask users to paste API keys into chat.

Risk: Repeated attempts could duplicate sends or trigger idempotency conflicts.

Mitigation: Use one stable Idempotency-Key per logical email or batch and handle idempotency conflicts deliberately.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux Sending API endpoint](https://smtp.sendmux.ai/api/v1/emails/send)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-send-email)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, TypeScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Sendmux API request bodies, CLI commands, SDK snippets, MCP tool choices, idempotency guidance, and attachment-handling guidance.]

## Skill Version(s):

1.0.7 (source: server release metadata); SKILL.md frontmatter reports 1.4.2

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
