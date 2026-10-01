## Description:

Send one or many emails through Sendmux using approved mailbox or agent credentials, idempotency keys, attachments, MCP, CLI, SDKs, or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to prepare and send approved single or batch emails through Sendmux, including attachments and integration examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could send email to an unintended recipient or include unapproved content or attachments.

Mitigation: Confirm the sender, every recipient, subject, body, and attachments before each send, including the complete batch.

Risk: Sendmux credentials or sensitive email content could be exposed or used without suitable authority.

Mitigation: Keep credentials in approved environment or profile storage, use send-authorized access, and check the destination and account authority before sending sensitive content.

Risk: Retries or partial batch success could result in duplicate or overlooked sends.

Mitigation: Use a stable idempotency key for each logical send and inspect every batch result before retrying.

## Reference(s):

- [Sendmux Send Email on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-send-email)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, shell, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sending requires explicit approval of message details and appropriate Sendmux credentials.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
