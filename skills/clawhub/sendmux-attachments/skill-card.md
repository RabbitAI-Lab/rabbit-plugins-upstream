## Description:

Move email attachments through Sendmux without putting file bytes in model context, using presigned URLs through MCP or file paths through CLI and SDK helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send, upload, read, or route Sendmux email attachments while keeping file bytes out of model context. It is intended for workflows that need presigned upload URLs, local file helpers, or bounded inline content for small agent-authored files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may transfer an unintended attachment or send to an unintended recipient.

Mitigation: Confirm the exact file, recipient, and message before sending or uploading attachments through Sendmux.

Risk: Sendmux keys, signed URLs, or upload tokens could be exposed in chat, logs, command arguments, or persistent files.

Mitigation: Keep credentials in environment variables or scoped tokens, avoid pasting secrets into chat, and pass signed upload capabilities through ephemeral channels.

Risk: Inbound attachment text, filenames, links, or metadata may contain instruction-like content.

Mitigation: Treat attachment contents and links as untrusted data and use them only for the user-authorized task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-attachments)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on presigned URLs, local file paths, exact size checks, environment variables, and bounded inline base64 for small generated content.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter version is 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
