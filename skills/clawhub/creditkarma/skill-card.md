## Description:

Accesses Credit Karma transaction data through an MCP server for syncing, filtering, and analyzing personal finance data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Credit Karma transaction data, sync local transaction history, and answer spending, merchant, category, account, and custom SQL questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP requires access to live Credit Karma session cookies and local transaction history.

Mitigation: Install only in an environment where that access is acceptable, and restrict filesystem access around the MCP.

Risk: CK_COOKIES, CKAT, and CKTRKID can function like passwords if exposed.

Mitigation: Store these values only in private configuration, avoid shared project files, rotate them if exposed, and prefer isolated runtime environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm Package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp Source](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy Extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, shell, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup guidance, transaction sync/query tool calls, and read-only SQL examples.]

## Skill Version(s):

2.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
