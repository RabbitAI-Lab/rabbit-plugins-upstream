## Description:

Connects an agent to Tempo for time tracking, resource planning, and timesheet management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo users and developers can ask an agent to review worklogs, plans, teams, accounts, and timesheet approvals, or to make authorized changes to them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A privileged Tempo token may expose coworker worklogs, teams, accounts, projects, and approval data.

Mitigation: Use a least-privilege token where possible and review access to sensitive data before using the skill.

Risk: A leaked Tempo API token could grant access to time-tracking data.

Mitigation: Keep the token out of shared repositories and chats; rotate it if exposed.

Risk: Create, update, delete, and timesheet approval actions can change or remove records.

Mitigation: Review the action preview and confirm only intended changes, especially deletions and approval decisions.

## Reference(s):

- [Tempo API MCP on ClawHub](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [Tempo API MCP npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Conversational text or Markdown, with configuration examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the connected Tempo account's permissions.]

## Skill Version(s):

3.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
