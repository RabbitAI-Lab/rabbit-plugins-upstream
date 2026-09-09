## Description:

Read Workday HR data from a signed-in Workday browser session using the fpx CLI, with guidance for fetching tenant-scoped Workday data endpoints and projecting safe fields with jq.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and engineers use this skill to read their own Workday org chart, worker profile, pay, benefits, compensation, app menu, and related HR data from a shell when the Workday MCP server is not installed or desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can surface sensitive HR data from a user's Workday session in terminal output.

Mitigation: Treat output as confidential HR data and avoid shared logs, CI jobs, chat tools, or untrusted scripts.

Risk: Raw Workday response envelopes can include sessionSecureToken and other internal fields.

Mitigation: Use field-selecting jq filters from the artifact and avoid dumping the raw JSON envelope.

Risk: The fpx CLI uses the user's signed-in browser session to make read-only requests.

Mitigation: Install and run the skill only when this access pattern is acceptable for the user's Workday environment.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read-only requests, authenticated browser-session requirements, endpoint path handling, and filtering output before display or logging.]

## Skill Version(s):

0.6.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
