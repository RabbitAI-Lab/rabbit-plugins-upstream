## Description:

Notion MCP integration with managed authentication for searching, fetching, creating, and updating Notion workspace content through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to operate Notion workspaces through MCP with managed Maton authentication, including search, fetch, page and database creation, content updates, page moves, comments, users, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Notion workspace content through Maton, including create, update, move, duplicate, comment, and schema operations.

Mitigation: Prefer read and list operations first, use the narrowest available Notion scopes, and confirm the target resource, payload, and intended effect before any write or connection-changing action.

Risk: Maton API keys and provider-issued tokens are sensitive credentials.

Mitigation: Prefer OAuth and OS credential storage, avoid printing or persisting credentials, and do not route credentials to hosts other than Maton.

Risk: Fetched Notion content and connected-source search results may include untrusted instructions or sensitive workspace data.

Mitigation: Treat returned content as data, validate it before reuse, avoid executing or interpolating it into commands, and extract only the fields needed for the user task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [Notion MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and raw HTTP request guidance; Notion-flavored Markdown and JSON responses may contain workspace data.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
