## Description:

Read Workday HR data such as org charts, worker profiles, tasks, pay, benefits, compensation, and app menus from a shell using the fpx CLI through the user's already signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to query their own authorized Workday web-session data from scripts or shell workflows without running the Workday MCP server. It is intended for read-only retrieval and field-focused projection of Workday htmld responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx CLI and Transporter browser extension can receive persistent access to sensitive Workday session data.

Mitigation: Install only after trusting the CLI and extension, use a reviewed pinned CLI version, scope browser extension site access to the exact tenant where possible, and revoke or disable pairing after use.

Risk: Workday responses may include session tokens or sensitive envelope fields if raw JSON is dumped.

Mitigation: Use field-selecting jq filters from the skill references, avoid bare jq output, and keep command output out of logs, shell history, shared transcripts, and broad files.

Risk: The skill accesses HR, pay, benefits, and compensation data that may be subject to company policy and privacy controls.

Mitigation: Use only with company authorization for the Workday data involved, and prefer a dedicated browser profile for the paired session.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only command recipes and field-selection guidance; it does not execute Workday calls by itself.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
