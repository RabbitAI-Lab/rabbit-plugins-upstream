## Description:

Set up Sendmux for agents, register a durable inbox without an existing key, link an owner, choose a runtime surface, and make the first harmless call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect an agent to Sendmux, select an appropriate credential and interface, optionally register an inbox, and verify access without sending an email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email and account credentials grant access beyond the setup check.

Mitigation: Use scoped mailbox or sending credentials where possible, avoid root keys outside management tasks, and keep secrets out of chat and logs.

Risk: Unpinned package install commands may fetch code from a source the user has not reviewed.

Mitigation: Review package sources before running installation commands.

Risk: Email, attachments, and linked documents can contain untrusted instructions.

Mitigation: Treat message content as data, not as setup or execution instructions.

## Reference(s):

- [Sendmux skills homepage (listed in skill metadata)](https://github.com/Sendmux/skills)
- [Sendmux Getting Started on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-getting-started)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credential selection, setup checks, and next-step routing]

## Skill Version(s):

1.0.9 (source: ClawHub release; source frontmatter states 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
