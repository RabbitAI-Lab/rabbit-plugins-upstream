## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to install and call the unofficial typed go-opik client for querying or sending Opik projects, traces, spans, datasets, experiments, prompts and evaluation feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downloaded Go client and its dependencies are outside the bundled skill review.

Mitigation: Review and pin the Go dependency before adding it to a project.

Risk: API credentials could be exposed or sent with overly broad access.

Mitigation: Use appropriately scoped credentials from OPIK_API_KEY and OPIK_WORKSPACE; do not hardcode, commit or log them.

Risk: Trace and span payloads may contain private prompts or model output, and requests may target the wrong Opik server or change unintended data.

Mitigation: Choose the intended server and send, update or delete only the data needed for the user's requested action.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-opik source repository](https://github.com/psyb0t/go-opik)
- [go-opik package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No fixed output file; content depends on the requested Opik operation.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
