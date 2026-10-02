## Description:

Helps agents search and manage Google Contacts, inspect People profiles, and search the Google Workspace directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent can look up personal contacts or Workspace directory entries, inspect profiles and relations, and manage contacts through an authenticated Google account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector has ongoing access to Google Contacts and People data.

Mitigation: Install only when this access is acceptable; use GOG_READONLY=1 for lookup-only workflows.

Risk: Some delete and merge actions may proceed without enforced user confirmation.

Mitigation: Manually confirm delete and dedupe-apply requests before the agent calls a tool; preview duplicate merges first.

Risk: Contact exports can write personal information to local files, and authentication changes affect account access.

Mitigation: Restrict GOG_FILE_ROOTS and manually confirm exports and authentication changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol documentation](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [MCP tool responses with contact or directory data; optional vCard (.vcf) exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain personal contact and directory information.]

## Skill Version(s):

4.6.0 (source: ClawHub release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
