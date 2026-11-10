## Description:

Provides typed Go guidance for calling the Together AI REST API, including authentication, response handling, and operations such as chat completions, embeddings, and resource management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls to Together AI services, including chat and text completions, embeddings, and resource management. It provides setup, authentication, request, and response handling guidance for projects using the go-togetherai package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Together AI bearer API key could be exposed through source code, logs, or request headers.

Mitigation: Read the key from an environment variable; do not hardcode, commit, or log it, and never print request headers.

Risk: Prompts and files sent by the client are processed by Together AI.

Mitigation: Send only data the user intends Together AI to process.

Risk: Fine-tuning jobs and dedicated resources can incur charges, while delete operations remove data.

Mitigation: Create paid resources or delete data only when the user explicitly requests the action.

Risk: The bundled guidance does not fully audit downloaded Go dependencies.

Mitigation: Review and consider pinning the Go dependency to a known version.

## Reference(s):

- [go-togetherai source repository](https://github.com/psyb0t/go-togetherai)
- [go-togetherai package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
