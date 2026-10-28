## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this unofficial typed client to ingest or query Opik traces and spans, and work with projects, datasets, experiments, prompts, and evaluation feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial client may differ from a client maintained by Comet or change between releases.

Mitigation: Review and pin the dependency version before using it.

Risk: API credentials and trace or span data may expose sensitive information, and requests can upload, update, or delete data in the selected workspace.

Mitigation: Keep credentials out of source code and logs; confirm the target workspace and sensitive data before requesting changes.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-opik package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [go-opik project](https://github.com/psyb0t/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
