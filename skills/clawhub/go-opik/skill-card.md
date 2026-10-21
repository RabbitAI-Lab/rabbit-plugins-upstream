## Description:

Unofficial Go client for the Opik REST API, generated with oapi-codegen from the specification Comet publishes. Package opik (github.com/psyb0t/go-opik) has typed methods for projects, traces, spans, datasets, experiments, prompts, feedback scores, annotation queues and the other published endpoints. Use when Go code needs Opik LLM observability data or already imports go-opik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add or work with the unofficial go-opik client for querying and sending Opik projects, traces, spans, datasets, experiments, prompts, and evaluation feedback. It guides installation, client setup, authentication, and use of generated API methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed in source control, logs, or request headers.

Mitigation: Read credentials from OPIK_API_KEY and OPIK_WORKSPACE; do not hardcode, commit, or log credentials or headers.

Risk: Sensitive prompts, model outputs, or other trace data could be sent to an unintended destination or changed beyond the requested scope.

Mitigation: Verify the selected cloud or user-chosen self-hosted API URL, and send, update, or delete only data involved in the requested action.

Risk: A clean scan does not establish the safety of downloaded dependency code.

Mitigation: Review and pin the dependency version before use.

## Reference(s):

- [Setup and Reference](artifact/references/setup.md)
- [Project Repository](https://github.com/psyb0t/go-opik)
- [Go Package Documentation](https://pkg.go.dev/github.com/psyb0t/go-opik)
- [ClawHub Skill Release](https://clawhub.ai/psyb0t/skills/go-opik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and edits depend on the requested Go integration task.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
