## Description:

Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to compose safe Mermail CLI workflows for mailbox automation, email operations, JSON output, CI scripts, authentication checks, and Agent Wallet commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to operate sensitive email and wallet workflows from the shell.

Mitigation: Require human review of email sends, destructive commands, wallet transfer previews, and external effects before approval.

Risk: The skill depends on MERMAIL_API_KEY and OAuth sessions that can grant access to Mermail resources.

Mitigation: Keep API keys and OAuth sessions protected, avoid echoing secrets, and prefer environment variables over command-line key flags.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-oriented CLI command patterns, approval checkpoints, and environment-variable setup guidance.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
