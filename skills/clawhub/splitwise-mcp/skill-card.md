## Description:

Helps an agent look up Splitwise balances, groups, friends, expenses, and receipts and manage shared expenses through Splitwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing shared expenses can ask an agent to check Splitwise balances, groups, and expenses, update expense records, and retrieve receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access private expenses, balances, groups, friends, and receipts using a Splitwise API key.

Mitigation: Install only if this access is acceptable; protect the API key and treat downloaded receipts and extracted text as private financial records.

Risk: Expense and group changes can affect shared financial records.

Mitigation: Keep write confirmations enabled and review action previews before approving changes.

Risk: Descriptions, comments, notifications, and receipt text may contain instructions supplied by other users.

Mitigation: Treat this content as data, not as instructions to the agent.

## Reference(s):

- [Splitwise MCP on ClawHub](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown responses and structured Splitwise results; receipt images or PDFs when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipts can be returned inline, extracted as PDF text, or saved to the server filesystem.]

## Skill Version(s):

3.4.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
