## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Go applications with Opik by installing and using the typed client for traces, projects, datasets, experiments, prompts, and evaluation feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client is unofficial, and downloaded dependencies may change.

Mitigation: Review and pin the dependency before using it.

Risk: API credentials or sensitive trace contents could be exposed when sent or logged.

Mitigation: Keep credentials out of source code and logs, and verify the workspace, selected server, and trace contents before sending data.

## Reference(s):

- [go-opik setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [Project repository](https://github.com/psyb0t/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
