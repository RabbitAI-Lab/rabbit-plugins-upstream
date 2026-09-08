## Description:

Manage Sendmux domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to guide Sendmux account-management workflows across domains, mailboxes, mailbox keys, sending accounts, webhooks, billing, logs, and metrics. It helps agents choose between MCP tools, CLI commands, and SDK examples while preserving secret-handling and confirmation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports sensitive Sendmux account-administration workflows, including root-key setup and generated mailbox or webhook secrets.

Mitigation: Use scoped tokens where possible, keep root keys out of chat, and store generated mailbox keys or webhook secrets only in the user's chosen secret store.

Risk: The skill can guide destructive or disruptive account actions such as deleting resources, suspending or resuming mailboxes, rotating secrets, or testing delivery.

Mitigation: Confirm the target resource and user intent before delete, suspend, resume, rotate-secret, and test-delivery operations.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-management)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with command tables, bash examples, TypeScript examples, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Sendmux API credentials when the user provides them through an appropriate environment or secret store.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
