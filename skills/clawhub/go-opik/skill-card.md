## Description:

Guides Go developers using the unofficial go-opik client to access Opik projects, traces, spans, datasets, and other REST API resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial go-opik client and write code that reads or updates Opik observability and evaluation data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go dependency may not meet the user's trust requirements.

Mitigation: Confirm the dependency is trusted before installation.

Risk: Opik API keys or sensitive trace contents could be exposed through logging or an unintended endpoint.

Mitigation: Keep keys in environment variables, avoid logging headers or trace contents, and send data only to Opik Cloud or a user-approved self-hosted endpoint.

## Reference(s):

- [go-opik on ClawHub](https://clawhub.ai/psyb0t/skills/go-opik)
- [go-opik package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a caller-selected Opik endpoint and environment-provided credentials.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
