## Description:

Helps agents search and manage Google Contacts and query Google Workspace directory profiles and relationships through the People API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this skill to find personal contacts, search a Google Workspace directory, inspect profiles and reporting relationships, and manage contacts when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can access personal contacts and Workspace directory information.

Mitigation: Install only if you trust the server with this account access; use GOG_READONLY=1 for lookup-only work.

Risk: Deletion, deduplication, generic contacts commands, and batch changes may modify or remove contacts without strong confirmation.

Mitigation: Review the exact targets and requested changes before allowing destructive or bulk operations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text or JSON returned by MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain personal contact and Workspace directory information.]

## Skill Version(s):

4.6.3 (source: server release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
