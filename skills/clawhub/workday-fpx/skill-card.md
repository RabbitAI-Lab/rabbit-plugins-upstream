## Description:

Read Workday HR data such as org charts, worker profiles, tasks, pay, benefits, compensation, and app menus from a shell with the fpx CLI through a user's signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operations teams use this skill to retrieve selected Workday HR data through an already-authenticated browser session when they need shell-based access without running the Workday MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Workday HR data, including worker, organization, pay, benefits, and compensation information.

Mitigation: Use only where browser-session-based Workday access from shell tools is permitted, minimize collected fields, and treat outputs as sensitive HR data.

Risk: Raw Workday response envelopes may include session-internal data such as sessionSecureToken.

Mitigation: Avoid raw response dumps and use field-selecting jq filters that project only the required data.

Risk: Persistent fpx pairing can continue to reuse an authenticated browser bridge.

Mitigation: Keep fpx paired only as needed and review pairing state before using the skill on shared or unmanaged machines.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include sensitive Workday HR data and should be field-projected rather than raw response dumps.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
