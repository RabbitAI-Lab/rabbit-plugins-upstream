## Description:

Access Tempo time-tracking data via MCP for worklogs, plans, teams, accounts, resource allocations, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo users use this skill to connect an agent to Tempo so it can retrieve time-tracking data, manage worklogs and plans, and handle timesheet approval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Tempo token may allow access to or modification of team and coworker time data when the account has those permissions.

Mitigation: Use a least-privileged Tempo token and review team, account, delete, and approval actions before allowing them to run.

Risk: The bundled terms section understates the possibility of broader Tempo access through account permissions.

Mitigation: Do not rely on self-only access claims; treat all reachable Tempo data as governed by the token's actual permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact or full views; write actions use confirmation previews or receipts.]

## Skill Version(s):

3.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
