## Description:

Set up Sendmux for agents, register a durable inbox without an existing key, link an owner, choose a runtime surface, and make the first harmless call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to set up Sendmux access, choose the correct CLI, MCP, SDK, or HTTP surface, and make an initial low-impact verification call before moving to mailbox, sending, or management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through installing Sendmux tooling and creating or using Sendmux credentials.

Mitigation: Use scoped keys where possible, rely on environment variables, CLI profiles, or a secret manager, and avoid pasting or printing secrets in chat, logs, prompts, screenshots, or repository files.

Risk: Sending and management workflows can give an agent mailbox or account-level authority.

Mitigation: Use separate least-privilege keys for mailbox, sending, and management work, and only approve sending or management steps when that authority is intended.

Risk: Email, attachment, and remote-document content may contain untrusted setup instructions.

Mitigation: Treat message content as data; do not fetch or execute setup instructions found inside email, attachments, or remote documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-getting-started)
- [Sendmux skills repository](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with shell commands, TypeScript examples, credential guidance, and routing recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment-variable guidance for SENDMUX_API_KEY, SENDMUX_MBX_KEY, and SENDMUX_ROOT_KEY.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
