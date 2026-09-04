## Description:

outlook-mcp is a production-grade MCP server that gives agents typed Microsoft Graph tools for personal Outlook mail, calendar, contacts, to-do, drafts, attachments, folders, threading, batch operations, and delta sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to connect MCP-compatible agents to personal Outlook accounts for reading, triaging, drafting, sending, scheduling, contact management, task management, and attachment workflows. It is intended for Outlook.com, Hotmail, and Live accounts with a user-provided Azure app registration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can access and change personal Outlook data, including mail, calendar items, contacts, tasks, folders, drafts, and attachments.

Mitigation: Install only for intended personal Outlook accounts, start with read_only: true, and enable only the allow_categories required for the agent workflow.

Risk: Attachment tools may expose or modify local files if broad paths are made available to the agent.

Mitigation: Restrict attachment operations to narrow, expected file paths and review attachment-related tool calls before enabling write workflows.

Risk: Token storage may be weaker on Linux hosts without encrypted keyring support.

Mitigation: Confirm encrypted Secret Service or equivalent keyring support before authenticating on Linux.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Project repository](https://github.com/mpalermiti/outlook-mcp)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)
- [MCP Registry listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti)
- [OpenClaw MCP documentation](https://docs.openclaw.ai/cli/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration; MCP tools return structured Outlook data and operation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes typed tool schemas, optional concise responses for high-volume reads, read-only mode, category-based permissions, and structured Microsoft Graph error guidance.]

## Skill Version(s):

1.13.0 (source: evidence release, pyproject.toml, server.json, CHANGELOG; released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
