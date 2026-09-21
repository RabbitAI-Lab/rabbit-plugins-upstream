## Description:

Send one or many emails through Sendmux using approved mailbox or agent credentials, idempotency keys, attachments, MCP, CLI, SDKs, or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to prepare Sendmux email sending workflows, including single sends, batch sends, attachments, idempotency, and CLI, SDK, HTTP, or MCP examples. It is intended for situations where the user is ready to send outbound email through Sendmux or needs commands and code for doing so safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could send email before the user has confirmed recipients, subject, body, sender, and attachments.

Mitigation: Require explicit user confirmation of the complete message or batch before any Sendmux send tool, API call, CLI command, or SDK call is used.

Risk: Sendmux credentials could be exposed if users paste keys into chat or commands print retained secrets.

Mitigation: Keep Sendmux keys in approved environment or profile storage, avoid asking users to paste secrets, and keep bearer tokens and signed upload URLs out of retained command output.

Risk: Attachments may upload local data outside the workspace or be sent with the wrong attachment reference.

Mitigation: Use the documented attachment upload flow, compare file size to the returned limit, avoid model-generated base64 for real files, and send only the returned attachment_id.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-send-email)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, shell, TypeScript, HTTP, and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Sendmux request bodies, idempotency-key guidance, credential setup guidance, batch-send checks, and attachment-handling instructions.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
