## Description:

Provides Go developers with a typed client and practical guidance for calling Together AI's REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Together AI API calls to applications, including chat, completions, embeddings, model listings, and endpoint management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial: a local path-like reference was not matched to an artifact, and the install-mechanism note is unexplained in the supplied results.

Mitigation: Review the unmatched reference and clarify the installation mechanism before relying on behavior the scan did not cover.

Risk: Some API operations may incur charges or delete data, and prompts or files sent through the client are processed by Together AI.

Mitigation: Keep the API key in an environment variable, and call paid or destructive operations only when explicitly requested.

## Reference(s):

- [Setup and Reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific guidance and code examples; live API calls require Go and a Together AI API key.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
