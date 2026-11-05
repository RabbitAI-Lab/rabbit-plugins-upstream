## Description:

Access Splitwise expense and group data via MCP. Use when the user asks about Splitwise expenses, groups, friends, or balances, or wants to add, edit, or delete expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using Splitwise can look up expenses, groups, friends, balances, and receipts, and manage shared expenses through natural-language requests. Developers configure the MCP server and Splitwise API key for the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Splitwise API key provides access to the connected account.

Mitigation: Protect the key and store it in a secret manager or environment configuration rather than exposing it in conversation.

Risk: Expense and account changes affect shared Splitwise data.

Mitigation: Review each change preview and approve it before the change is sent.

Risk: Hosted receipt uploads send the file before the later account-change confirmation.

Mitigation: Check the receipt contents and share only files intended for upload.

Risk: The bundled skill instructions do not independently verify security controls in the downloaded server.

Mitigation: Use a reviewed, pinned server version.

## Reference(s):

- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Project repository link in skill documentation](https://github.com/chrischall/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)

## Skill Output:

**Output Type(s):** [Guidance, API data, Configuration instructions]

**Output Format:** [Structured data and concise natural-language responses; Markdown configuration examples where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes require user confirmation; receipt retrieval may produce a file, image, PDF, or extracted PDF text.]

## Skill Version(s):

3.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
