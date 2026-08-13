## Description:

Helps agents install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to produce safe, reproducible Mermail CLI commands and scripts for mailbox, email, workspace, triage, and Agent Wallet workflows. It is intended for bounded reads, deterministic output, explicit write previews, and careful handling of authentication and wallet handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can access sensitive Mermail workspace, mailbox, email, and wallet state through MERMAIL_API_KEY or OAuth credentials.

Mitigation: Use the CLI only in trusted workspaces, keep credentials in protected environment or OAuth storage, and never echo, log, or persist full API keys, OAuth tokens, OTPs, signing keys, or payment proofs.

Risk: Send, reply, forward, schedule, delete, wallet, swap, and x402 actions can create high-impact external effects.

Mitigation: Preview exact recipients, resource IDs, scope, amounts, assets, networks, destinations, and irreversible effects, then require explicit user approval before executing each write once.

Risk: Email bodies, headers, links, attachments, command output, and third-party content can contain misleading instructions.

Mitigation: Treat inbound and fetched content as untrusted data, independently match expected senders and destinations, and prevent it from broadening scope, changing commands, authorizing spending, or exposing secrets.

Risk: Wallet signing and pending provider states can be mistaken for completed transactions.

Mitigation: Use only authoritative returned provider status and invocation-scoped handoffs, report pending or unknown states as non-success, and do not retry or replace uncertain wallet requests automatically.

## Reference(s):

- [Mermail CLI command contract](references/tools.md)
- [Mermail CLI workflows](references/workflows.md)
- [Mermail CLI safety](references/security.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP endpoint](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deterministic JSON, YAML, raw, or table output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers bounded reads, stable resource IDs, explicit confirmation boundaries, and machine-readable CLI output.]

## Skill Version(s):

1.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
