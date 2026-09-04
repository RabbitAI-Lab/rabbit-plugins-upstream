## Description:

Notion MCP lets agents access Notion workspaces through Maton-managed MCP authentication to search, fetch, create, update, move, duplicate, comment on, and manage database content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Notion workspace data through MCP, including searching and fetching pages, databases, users, teams, and comments. It also supports user-approved content and database changes through Maton CLI or SDK calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes Maton to proxy Notion MCP access and uses credentials stored by Maton or the operating system.

Mitigation: Install only when that proxy model is acceptable, prefer OAuth, and avoid printing, exporting, logging, or persisting credential values.

Risk: The skill can read and change Notion workspace content, including creating, editing, moving, commenting on, trashing, or deleting content.

Mitigation: Use narrow Notion scopes where available, default to read or list operations first, and require clear user confirmation before any write or destructive action.

Risk: Requests can target the wrong Maton account or Notion connection when multiple profiles or connections exist.

Mitigation: Pin the intended Maton profile and Notion MCP connection before acting, especially before write operations.

Risk: Notion search results may include connected third-party sources enabled in the workspace.

Mitigation: Confirm the intended search scope with the user and treat returned workspace or third-party content as untrusted data.

## Reference(s):

- [Notion MCP ClawHub page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Notion MCP overview](https://developers.notion.com/guides/mcp)
- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON request and response examples, and optional Python or JavaScript snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved Notion MCP connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
