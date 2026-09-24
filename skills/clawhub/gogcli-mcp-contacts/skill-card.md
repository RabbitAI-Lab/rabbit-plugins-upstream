## Description:

Use when the user asks to look up, search, or manage Google Contacts and the broader People API, including Workspace directory searches, profile fields, manager/reports relations, and contact lookups by name, email, or phone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and Google Workspace users use this MCP server to let an agent search, read, create, update, export, delete, and deduplicate Google Contacts and inspect People API directory and profile data through gogcli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Google Contacts and Workspace directory data.

Mitigation: Use a narrowly scoped Google account and grant only the Google services needed for the intended workflow.

Risk: The skill can create, update, export, delete, and deduplicate contacts, including delete or merge operations without a separate enforced confirmation step.

Mitigation: Set GOG_READONLY=1 for read-only use and manually review any delete, update, export, or dedupe request before allowing it to run.

Risk: Contact export can write vCard files to configured output paths.

Mitigation: Configure GOG_FILE_ROOTS to limit allowed file directories for exports and other file operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [Source repository](https://github.com/chrischall/gogcli-mcp)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [MCP tool responses, including text and JSON returned from gogcli commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Google Contacts and Workspace People API data; contact export can write vCard files when configured.]

## Skill Version(s):

4.3.0 (source: manifest.json, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
