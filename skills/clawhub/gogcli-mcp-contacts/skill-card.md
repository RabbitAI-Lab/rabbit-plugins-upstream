## Description:

Use when the user asks to look up, search, or manage Google Contacts and the broader People API, including Workspace directory search, profile fields, and manager or reports relations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and end users connect an agent to an authenticated Google account to search contacts, inspect People API profiles, query Workspace directory records, and manage contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and manage contacts for the selected Google account.

Mitigation: Install only for accounts where this access is acceptable, and prefer a dedicated or least-privileged Google account when possible.

Risk: Contact delete and dedupe apply actions can remove or merge contacts without an enforced separate confirmation token.

Mitigation: Use GOG_READONLY=1 for lookup-only use, preview dedupe plans before applying them, and review delete or merge requests before execution.

Risk: Export tools can write contact data to files.

Mitigation: Restrict allowed file directories with GOG_FILE_ROOTS and review requested output paths before exporting contacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli dependency](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, files, configuration]

**Output Format:** [MCP tool responses with contact records, diagnostics, raw People API JSON, and vCard export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reflect the selected Google account and can include contact mutations or exports when write-capable tools are used.]

## Skill Version(s):

4.5.0 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
