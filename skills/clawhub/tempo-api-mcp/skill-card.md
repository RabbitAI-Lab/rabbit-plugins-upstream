## Description:

Connects an agent to Tempo time tracking for worklogs, resource plans, teams, accounts, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo users and authorized team reviewers use this skill to query worklogs and plans, log time, and manage timesheet approvals through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can access team or coworker-related data despite claiming it cannot access colleagues' entries.

Mitigation: Review before workplace installation; use team, reviewer, approval, or coworker worklog features only with organizational authorization.

Risk: A leaked Tempo token could expose time-tracking data or permit changes.

Mitigation: Use the least-privileged token available and never commit or share it.

Risk: Writes can change timesheets and worklogs; deleted worklogs cannot be restored.

Mitigation: Confirm every write preview carefully and treat worklog deletion as irreversible.

## Reference(s):

- [ClawHub tempo-api-mcp release](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [tempo-api-mcp npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Markdown responses and structured Tempo data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results default to compact view, which removes image fields; full view preserves the upstream response. Writes return confirmation previews or receipts.]

## Skill Version(s):

3.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
