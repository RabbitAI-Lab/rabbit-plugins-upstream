## Description:

Notion MCP lets agents access Notion through Maton-managed authentication to search databases, fetch workspace content, create and update pages, manage blocks, and run user-approved Notion automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform user-approved Notion workspace operations through MCP, starting with read/list queries and confirming writes, new connections, and automation setup before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's Notion workspace through a Maton connection.

Mitigation: Install only when the user is comfortable granting Maton access, begin with read/list calls, and confirm each write or new connection before execution.

Risk: Hosted functions, triggers, destinations, and local --exec watching can turn a Notion connection into ongoing automation.

Mitigation: Use automation only for a specific user-approved task, scope it narrowly, prefer DENY_ALL network policy for functions where applicable, and remove automation when it is no longer needed.

Risk: Raw HTTP or API key workflows can expose long-lived credentials if used casually.

Mitigation: Prefer OAuth through the Maton CLI; use raw HTTP or API keys only where the CLI cannot be installed and keep credentials out of logs and child processes.

## Reference(s):

- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, Python snippets, and Notion action schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and raw HTTP instructions for Notion MCP operations; Notion responses may contain workspace or personal data and should be minimized to the task.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
