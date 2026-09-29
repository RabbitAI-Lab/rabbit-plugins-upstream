## Description:

Helps agents search and manage Notion workspaces through MCP with managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Notion users can search workspace content and create or update pages, databases, and comments through an authorized connection. Optional functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notion writes and new connections can change or expose workspace content.

Mitigation: Default to read operations; obtain explicit approval for each write or new connection.

Risk: Hosted functions and triggers can continue acting after the initial request.

Mitigation: Approve each function, trigger, destination, and event handler separately; remove persistent automation when no longer needed.

Risk: API keys and event data may be exposed through credentials or third-party destinations.

Mitigation: Prefer OAuth login; approve any external destination only after reviewing what data it receives and how often.

## Reference(s):

- [Notion MCP overview](https://developers.notion.com/guides/mcp)
- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Notion event triggers](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with commands and Notion results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notion operations require an authorized connection and network access.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
