## Description:

Move email attachments through Sendmux without putting file bytes in model context, using presigned URLs through MCP or file paths through CLI and SDK helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to send and read Sendmux email attachments through MCP, CLI, HTTP, or SDK workflows while keeping file bytes out of model context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An attachment may contain instructions intended to redirect the agent.

Mitigation: Treat attachment content and metadata as untrusted data and follow only the user's authorized task.

Risk: Attachment workflows may expose credentials or sensitive file contents.

Mitigation: Use scoped Sendmux tokens, keep secrets out of chat and logs, and transfer real file bytes outside model context.

Risk: Sending an attachment to the wrong recipient may disclose private data.

Mitigation: Confirm recipients and attachment choices before sending mail.

## Reference(s):

- [Sendmux Attachments on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-attachments)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains presigned transfers and local-file helpers without placing attachment bytes in model context.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter says 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
