## Description:

Guides Go developers in using the unofficial go-opik client to access Opik observability data through typed API methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working in Go use this skill to add the unofficial Opik client, authenticate requests, and work with projects, traces, spans, datasets, and evaluations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go module is a third-party dependency that may be unsuitable for some projects.

Mitigation: Review the module and use it only in Go projects that need Opik access.

Risk: Opik credentials, traces, prompts, and model outputs may contain sensitive information.

Mitigation: Keep credentials in environment variables, avoid logging headers or committing keys, and review data before sending it to Opik.

Risk: Client operations can update or delete Opik data.

Mitigation: Review write and delete operations and perform only actions requested by the user.

## Reference(s):

- [go-opik setup and reference](references/setup.md)
- [go-opik module homepage](https://github.com/psyb0t/go-opik)
- [go-opik ClawHub release](https://clawhub.ai/psyb0t/skills/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for a Go project; the skill does not itself produce files.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
