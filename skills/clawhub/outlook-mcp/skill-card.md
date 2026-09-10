## Description:

Production-grade MCP server for personal Outlook (Outlook.com / Hotmail / Live) with 62 typed Microsoft Graph tools across mail, calendar, contacts, to-do, drafts, attachments, folders, threading, batch operations, and delta sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to connect MCP-compatible agents to personal Outlook accounts for mailbox triage, message drafting and sending, calendar management, contacts, tasks, attachments, folders, and recurring digest workflows. It is intended for personal Microsoft accounts and requires the user to bring their own Azure app registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Microsoft account tokens could be exposed if host credential storage falls back to plaintext or the server runs on a machine with sensitive local access.

Mitigation: Review the installation before use, avoid running it on hosts with unnecessary sensitive files, and ensure encrypted OS credential storage is available before authenticating.

Risk: Write-capable tools can send email or modify Outlook data when enabled.

Mitigation: Start with read_only:true, enable only required write categories with allow_categories, and require human approval for mail_send and other high-impact actions.

Risk: Attachment tools can read local files for outgoing attachments or write downloaded attachments to paths on the host.

Mitigation: Limit OUTLOOK_MCP_TOOLSETS to the needed groups and avoid enabling attachment or draft-attachment tools for autonomous agents unless the host filesystem exposure is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [README](artifact/README.md)
- [Security policy](artifact/SECURITY.md)
- [MCP server manifest](artifact/server.json)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)
- [MCP Registry listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Structured MCP tool responses and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-visible tools can read, write, triage, and organize Outlook mail, calendar events, contacts, tasks, drafts, attachments, folders, threads, and batch operations through Microsoft Graph.]

## Skill Version(s):

1.19.0 (source: release evidence, pyproject.toml, CHANGELOG, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
