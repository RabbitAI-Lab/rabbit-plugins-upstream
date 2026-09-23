## Description:

Use to look up, search, and manage Google Contacts and Google People API data, including personal contacts, Workspace directory users, profile fields, relations, and raw People API queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and Google Workspace users use this MCP server to let an agent search Contacts and People API data, inspect Workspace directory relationships, and manage personal contacts through gogcli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can persist Google OAuth credentials and access Google Contacts or Workspace directory data.

Mitigation: Install only for trusted environments, use a least-privilege Google account and OAuth scopes, and avoid shared or weakly protected file-keyring deployments.

Risk: Contact update, delete, and dedupe apply tools can make destructive changes without their own confirmation gate.

Mitigation: Require client-side approval before invoking delete, update, dedupe apply, or raw run tools; use GOG_READONLY=1 for lookup-only use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration]

**Output Format:** [MCP tool responses with text or JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires gogcli authentication and may access Google Contacts and Workspace directory data for the configured account.]

## Skill Version(s):

4.2.5 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
