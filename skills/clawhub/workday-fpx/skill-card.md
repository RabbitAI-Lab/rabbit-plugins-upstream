## Description:

Guides employees in reading Workday HR information through their signed-in browser session using the fpx CLI instead of a separate MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized developers use the skill to look up specific Workday app, worker, org chart, pay, or benefits information from an existing signed-in session without running the Workday MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated Workday session may expose sensitive HR information about other employees.

Mitigation: Limit use to specific authorized lookups; avoid bulk crawling and handle results under employer HR-data policies.

Risk: Raw Workday responses can expose sensitive data or session information.

Mitigation: Never print or save raw responses; project only the fields needed for the lookup.

## Reference(s):

- [Workday endpoint recipes](references/endpoints.md)
- [ClawHub workday-fpx release](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain sensitive HR data; show only fields needed for the authorized lookup.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
