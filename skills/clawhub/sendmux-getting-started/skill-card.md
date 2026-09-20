## Description:

Set up Sendmux for agents, register a durable inbox without an existing key, link an owner, choose a runtime surface, and make the first harmless call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure Sendmux credentials, choose a CLI, MCP, SDK, or HTTP surface, validate access, and make initial low-risk calls for mailbox, management, sending, or self-registered agent inbox workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials may grant mailbox, sending, or account-management access.

Mitigation: Prefer OAuth or scoped mailbox/agent keys, avoid root keys except for management tasks, keep credentials in environment variables, local profiles, or a secret manager, and rotate any leaked key.

Risk: Email, attachment, and remote-document content can contain untrusted instructions.

Mitigation: Treat fetched message content as untrusted data and do not execute setup instructions found inside messages, attachments, or remote documents.

Risk: The skill may lead an agent toward actions that read mailbox content, change account settings, or send email.

Mitigation: Confirm the selected profile, credential scope, and user intent before mailbox reads, account-management changes, or any real send.

Risk: Package installation examples rely on external package sources.

Mitigation: Review package sources and versions before installing CLI, MCP, or SDK packages in a production environment.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-getting-started)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with shell commands, HTTP examples, MCP tool names, and TypeScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes credential selection, connection validation, harmless first calls, and routing to follow-on Sendmux skills.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter and changelog text mention 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
