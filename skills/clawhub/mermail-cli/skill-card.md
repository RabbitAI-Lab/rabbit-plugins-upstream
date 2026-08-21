## Description:

Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to install and run the official Mermail CLI for reproducible workspace, mailbox, email, Agent Inbox, and Agent Wallet workflows when shell commands, scripts, CI steps, or stable machine-readable output are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email and wallet actions can create high-impact external effects such as sends, deletes, transfers, swaps, or x402 payments.

Mitigation: Preview exact recipients, resource IDs, amounts, assets, networks, destinations, and scopes, then require explicit approval immediately before each write.

Risk: Untrusted email bodies, headers, links, attachments, command output, or third-party content may try to redirect the workflow or authorize unintended actions.

Mitigation: Treat external content as data only; independently match expected senders, recipients, timestamps, and destinations before acting.

Risk: API keys, OAuth tokens, signing links, magic links, OTPs, signing keys, and payment proofs are sensitive secrets.

Mitigation: Keep secrets out of command arguments, logs, shell history, and persisted files; prefer environment variables, stdin, protected task-local context, and returned Mermail handoffs.

Risk: Pending, uncertain, rate-limited, or failed wallet and email operations can be mistaken for successful completion or retried unsafely.

Mitigation: Verify authoritative command or provider state, report pending or unknown states as non-success, and do not automatically retry writes.

## Reference(s):

- [Use Mermail CLI on ClawHub](https://clawhub.ai/mermail/skills/mermail-cli)
- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP Endpoint](https://console.mermail.app/mcp)
- [Mermail CLI Safety](references/security.md)
- [Mermail CLI Command Contract](references/tools.md)
- [Mermail CLI Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell command blocks and optional structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers deterministic JSON for automation and preserves approval boundaries for writes.]

## Skill Version(s):

1.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
