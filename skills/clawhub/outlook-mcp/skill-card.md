## Description:

outlook-mcp gives agents typed Microsoft Graph tools for personal Outlook mail, calendar, contacts, tasks, drafts, attachments, folders, threading, batch operations, and delta sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use outlook-mcp to connect MCP-compatible agents to personal Microsoft Outlook accounts for reading, triaging, drafting, sending, scheduling, contact management, task management, and recurring inbox or calendar workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Token-handling risks could expose a user's Microsoft account access.

Mitigation: Review before installing and require encrypted token storage on Linux via libsecret or gnome-keyring, or use an explicit opt-in before authenticating.

Risk: Delta-sync tools or untrusted stored delta tokens may rely on cursor or nextLink URLs before validation is complete.

Mitigation: Avoid delta-sync tools and untrusted stored delta tokens until cursor and nextLink URLs are validated against graph.microsoft.com.

Risk: Broad write permissions can let an agent send email, modify calendars, edit contacts or tasks, and move or delete messages.

Mitigation: Use a least-privilege Azure app, start with read_only true, and restrict allow_categories before enabling write tools.

Risk: Known dependency vulnerabilities may affect broad deployments.

Mitigation: Update vulnerable dependencies before broad use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Publisher Profile](https://clawhub.ai/user/mpalermiti)
- [Repository](https://github.com/mpalermiti/outlook-mcp)
- [PyPI Package](https://pypi.org/project/outlook-graph-mcp/)
- [MCP Registry Listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti)

## Skill Output:

**Output Type(s):** [Text, Files, API Calls, Guidance]

**Output Format:** [Structured MCP tool responses with text summaries and JSON-like fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform Microsoft account actions and save attachments inside the configured attachments directory.]

## Skill Version(s):

1.20.0 (source: release evidence, CHANGELOG, pyproject.toml, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
