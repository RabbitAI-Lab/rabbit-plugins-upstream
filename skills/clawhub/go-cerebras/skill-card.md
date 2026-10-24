## Description:

Helps developers write Go code using an unofficial client for the Cerebras Inference API, including chat completions, text completions, and model discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Cerebras inference calls to Go projects, locate typed client methods, and handle responses and errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adding an unofficial Go dependency may introduce supply-chain risk.

Mitigation: Review the dependency before installing it with the Go toolchain.

Risk: Prompts and API requests are sent to Cerebras through the configured base URL.

Mitigation: Confirm the base URL and review what data may be sent before making requests.

Risk: A leaked API key can expose access to the Cerebras account.

Mitigation: Store the key in an environment variable or secret manager; do not commit it or log request headers.

## Reference(s):

- [go-cerebras setup and reference](references/setup.md)
- [go-cerebras package documentation](https://pkg.go.dev/github.com/psyb0t/go-cerebras)
- [go-cerebras project repository](https://github.com/psyb0t/go-cerebras)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code snippets and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Cerebras API key for authenticated requests.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
