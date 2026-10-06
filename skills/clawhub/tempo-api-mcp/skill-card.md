## Description:

Helps agents use Tempo to review and manage time tracking, resource plans, teams, accounts, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo users and their teams can ask an agent to inspect worklogs and plans, log time, and manage timesheet approvals within their granted permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Tempo token may expose or change colleagues' worklogs, plans, teams, accounts, and approvals, depending on its permissions.

Mitigation: Confirm actual Tempo/Jira permissions and obtain organizational approval before using the skill in a workplace instance.

Risk: Write actions can alter or delete time-tracking records or change timesheet approval status.

Mitigation: Review each proposed change and require explicit user confirmation before performing writes.

Risk: Installing the linked package and supplying a Tempo token grants software access to sensitive business data.

Mitigation: Install only if you trust the package and source, and protect the token from disclosure.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [tempo-api-mcp npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses based on Tempo tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and available actions depend on the token's Tempo and Jira permissions.]

## Skill Version(s):

3.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
