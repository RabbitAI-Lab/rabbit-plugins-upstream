## Description:

Read Workday HR data through your signed-in Workday browser session using the fpx CLI, without running the workday-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Workday employees and developers use the skill to read permitted HR data, such as worker profiles, org charts, benefits, and pay, through their own authenticated Workday session. It provides shell commands and jq projections for retrieving and filtering that data without a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged review is incomplete because some referenced documentation paths are unavailable.

Mitigation: Confirm endpoint behavior against your Workday tenant and check any referenced documentation that is not included before relying on those recipes.

Risk: Raw Workday response envelopes can contain a session security token alongside HR data.

Mitigation: Use the provided field-selecting jq projections and avoid printing or saving the full unfiltered response.

## Reference(s):

- [Endpoint recipes](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with shell and jq examples; fetched Workday responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; responses may include sensitive HR data.]

## Skill Version(s):

1.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
