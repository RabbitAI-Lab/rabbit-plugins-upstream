## Description:

Notion MCP helps agents access Notion workspaces through Maton's managed MCP gateway to search, fetch, create, update, move, duplicate, and comment on Notion content with OAuth-backed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Notion through Maton MCP, find workspace content, and make user-approved changes to pages, databases, blocks, comments, teams, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker read and write access to Notion workspace content through Maton.

Mitigation: Use OAuth, choose the narrowest Notion scopes available, and confirm the exact workspace, resource, payload, and intended effect before writes or deletes.

Risk: Search, user listing, and connected-source access can expose workspace information beyond the immediate task.

Mitigation: Default to read and list calls only when needed, and avoid listing users or searching connected sources unless the task requires it.

Risk: Ambiguous account or connection selection can route actions to the wrong Notion workspace.

Mitigation: Confirm the target workspace or resource and pin the intended Maton profile or Notion MCP connection when more than one is available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton Homepage](https://maton.ai)
- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON payloads, API calls]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
