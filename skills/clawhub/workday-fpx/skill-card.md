## Description:

Helps users read Workday HR information through their signed-in browser session with the fpx CLI, without running a separate MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized developers use this skill to retrieve their accessible Workday app menu, worker profiles, org chart, tasks, pay, benefits, and compensation information from a signed-in session without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the paired browser extension grants access through an existing signed-in Workday session.

Mitigation: Install only if comfortable granting this access, and use the minimum endpoint needed for each task.

Risk: Workday responses may expose confidential HR information or session data if raw responses are logged or shared.

Mitigation: Select only required fields; do not log raw responses or bulk crawl employee records.

## Reference(s):

- [Workday endpoint recipes](artifact/references/endpoints.md)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and filtered Workday data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; output can contain confidential HR information.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
