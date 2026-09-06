## Description:

outlook-mcp provides AI agents with a typed MCP server for personal Outlook accounts, covering mail, calendar, contacts, tasks, drafts, attachments, folders, threading, batch operations, and delta sync through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect AI agents to personal Outlook accounts for reading, triaging, drafting, sending, scheduling, contact management, task management, and recurring mailbox or calendar sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user-supplied delta-sync cursor can cause a Microsoft bearer token to be sent to an arbitrary URL.

Mitigation: Do not allow arbitrary or user-authored delta_token values; require delta-token URLs to stay on graph.microsoft.com before enabling delta-sync workflows.

Risk: Write-capable categories can send email, delete items, change calendars, modify contacts, or alter tasks.

Mitigation: Start with read_only: true, then enable only the required allow_categories; avoid mail_send and delete-capable categories unless the agent workflow explicitly requires them.

Risk: Attachment tools read from and write to host file paths.

Mitigation: Use trusted absolute paths, review attachment_paths and save_path values, and restrict host filesystem access for agents that handle untrusted messages or attachments.

Risk: Installing from a moving source can expose users to unreviewed dependency or source changes.

Mitigation: Prefer trusted and pinned install sources for production use, and review the release evidence and security guidance before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Publisher profile](https://clawhub.ai/user/mpalermiti)
- [Project repository](https://github.com/mpalermiti/outlook-mcp)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)
- [MCP Registry listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti)
- [Artifact README](artifact/README.md)
- [Artifact SECURITY](artifact/SECURITY.md)
- [Artifact CHANGELOG](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Files, Configuration]

**Output Format:** [Structured JSON tool responses, status text, configuration snippets, and saved files for attachment downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool behavior depends on Microsoft Graph permissions, host authentication, read_only settings, allow_categories, and selected OUTLOOK_MCP_TOOLSETS.]

## Skill Version(s):

1.14.0 (source: release evidence, CHANGELOG, pyproject.toml, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
