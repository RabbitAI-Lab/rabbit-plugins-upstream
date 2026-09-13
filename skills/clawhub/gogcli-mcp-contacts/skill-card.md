## Description:

Looks up, searches, and manages Google Contacts and Google People API Workspace directory data through a gogcli-backed MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and MCP users use this skill to connect an agent to Google Contacts and the People API for contact lookup, Workspace directory search, profile fields, manager or reports relations, and contact management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose read and management access to Google Contacts and People data.

Mitigation: Install only when that access is needed, pin the package version, and use GOG_READONLY=1 when possible.

Risk: Underdocumented destructive contact tools may delete contacts or apply deduplication changes.

Mitigation: Require explicit review of the exact Google account and resources before delete, dedupe with apply, export, or generic gog subcommand use.

Risk: A configurable remote runner can forward Google tokens outside the local environment.

Mitigation: Avoid setting GOG_RUNNER_URL unless the endpoint is controlled and trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, files, configuration]

**Output Format:** [MCP tool results, including text, JSON, and vCard export content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the configured Google account, People API permissions, selected gogcli command, and optional pagination or export arguments.]

## Skill Version(s):

2.29.1 (source: release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
