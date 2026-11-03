## Description:

Read authorized Workday HR data through a signed-in browser session using the fpx CLI, with shell examples for Workday data endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Workday employees and developers use this skill to retrieve authorized worker, organization, task, pay, and benefits information from a shell when they need an alternative to the Workday MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes access as limited to the user's own records while also providing instructions for reading other workers' profiles.

Mitigation: Before pairing, establish which employees' records are authorized and limit requests to those records.

Risk: Workday response envelopes contain a sessionSecureToken that should not be exposed in command output.

Mitigation: Use the supplied field-selecting jq projections and never print the raw response envelope.

## Reference(s):

- [ClawHub workday-fpx listing](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions with shell command examples and projected JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data retrieval; response examples project selected fields rather than printing the full response envelope.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
