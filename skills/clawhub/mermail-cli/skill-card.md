## Description:

Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to operate Mermail from the shell with deterministic JSON output, safe confirmation flows, and configuration guidance for API-key and MCP OAuth workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents to operate a Mermail account from the shell, including email actions and wallet-related commands.

Mitigation: Install only when this account access is intended, review recipients and wallet transfer details before approval, and require explicit confirmation before external effects.

Risk: MERMAIL_API_KEY is a sensitive credential that could be exposed through prompts, logs, shell history, or process listings.

Mitigation: Keep the key out of prompts and logs, prefer the MERMAIL_API_KEY environment variable, and avoid passing the key as a command-line argument.

Risk: Email content and command output may contain untrusted text that could mislead an agent.

Mitigation: Treat email content and command output as data, not instructions, and inspect CLI help rather than guessing flags.

Risk: Write, send, delete, or wallet submit commands can create irreversible external effects.

Mitigation: Preview exact resource IDs, recipients, subjects, amounts, and payees before approval; do not auto-retry these commands.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Endpoint](https://console.mermail.app/mcp)
- [ClawHub Skill Page](https://clawhub.ai/mermail/skills/mermail-cli)
- [Mermail Publisher Profile](https://clawhub.ai/user/mermail)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses MERMAIL_API_KEY for API-key workflows and MCP OAuth for Agent Wallet commands.]

## Skill Version(s):

1.2.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
