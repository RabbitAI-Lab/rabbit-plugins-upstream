## Description:

Use when the user asks to look up, search, or manage Google Contacts and the broader People API (Workspace directory).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this MCP server to let an assistant search, read, create, update, export, deduplicate, and delete Google Contacts, and query Google Workspace People API profile, directory, and reporting relationship data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad contact and authentication controls, including tools that can create, update, delete, export, deduplicate, and run escape-hatch Google Contacts commands.

Mitigation: Review the full manifest tool list before installing, restrict use to trusted agents and accounts, and use GOG_READONLY=1 for read-only workflows.

Risk: A configured remote runner can receive command requests and may receive token-backed access.

Mitigation: Set GOG_RUNNER_URL only to a runner you trust, or leave it unset to use the local gog executable.

Risk: The main skill documentation under-describes the full tool set compared with the manifest.

Mitigation: Review the manifest and security summary before deployment so users understand both read-only and destructive capabilities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [MCP tool responses as text, JSON, vCard export data, and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires gogcli, Node.js 18 or later, and an authenticated Google account with Contacts and People API access.]

## Skill Version(s):

2.29.0 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
