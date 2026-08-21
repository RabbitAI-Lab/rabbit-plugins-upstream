## Description:

Builds an 8-12 person influencer shortlist from a category, budget, and market, or from account links and handles the user already has.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external campaign teams use this skill to identify creators to approach for an influencer campaign or collaboration. It can work from pasted creator details or, with explicit confirmation, paid public profile and post lookups on supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses broad shared Beatra account authority, including spending credits and access beyond creator lookup.

Mitigation: Install only when that shared authority is acceptable, reconnect deliberately if scope is insufficient, and avoid private or regulated account data unless sending it through Beatra is acceptable.

Risk: Optional creator lookups are paid and can create charges for each confirmed page or operation.

Mitigation: Confirm each lookup separately, show the live operation price before execution, use one stable request identifier per paid request, and report net charged credits from returned billing fields.

Risk: The bundled client silently checks for and installs newer package code by default.

Mitigation: Disable automatic updates when explicit review of code changes is required, and use the documented update check command to inspect availability without replacement.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/influencer-fit-analyzer)
- [Beatra skill homepage](https://beatra.ai/skills/influencer-fit-analyzer)
- [Looking up creators](references/creator-lookup.md)
- [Writing the shortlist](references/shortlist.md)
- [Shortlist workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown shortlist memo with creator facts, fit rationale, talk-or-not recommendations, and lookup task or billing details when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup-derived figures should be labeled with read time; supplied figures should remain labeled as supplied; missing counts should not be estimated.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
