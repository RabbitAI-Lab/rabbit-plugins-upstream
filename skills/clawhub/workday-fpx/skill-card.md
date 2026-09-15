## Description:

Read Workday HR data from an authorized signed-in Workday browser session using fpx CLI commands and jq projections for tenant-scoped *.htmld endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees, developers, and HR operations engineers use this skill to query Workday data through their own authenticated tenant session without running the Workday MCP server. It helps agents assemble shell commands, endpoint paths, and jq projections for read-only Workday data inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Workday HR records through an authenticated browser session.

Mitigation: Use it only with organizational authorization, restrict access to the exact Workday tenant where possible, and treat all outputs as sensitive HR records.

Risk: Raw Workday response envelopes may include session tokens or other session-internal fields.

Mitigation: Use field-selecting jq projections and avoid raw response dumps in terminals, logs, scripts, or agent transcripts.

Risk: Persistent browser extension pairing can continue beyond the immediate task.

Mitigation: Unpair or revoke extension access when finished, and pin and verify the fpx package and extension source before use.

Risk: The practical access scope may be broader than self-only data claims.

Mitigation: Avoid broad enumeration and confirm the intended Workday data scope before running commands.

## Reference(s):

- [Workday *.htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown guidance with inline shell commands, endpoint examples, and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference sensitive Workday HR data and should avoid raw response dumps.]

## Skill Version(s):

0.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
