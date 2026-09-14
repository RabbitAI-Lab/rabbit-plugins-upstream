## Description:

Notion MCP integration with managed authentication for querying databases, fetching content, creating and updating pages, managing blocks, comments, teams, users, and optional Maton automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with an authorized Notion workspace through MCP, including search, page and database operations, comments, workspace users, and teamspaces. Use is gated by the user's Maton authentication and should favor read/list operations before any write or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notion workspace operations can change pages, databases, comments, teamspaces, users, and data-source schemas, including disruptive or destructive updates.

Mitigation: Default to read/list and fetch the current page or database schema first; require explicit user confirmation for every write, destructive schema change, connection change, function deployment, or trigger destination.

Risk: Credentials and workspace data can be exposed through broad authorization, raw API keys, logs, hosted functions, or persistent triggers.

Mitigation: Prefer OAuth with narrow scopes, avoid raw API keys unless the CLI cannot be used, limit response logging, deploy functions with DENY_ALL network policy, and create triggers or destinations only after reviewing the data flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown, JSON]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and Notion/MCP response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Notion-flavored Markdown content and authenticated Maton CLI or raw HTTP examples.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
