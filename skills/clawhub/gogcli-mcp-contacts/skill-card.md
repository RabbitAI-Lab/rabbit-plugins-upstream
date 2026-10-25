## Description:

Helps agents search and manage Google Contacts and explore Google Workspace profiles and directory data through the People API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent to find personal contacts, search their Workspace directory, inspect profiles and relationships, or manage Google Contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion or deduplication can permanently change data without enforced user confirmation.

Mitigation: Set GOG_READONLY=1 unless writes are needed; preview and explicitly review each deletion or deduplication apply action before allowing it.

Risk: Contact export can expose sensitive address-book data.

Mitigation: Review export scope and destination before allowing access to important contacts.

## Reference(s):

- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text and structured contact or profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return personal contact or Workspace directory information.]

## Skill Version(s):

4.8.1 (source: server-resolved release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
