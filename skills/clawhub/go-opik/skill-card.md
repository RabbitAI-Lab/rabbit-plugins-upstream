## Description:

Provides a typed Go client for working with Opik REST API resources such as traces, spans, projects, datasets, experiments, prompts, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go code that sends or retrieves Opik observability and evaluation data. It is intended for Go projects using Opik Cloud or a self-hosted Opik server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opik traces and spans can contain prompts, model output, and other sensitive data.

Mitigation: Protect API credentials and confirm the destination and requested data changes before sending or modifying trace data.

Risk: This is an unofficial client and may not match Comet-maintained tooling or future API behavior.

Mitigation: Review and pin the dependency version before using it in a project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-opik on GitHub](https://github.com/psyb0t/go-opik)
- [go-opik on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [go-opik on ClawHub](https://clawhub.ai/psyb0t/skills/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
