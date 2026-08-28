## Description:

Accesses Splitwise expense, group, friend, balance, and receipt data through the splitwise-mcp MCP server, including expense and group-management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Splitwise expenses, groups, friends, balances, and receipts, and to create or modify Splitwise expenses and group membership after configuring the splitwise-mcp server with a Splitwise API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, edit, delete, or restore Splitwise expenses and can change group membership.

Mitigation: Configure the agent to ask for explicit confirmation before financial or group-management actions.

Risk: The MCP server requires a Splitwise API key that is attached to requests.

Mitigation: Install only from a trusted package source and store the key in the MCP environment rather than in prompts or shared files.

Risk: Receipt retrieval can expose receipt contents or write receipt files to the server filesystem.

Mitigation: Use inline receipt viewing, PDF text extraction, or a controlled output directory when handling receipts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with MCP tool calls, JSON configuration snippets, shell commands, and optional receipt file paths or inline receipt content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SPLITWISE_API_KEY; receipt retrieval can return inline bytes or text, or write files to a configured output directory.]

## Skill Version(s):

2.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
