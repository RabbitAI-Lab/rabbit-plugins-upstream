## Description:

Provides Go developers with a typed client for Perplexity API features such as chat, search, embeddings, and account tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers can use this skill to add typed Go access to Perplexity API features in an existing Go application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed, and requests may transmit sensitive data to Perplexity.

Mitigation: Keep the API key in an environment variable, never commit or log it, and review what data each request sends.

Risk: API calls may incur charges or change account state.

Mitigation: Make chargeable or state-changing calls only when explicitly requested, and limit account changes to resources named or created for the task.

Risk: The integration is unofficial and depends on third-party Go packages.

Mitigation: Review the third-party dependency before adding it to a project.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-perplexity)
- [Project homepage](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Go toolchain and a Perplexity API key.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
