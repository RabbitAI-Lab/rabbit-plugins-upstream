## Description:

Guides an agent to fetch read-only Workday HR data through an authorized signed-in Workday browser session with the fpx CLI and project selected results with jq.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees, developers, and operations teams use this skill to retrieve selected Workday HR information such as org charts, worker profiles, tasks, pay, benefits, compensation, and app-menu data from their own signed-in Workday session for shell or script workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Workday HR data may be exposed through terminal output, scripts, logs, or saved raw responses.

Mitigation: Use the skill only with authorization, treat outputs as confidential, project only needed fields, and avoid storing or logging results unless approved.

Risk: Raw Workday response envelopes can include session-related secret fields.

Mitigation: Do not dump complete responses; use the documented jq projections or equivalent allowlisted field extraction.

Risk: The workflow depends on the external fpx CLI and Transporter browser extension operating with an authenticated Workday session.

Mitigation: Review and approve the fpx and Transporter trust model before pairing them with a Workday session.

## Reference(s):

- [Workday *.htmld endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only command guidance; outputs can include sensitive HR data and should be projected to selected fields.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
