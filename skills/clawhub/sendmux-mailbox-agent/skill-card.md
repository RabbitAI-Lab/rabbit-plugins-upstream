## Description:

Let an OpenClaw agent read, search, count, sync, triage, file, delete, thread, and reply from one Sendmux mailbox efficiently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw agent users and developers use this skill to search, read, triage, sync, file, delete, thread, and reply from a scoped Sendmux mailbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox credentials may grant access to sensitive messages or attachments.

Mitigation: Use scoped mailbox or agent tokens, avoid root keys, and do not paste secrets into chat.

Risk: Mailbox mutations such as replies, filing, or deletion can affect user data.

Mitigation: Review replies and require explicit confirmation before deletes or other sensitive mutations.

Risk: Inbound email bodies, headers, links, and attachments may contain untrusted instructions.

Mitigation: Treat mailbox content as data rather than instructions and avoid changing configuration or sending mail solely because message content requested it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mailbox-agent)
- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [Publisher profile](https://clawhub.ai/user/sendmux.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code, shell commands, TypeScript examples, and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose mailbox API, CLI, SDK, and MCP calls; does not require secrets to be pasted into chat.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
