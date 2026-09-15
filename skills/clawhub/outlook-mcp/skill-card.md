## Description:

Outlook MCP is a production-grade MCP server that gives agents typed access to personal Outlook mail, calendar, contacts, tasks, drafts, attachments, folders, threading, batch operations, and delta sync through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use Outlook MCP to connect MCP clients to personal Outlook accounts for email triage, calendar coordination, contacts, tasks, drafts, and attachment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install metadata includes an unpinned GitHub clone while the server can receive broad personal Outlook access.

Mitigation: Prefer the declared PyPI package or a pinned release instead of installing mutable source.

Risk: Agents may receive mailbox, calendar, contact, task, attachment, and send-mail authority.

Mitigation: Install only when that access is acceptable, start with read_only enabled, and use a separately consented read-only Azure app when a Microsoft-enforced read-only credential is required.

Risk: Attachment tools interact with local files through the configured attachment directory.

Mitigation: Keep attachments_dir narrow and dedicated to files intended for Outlook attachment workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Repository](https://github.com/mpalermiti/outlook-mcp)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)
- [MCP Registry listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti)

## Skill Output:

**Output Type(s):** [Text, API Calls, Shell commands, Configuration]

**Output Format:** [Structured MCP tool responses with Markdown setup guidance and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include Outlook content and actions across mail, calendar, contacts, tasks, drafts, folders, attachments, and batch workflows.]

## Skill Version(s):

1.22.0 (source: release evidence, CHANGELOG.md, pyproject.toml, server.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
