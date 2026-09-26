## Description:

Helps agents use Tempo through an MCP server to review worklogs and resource plans, log time, and manage permitted timesheet actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo users and authorized reviewers can query time entries and resource plans, log time, and manage timesheet approvals within their granted permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Tempo token may expose more team, account, and timesheet data than expected.

Mitigation: Review token permissions before installation, use a least-privilege token, and limit team-wide queries to authorized tasks.

Risk: Delete operations, account or team changes, and timesheet approval actions can affect other records.

Mitigation: Review the target and proposed changes, then obtain explicit confirmation before each write.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [Tempo API MCP npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration and command examples; Tempo tool results in text or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include worklogs, plans, team and account data, and timesheet status; changes require confirmation.]

## Skill Version(s):

3.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
