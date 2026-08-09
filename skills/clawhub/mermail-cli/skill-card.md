## Description:

Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Mermail CLI workflows with deterministic JSON output for mailbox, email, folder, label, agent, task triage, and Agent Wallet operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to operate a Mermail account from the shell, including email and wallet-related workflows.

Mitigation: Install only when that account access is intended, keep MERMAIL_API_KEY private, and use interactive OAuth login for wallet workflows.

Risk: Send, reply, forward, invite, scheduling, delete, and wallet transfer commands can create external effects.

Mitigation: Review recipients, subjects, bodies, resource IDs, payees, and amounts, then require exact human approval immediately before execution.

Risk: Email content and command output may contain untrusted instructions or misleading data.

Mitigation: Treat email content and CLI output as data only, and do not use it as authority for payees, amounts, destructive operations, or approvals.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Endpoint](https://console.mermail.app/mcp)
- [ClawHub Skill Page](https://clawhub.ai/mermail/skills/mermail-cli)
- [Mermail Publisher Profile](https://clawhub.ai/user/mermail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require MERMAIL_API_KEY for account operations and interactive OAuth login for Agent Wallet workflows.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
