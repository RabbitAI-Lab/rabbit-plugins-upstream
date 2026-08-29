## Description:

Read Workday HR data such as org charts, worker profiles, tasks, pay, benefits, compensation, and app menus from a shell with the fpx CLI through the user's signed-in myworkday.com browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Workday users use this skill to retrieve selected Workday employee data from their own authenticated browser session without running the Workday MCP server. It supports scripting and shell-based inspection of read-only Workday data endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses fpx and the Transporter extension with the user's active Workday browser session.

Mitigation: Install only when that access pattern is acceptable, keep use user-directed and read-only, and treat exported Workday HR data as confidential.

Risk: Raw Workday response envelopes can include session-related fields and confidential HR, pay, or benefits data.

Mitigation: Avoid raw JSON dumps and use the provided field-selecting jq filters so only intended fields are emitted.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is oriented around read-only Workday retrieval and field-selecting JSON projections.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
