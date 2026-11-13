## Description:

Provides typed Go methods and usage guidance for calling the Together AI REST API with bearer-key authentication and typed responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and call the go-togetherai Go client in projects that need Together AI API operations, including completions, embeddings, and endpoint management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scan coverage is incomplete because one reference in SKILL.md could not be resolved.

Mitigation: Review the unresolved reference and available skill files before installing.

Risk: An exposed API key could allow unauthorized use of the Together AI account.

Mitigation: Read the key from an environment variable; do not hardcode, commit, or log it.

Risk: Fine-tuning, dedicated endpoint, and cluster operations can incur costs, and delete operations remove data.

Mitigation: Run billable or destructive operations only when the user requested them.

Risk: Prompts and files sent through the client are processed by Together AI.

Mitigation: Send only data that is appropriate to share with the service.

## Reference(s):

- [Setup and usage guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use an API key and make requests to Together AI.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
