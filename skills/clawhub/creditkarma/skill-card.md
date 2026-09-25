## Description:

Access Credit Karma transaction data through creditkarma-mcp to sync transactions locally and query spending, merchants, categories, account summaries, and read-only SQL results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to creditkarma-mcp, sync personal Credit Karma transactions into a local SQLite database, and answer spending or account-summary questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide live Credit Karma session cookies to an MCP server.

Mitigation: Use only if comfortable granting that access, avoid placing full cookie headers in shared project configs, and prefer an official authentication method if one becomes available.

Risk: The MCP server stores sensitive financial transaction data locally.

Mitigation: Keep local session and database files protected, remove session files when finished, and review the skill carefully before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, bash, SQL examples, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires creditkarma-mcp setup, Credit Karma session access, and local SQLite transaction sync before querying.]

## Skill Version(s):

3.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
