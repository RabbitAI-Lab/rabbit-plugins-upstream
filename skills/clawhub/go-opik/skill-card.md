## Description:

An unofficial typed Go client for the Opik REST API that helps Go projects query and manage observability data through methods for projects, traces, spans, datasets, experiments, prompts, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the skill to add typed Opik API operations to Go projects for querying and sending observability data such as traces, spans, projects, datasets, experiments, prompts, and feedback. It is intended for projects using Opik Cloud or a self-hosted Opik server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if hardcoded, committed, or logged with request headers.

Mitigation: Read the API key and workspace from OPIK_API_KEY and OPIK_WORKSPACE; do not hardcode, commit, or log credentials or request headers.

Risk: Trace and span payloads can contain prompts, model output, and other sensitive data.

Mitigation: Send, update, or delete data only for the action the user requested, and use a self-hosted server only when the user selected its URL.

Risk: The security review is partial because a referenced local path was missing.

Mitigation: Review the available skill and reference files before use; the benign scan verdict does not establish that the skill is risk-free.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [Project homepage](https://github.com/psyb0t/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for Go API usage, setup, authentication, pagination, and response handling.]

## Skill Version(s):

0.6.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
