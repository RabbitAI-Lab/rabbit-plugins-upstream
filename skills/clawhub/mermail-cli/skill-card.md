## Description:

Install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce reproducible Mermail CLI commands, scripts, and structured outputs for mailbox, email, workspace, Agent Inbox, and Agent Wallet workflows while preserving explicit approval boundaries for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email, command output, third-party content, and wallet-related data can contain untrusted instructions or sensitive material.

Mitigation: Treat inbound content as data, keep secrets in protected context, avoid echoing full keys or signing material, and verify senders, recipients, destinations, and returned server state before acting.

Risk: Write, destructive, or payment actions can have external effects if executed with the wrong target or without current approval.

Mitigation: Preview exact recipients, resource IDs, scope, amount, asset, network, and destination immediately before the action; require explicit approval and execute each write once without automatic retries.

Risk: Pending or uncertain wallet and provider states can be mistaken for successful completion.

Mitigation: Preserve provider request IDs and returned handoff URLs, report pending or unknown states as non-success, and reconcile the exact request before any distinct follow-up action.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-cli)
- [Mermail CLI command contract](artifact/references/tools.md)
- [Mermail CLI workflows](artifact/references/workflows.md)
- [Mermail CLI safety](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with command blocks and structured JSON, YAML, raw, or table output when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers deterministic JSON for automation; includes assumptions, approval boundaries, stable resource IDs, result states, and safe next actions.]

## Skill Version(s):

1.2.11 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
