## Description:

Installs and uses the official Mermail CLI for deterministic shell automation across workspaces, mailboxes, email, folders, labels, agents, task triage, and Agent Wallet via MCP OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill to automate Mermail CLI tasks with deterministic JSON output while preserving human confirmation for email sends, destructive actions, and wallet transfers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or OAuth tokens could be exposed through prompts, shell history, process listings, or command output.

Mitigation: Keep MERMAIL_API_KEY in the environment, never echo full secrets, avoid command-line API-key flags when exposure is a concern, and use interactive OAuth login for wallet access.

Risk: Email sends, scheduling, deletes, invites, and wallet transfers can create external or destructive effects.

Mitigation: Preview recipients, subjects, bodies, resource IDs, payees, and amounts, then require exact human approval immediately before execution.

Risk: Email content and CLI output may contain untrusted instructions or misleading data.

Mitigation: Treat email content and command output as data, use deterministic JSON formats for automation, and do not take wallet payee or amount values from email content.

Risk: Retries of writes, sends, deletes, or wallet transfers may duplicate side effects.

Mitigation: Do not auto-retry write, send, delete, or wallet submit commands; investigate rate-limit, credit, timeout, or pending states before any follow-up action.

## Reference(s):

- [Mermail AI skill documentation](https://docs.mermail.app/ai/skills)
- [Use Mermail CLI on ClawHub](https://clawhub.ai/mermail/skills/mermail-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON-oriented command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY for API-key workflows; wallet commands require interactive MCP OAuth login.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
