## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Opik for managing projects, traces, spans, datasets, experiments, prompts, and evaluation feedback. It provides setup, authentication, API usage, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opik trace and span payloads may contain sensitive prompts, model outputs, or other data, and API credentials could be exposed.

Mitigation: Keep the API key and workspace in environment variables, never hardcode or log credentials or request headers, and review payloads before sending them to the selected Opik endpoint.

Risk: The skill is unofficial, and its benign security verdict does not audit the downloaded Go dependency.

Mitigation: Review and pin the Go dependency before use.

## Reference(s):

- [Setup and reference guide](references/setup.md)
- [go-opik repository](https://github.com/psyb0t/go-opik)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-opik)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover Go client setup, API requests, authentication, and response handling.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
