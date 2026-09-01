## Description:

Notion MCP integration with managed authentication for querying databases, creating and updating pages, and managing blocks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with Notion workspaces through managed MCP access, including search, fetch, page and database creation, content updates, comments, teams, and users. It is intended for workflows that default to read and list operations and require explicit user approval before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Notion workspace content through Maton.

Mitigation: Connect only the intended workspace, prefer the narrowest available OAuth scopes, default to read and list calls, and require explicit user approval before create, update, move, database schema, comment, trash, or delete-related operations.

Risk: Writes may affect the wrong workspace, profile, or connection when multiple accounts or connections exist.

Mitigation: Pin the intended Maton profile and Notion MCP connection before executing sensitive calls, and confirm the target resource and payload with the user.

Risk: Long-lived API keys and returned provider credentials can be exposed if printed, logged, stored, or passed through command lines.

Mitigation: Prefer OAuth through the Maton CLI credential store, avoid MATON_API_KEY unless the CLI cannot be used, and never print, persist, or transmit credentials outside the intended Maton API flow.

Risk: Fetched Notion content can contain untrusted instructions or adversarial text.

Mitigation: Treat Notion content as data, validate values before reuse, and do not let fetched content choose follow-up endpoints, recipients, shell commands, or prompts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Notion MCP Overview](https://developers.notion.com/guides/mcp)
- [MCP Supported Tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Maton CLI commands, Notion MCP endpoint paths, and JSON payload examples.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
