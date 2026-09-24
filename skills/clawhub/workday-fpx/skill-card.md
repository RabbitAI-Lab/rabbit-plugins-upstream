## Description:

Read Workday HR data, including org chart, worker profiles, tasks, pay, benefits, compensation, and app menu data, from a shell with the fpx CLI through the user's already signed-in myworkday.com browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Workday users use this skill to fetch their own Workday data from a shell when they need scriptable access without running the Workday MCP server. It provides setup steps, endpoint patterns, jq projections, and troubleshooting guidance for read-only Workday htmld data requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses fpx and the Transporter extension to make Workday requests through the user's active signed-in browser session.

Mitigation: Install and pair it only when that access model is acceptable, and keep requests scoped to the user's own authorized Workday data.

Risk: Raw Workday response envelopes may include session tokens and sensitive HR data.

Mitigation: Use the field-selecting jq filters provided by the skill instead of dumping raw responses.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, endpoint patterns, and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be reviewed and adapted for the user's own Workday host, tenant, signed-in browser session, and selected fields.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
