## Description:

Helps agents search and manage Google Contacts and look up Google Workspace directory profiles and relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent with an authorized Google account can find personal contacts, search a Workspace directory, inspect profiles and relationships, and manage contacts when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to personal contacts and Workspace profiles may expose sensitive personal information.

Mitigation: Use a narrowly scoped Google account and enable GOG_READONLY=1 unless contact changes are needed.

Risk: Additional tools can delete or change contacts, including actions without enforced confirmation.

Mitigation: Review agent actions involving delete, dedupe, batch update, export, or run tools before allowing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Contact and directory results as text or JSON; contact exports as vCard files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Google account; available data depends on account permissions.]

## Skill Version(s):

4.7.0 (source: server release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
