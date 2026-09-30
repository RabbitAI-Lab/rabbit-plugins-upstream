## Description:

Guides agents in reading Workday HR data through a user's signed-in browser session using the fpx CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to read Workday app menus, worker profiles, org charts, tasks, pay, and benefits from an existing signed-in browser session without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx CLI and ContextMint Bridge can access Workday pages available to the signed-in browser session.

Mitigation: Install and pair them only if you are comfortable granting that access.

Risk: Raw Workday responses may expose session tokens or sensitive HR information.

Mitigation: Use the supplied field-selecting jq projections; do not print or store raw responses.

## Reference(s):

- [Workday FPX skill listing](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint and jq recipes](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Field-selected Workday data; raw responses may contain sensitive HR information or session tokens.]

## Skill Version(s):

1.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
