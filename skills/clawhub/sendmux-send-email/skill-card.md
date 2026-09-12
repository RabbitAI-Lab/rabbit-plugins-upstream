## Description:

Send one or many emails through Sendmux using approved mailbox or agent credentials, idempotency keys, attachments, MCP, CLI, SDKs, or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to prepare or send single and batch outbound emails through Sendmux via MCP, CLI, SDKs, or HTTP. It guides agents to confirm recipients, content, credentials, and attachments before sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could send email to incorrect recipients or with unconfirmed content.

Mitigation: Require the user to supply or confirm every recipient, subject, body, and batch message before sending.

Risk: Secrets could be exposed if API keys or tokens are pasted into chat.

Mitigation: Use scoped Sendmux credentials, owner-approved agent profiles, environment variables, or delegated tokens instead of asking users to paste secrets.

Risk: Retries could duplicate outbound email or conflict with a changed payload.

Mitigation: Use one stable idempotency key per logical email or batch and handle idempotency conflicts deliberately.

Risk: Attachments can exceed supported size limits or be encoded inefficiently.

Mitigation: Upload files through Sendmux attachment workflows and pass attachment IDs; respect the documented per-file and final message size limits.

Risk: Batch sends can partially succeed, leaving some messages failed and others queued.

Mitigation: Inspect each batch result item and handle failed indexes separately.

## Reference(s):

- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux Sending API endpoint](https://smtp.sendmux.ai/api/v1/emails/send)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-send-email)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, TypeScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool choices, CLI commands, SDK snippets, HTTP examples, and Sendmux request JSON.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
