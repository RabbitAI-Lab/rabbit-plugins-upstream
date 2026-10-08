## Description:

Helps agents use Tempo through MCP to review time tracking, resource plans, teams, accounts, and timesheet approvals and to make authorized changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo/Jira users and their agents use this skill to review worklogs, allocations, and timesheet approvals, and to make authorized changes to time-tracking records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's personal-use description understates access to coworkers' worklogs, team data, and other-user timesheets when the token has broader permissions.

Mitigation: Review Tempo/Jira permissions before installation and use a least-privilege token; limit team, reviewer, account, plan, and approval access to what is needed.

Risk: Authorized write actions can change or delete time records and act on timesheet approvals.

Mitigation: Keep confirmation prompts enabled for writes and review each proposed action before approving it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [Tempo API MCP npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured Tempo tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations request confirmation before execution.]

## Skill Version(s):

3.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
