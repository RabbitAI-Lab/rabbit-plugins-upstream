## Description:

Read selected Workday HR data from an authenticated browser session using the fpx CLI, including org charts, worker profiles, tasks, pay, benefits, compensation, and app-menu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and authorized operators use this skill to retrieve specific Workday tenant data through their own signed-in browser session and project the response into safer command-line output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill bridges a local shell to an authenticated Workday browser session and can access sensitive HR, compensation, pay, benefits, and worker data.

Mitigation: Use only with authorization, restrict browser-extension site access to the narrowest tenant host possible, and uninstall or revoke pairing after use on shared or sensitive machines.

Risk: Raw Workday response envelopes may include session security tokens or other internal fields.

Mitigation: Use field-selecting jq filters and never output, log, or store complete raw response envelopes.

Risk: Persistent third-party bridge tooling may retain access after initial pairing.

Mitigation: Verify the CLI and extension source before installation and remove pairing when the workflow is complete.

## Reference(s):

- [Workday htmld endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should project selected fields from Workday responses and avoid raw response envelopes.]

## Skill Version(s):

0.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
