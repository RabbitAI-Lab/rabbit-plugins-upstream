## Description:

Manage Sendmux domains, mailboxes, mailbox keys, sending accounts, webhooks, logs, billing, and account-level setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to guide Sendmux account management tasks, including domain setup, mailbox and key administration, sending-account configuration, webhook lifecycle work, logs, metrics, billing checks, and choosing between MCP, CLI, SDK, and HTTP surfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-privilege Sendmux management access can administer account resources, credentials, billing, providers, logs, and webhooks.

Mitigation: Use the least-privileged OAuth profile or API key that fits the task, validate Management access before resource reads, and keep root keys in a secret store.

Risk: Delete, suspend, resume, key creation or deletion, webhook secret rotation, billing, and provider changes can have destructive or sensitive effects.

Mitigation: Review those operations before execution, confirm target resources explicitly, and store one-time key or webhook-secret values only in the user's chosen secret store or secure output path.

## Reference(s):

- [Sendmux Skills Repository](https://github.com/Sendmux/skills)
- [sendmux-management ClawHub Page](https://clawhub.ai/sendmux.ai/skills/sendmux-management)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with CLI, SDK, MCP, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON command examples, TypeScript snippets, MCP tool names, scoped credential guidance, and confirmation prompts for high-impact operations.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
