## Description:

Provides a typed Go client for calling Fireworks AI inference and control-plane REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add or work with the go-fireworks client in a project that calls Fireworks AI. It provides setup, authentication, endpoint, and typed response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, prompts, datasets, and model files sent through the client are disclosed to the configured Fireworks AI endpoint.

Mitigation: Use a narrowly scoped API key, verify the destination URL, and send only data intended for Fireworks AI. Keep credentials in environment variables and out of logs and source control.

Risk: Deployment, fine-tuning, batch-job, and delete operations can incur costs or affect resources.

Mitigation: Run these operations only when explicitly requested, and confirm that they target the intended resources.

Risk: The client is an unofficial dependency whose version may change.

Mitigation: Review the dependency and pin the version used by the project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-fireworks on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-fireworks)
- [go-fireworks project repository](https://github.com/psyb0t/go-fireworks)
- [go-fireworks on ClawHub](https://clawhub.ai/psyb0t/skills/go-fireworks)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for adding and using the client in a Go project.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
