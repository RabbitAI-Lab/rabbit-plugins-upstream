## Description:

Access Splitwise expense, group, friend, balance, receipt, notification, category, and currency data through an MCP server, including tools to create, edit, delete, and restore shared expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Splitwise users with a Splitwise API key use this skill to connect an agent to Splitwise for shared-expense, group, friend, balance, and receipt workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can read financial and social Splitwise account data and perform confirmed changes to expenses, groups, friends, comments, and profile fields.

Mitigation: Install only if this level of account access is acceptable, review changes before execution, pin the package version, and keep the Splitwise API key out of shared files.

Risk: Receipt handling can write downloaded files to the server filesystem or expose receipt bytes and PDF text through tool results.

Mitigation: Use inline:true, extract_text:true, write:false, or a dedicated SPLITWISE_OUTPUT_DIR when handling receipts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Source repository](https://github.com/chrischall/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, MCP tool calls, Configuration guidance, Files]

**Output Format:** [Markdown instructions with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Splitwise records, receipt file paths, inline receipt bytes, or extracted PDF text through the MCP server.]

## Skill Version(s):

2.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
