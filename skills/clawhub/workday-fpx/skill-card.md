## Description:

Read Workday HR data from an authenticated Workday browser session using the fpx CLI, with guidance for fetching selected *.htmld endpoints and projecting JSON fields with jq.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and automation agents use this skill to retrieve selected Workday HR information, such as org charts, worker profiles, tasks, pay, benefits, compensation, and app menus, through an already signed-in Workday session without running the workday-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates persistent, broadly scoped shell access to sensitive Workday HR data through the fpx CLI and Transporter browser extension.

Mitigation: Install only if that access is acceptable, verify the package and extension identity, and remove the pairing or browser site access immediately after use when appropriate.

Risk: Skill output can contain sensitive HR information, including pay, benefits, compensation, worker profile, task, and org chart data.

Mitigation: Treat all retrieved output as sensitive HR data, avoid raw dumps and logs, and share only the minimum projected fields needed for the task.

Risk: Raw Workday response envelopes may include sessionSecureToken or other internal session fields.

Mitigation: Use the documented field-selecting jq filters and do not pipe responses through bare jq output or other whole-envelope dumps.

## Reference(s):

- [Workday *.htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guidance emphasizes field-selecting jq projections and avoiding raw Workday response dumps.]

## Skill Version(s):

0.6.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
