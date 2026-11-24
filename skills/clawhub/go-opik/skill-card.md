## Description:

An unofficial Go client for the Opik REST API that provides typed access to projects, traces, spans, datasets, experiments, prompts, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and configure the unofficial go-opik client in a project. It helps them call Opik endpoints for observability data and related resources while handling credentials and sensitive trace data carefully.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because one referenced item could not be resolved.

Mitigation: Resolve and review the missing reference before relying on the skill in a sensitive environment.

Risk: Trace and span payloads may contain prompts, model output, or other sensitive data.

Mitigation: Send, update, or delete data only for the requested action, and avoid logging API credentials or request headers.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [Source repository](https://github.com/psyb0t/go-opik)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for using the Go client; no standalone output file is specified.]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
