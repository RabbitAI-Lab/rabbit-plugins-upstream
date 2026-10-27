## Description:

Access Splitwise expense, group, friend, and balance data, and manage shared expenses through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to review Splitwise balances and expense history, manage groups, or create and update shared expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can access private Splitwise data using an API key.

Mitigation: Protect the API key and avoid exposing it in prompts, logs, or shared configuration.

Risk: Expense and group changes affect shared account records.

Mitigation: Keep confirmation mode set to ask-user and verify the target group, participants, and amounts in each preview before approval.

Risk: Receipt handling may involve a hosted receipt server.

Mitigation: Trust the hosted receipt server before using receipt features.

Risk: An unpinned package version can change between installations.

Mitigation: Consider pinning the package version.

## Reference(s):

- [splitwise-mcp package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)
- [Project repository linked in the skill](https://github.com/chrischall/splitwise-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Natural-language responses and Splitwise data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, edit, or delete shared expense and group records after user approval.]

## Skill Version(s):

3.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
