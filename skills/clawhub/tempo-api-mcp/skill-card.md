## Description:

Connect to Tempo through MCP to read and manage worklogs, resource plans, teams, accounts, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo and Jira users use this connector to review or update worklogs, resource plans, team and account data, and timesheet approvals. It supports reporting and time-tracking workflows through the Tempo API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The self-only access claim conflicts with documented tools for reading colleagues’ worklogs.

Mitigation: Verify the token’s actual permissions and use the narrowest access needed, preferably read-only for reporting.

Risk: The connector can make consequential changes, including hard-deleting worklogs and changing timesheet approvals.

Mitigation: Review each write preview and confirm its target and scope, especially for deletions and approvals.

Risk: The connector requires a Tempo API token, and the supplied documentation does not establish the external server’s runtime behavior.

Mitigation: Keep the token private and use a reviewed, pinned package version.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured Tempo responses and natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses can be compact or full; write operations require confirmation.]

## Skill Version(s):

3.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
