## Description:

Read Workday HR data from a shell with the fpx CLI using an authorized browser-authenticated Workday session instead of running the workday-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers with authorized Workday access use this skill to fetch selected Workday HR data from their own signed-in browser session via fpx, without running the Workday MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workday output can contain sensitive HR and session-linked data.

Mitigation: Use only field-selecting jq filters and avoid logging, sharing, or dumping raw Workday responses.

Risk: The fpx pairing reuses a signed-in browser session from the local machine or browser profile.

Mitigation: Install and use the skill only when authorized for the Workday tenant, and remove or re-pair fpx if the machine or browser profile is no longer trusted.

## Reference(s):

- [Workday *.htmld endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday data access guidance that emphasizes field-selecting jq filters and avoiding raw response dumps.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
