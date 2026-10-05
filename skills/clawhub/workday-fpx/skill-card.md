## Description:

Helps employees read their Workday HR data through an already signed-in browser session using the fpx CLI, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use the skill to retrieve their own Workday app menu, worker profiles, org chart, tasks, pay, benefits, and compensation from a signed-in session for review or scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access routes a signed-in Workday session through the browser bridge.

Mitigation: Install only if comfortable using the bridge with your own signed-in session; follow your organization's HR data handling rules.

Risk: Workday results may expose sensitive HR data or session details when shared or logged.

Mitigation: Query only needed fields, avoid raw response dumps and shared logs, and redact results before sharing.

## Reference(s):

- [Workday via fpx on ClawHub](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint and field-selection guide](references/endpoints.md)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions with shell commands and field-selected JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain sensitive HR information.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
