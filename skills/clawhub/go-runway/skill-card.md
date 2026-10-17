## Description:

Guides Go developers in using an unofficial typed client to call the Runway API for media generation, task polling, and account management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to add the Runway client, authenticate requests, start media-generation tasks, check task status, and access organization data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Runway API key could allow unauthorized API use.

Mitigation: Read RUNWAYML_API_SECRET from the environment; never put it in code, commits, logs, or printed request headers.

Risk: Generation calls can spend credits, while cancel or delete calls can change user resources.

Mitigation: Review credit-spending and destructive calls before running them; act only on resources the user requested or identified.

Risk: Adding the third-party Go client fetches an external dependency, and API requests send inputs to Runway.

Mitigation: Confirm the dependency source before adding it to a project, and share only inputs intended for Runway.

## Reference(s):

- [Go Runway on ClawHub](https://clawhub.ai/psyb0t/skills/go-runway)
- [Go Runway setup and reference](references/setup.md)
- [Go client repository (skill-listed homepage)](https://github.com/psyb0t/go-runway)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authenticating requests and handling asynchronous task results.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
