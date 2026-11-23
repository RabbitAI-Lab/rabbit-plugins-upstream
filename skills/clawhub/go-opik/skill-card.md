## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill when Go applications need to query or send Opik projects, traces, spans, datasets, experiments, prompts, and evaluation feedback through the unofficial typed Go client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opik API keys and workspace credentials could be exposed if hardcoded, committed, or logged.

Mitigation: Read credentials from OPIK_API_KEY and OPIK_WORKSPACE, and keep them out of source control and logs.

Risk: Trace and span payloads can contain prompts, model output, and other sensitive data.

Mitigation: Send, update, or delete trace and span data only for the action the user requested.

Risk: The security scan could not resolve one local reference, so its coverage is incomplete.

Mitigation: Review the unresolved reference when assessing the scan results.

## Reference(s):

- [Project repository](https://github.com/psyb0t/go-opik)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-opik)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
