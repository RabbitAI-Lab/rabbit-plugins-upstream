## Description:

Notion MCP integration with managed authentication for querying databases, creating and updating pages, and managing blocks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a user-approved Notion workspace, search and fetch workspace content, and perform approved content or database updates. It is suited for Notion workflows that need managed authentication through Maton instead of direct credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access selected Notion workspace content through Maton, including pages, databases, comments, users, and team information.

Mitigation: Install only when comfortable authorizing Maton for the selected workspace, prefer OAuth, choose the narrowest available Notion scopes, and avoid collecting or storing data beyond the immediate task.

Risk: Write operations can create or change pages, comments, databases, data-source schemas, moves, deletions, and raw passthrough API calls.

Mitigation: Require a clear confirmation step before page edits, schema changes, comments, moves, deletions, or passthrough calls, including the target resource and intended payload.

Risk: Long-lived Maton API keys can be exposed if printed, stored improperly, or inherited by child processes.

Mitigation: Prefer OAuth through the Maton CLI, avoid MATON_API_KEY unless the CLI is unavailable, and rotate the key if it is ever printed or stored improperly.

Risk: The external Maton CLI or SDK is part of the execution path.

Mitigation: Verify the Maton package source and version before installation or use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate authenticated Notion MCP API calls that return workspace content, page metadata, comments, users, teams, IDs, URLs, and operation results.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
