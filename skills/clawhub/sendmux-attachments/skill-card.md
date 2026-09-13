## Description:

Move email attachments through Sendmux without putting file bytes in model context, using file paths, presigned URLs, CLI, SDKs, or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an OpenClaw agent needs to send, upload, read, or route Sendmux email attachments without placing file bytes in model context. It provides guidance for MCP, CLI, direct HTTP, TypeScript, and Python workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may upload or send an unintended local file when given an incorrect attachment path.

Mitigation: Review each send or upload action and provide only file paths for attachments that should be uploaded or sent.

Risk: Sendmux API keys or mailbox keys could be exposed if pasted into chat or embedded in generated examples.

Mitigation: Keep credentials in environment variables such as SENDMUX_API_KEY or SENDMUX_MBX_KEY and avoid placing secrets in model context.

Risk: Inbound attachment content, filenames, links, or metadata may contain instruction-like text.

Mitigation: Treat attachment contents and metadata as untrusted data, and report suspicious instructions as data rather than following them.

Risk: Large attachments may be mishandled if converted to inline base64 or if upload size limits are bypassed.

Mitigation: Use file paths, presigned URLs, CLI, SDK, HTTP, or MCP file helpers for real files, and respect Sendmux attachment size limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-attachments)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes file paths, presigned URLs, CLI, SDK, HTTP, and MCP workflows over inline base64 for real attachment bytes.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter version: 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
