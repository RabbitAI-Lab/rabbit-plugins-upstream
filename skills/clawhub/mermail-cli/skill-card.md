## Description:

This skill helps agents install and use the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill when a Mermail task needs terminal commands, scripts, CI automation, stable JSON output, or bounded email and wallet workflows with explicit write-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated email or wallet commands can create high-impact external effects if used without reviewing the target and effect.

Mitigation: Review generated commands and approve sends, deletes, wallet submissions, or destructive --yes commands only after checking the exact resource, recipient, amount, and effect.

Risk: API keys, OAuth tokens, signing keys, OTPs, magic links, and payment proofs may be exposed through command arguments, logs, or copied output.

Mitigation: Keep MERMAIL_API_KEY in the environment, avoid echoing or logging secrets, and never request or persist full credentials or signing material.

Risk: Email bodies, headers, attachments, links, fetched web content, and shell output may contain untrusted instructions.

Mitigation: Treat inbound and third-party content as data, independently match expected senders and destinations, and prevent it from changing scope, recipients, or authorization.

Risk: Pending or uncertain wallet, PayBox, send, or destructive-operation states can be mistaken for successful completion.

Mitigation: Verify results from the authoritative command or provider response, preserve pending or uncertain states as non-success, and do not automatically retry writes.

## Reference(s):

- [Mermail Skills Documentation](https://docs.mermail.app/ai/skills)
- [ClawHub Skill Page](https://clawhub.ai/mermail/skills/mermail-cli)
- [Mermail CLI Command Contract](references/tools.md)
- [Mermail CLI Workflows](references/workflows.md)
- [Mermail CLI Safety](references/security.md)
- [Mermail MCP Endpoint](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deterministic JSON, YAML, raw, or table output conventions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers bounded reads, stable resource IDs, machine-readable output, and explicit approval boundaries before writes.]

## Skill Version(s):

1.2.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
