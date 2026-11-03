## Description:

Provides Go developers with a typed client for calling Mistral AI's REST API, including chat, embeddings, model listing, and other endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add and use the go-mistral client in projects that call Mistral AI endpoints such as chat completions and embeddings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests may send prompts or files to Mistral AI, and mishandled API keys could expose credentials.

Mitigation: Use a protected MISTRAL_API_KEY, never commit or log it, and send only data intended for Mistral to process.

Risk: Batch jobs may incur charges, and delete endpoints remove data.

Mitigation: Run paid batch or delete operations only when explicitly requested by the user.

Risk: The Go dependency version may change between builds if it is not pinned.

Mitigation: Consider pinning the go-mistral dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-mistral source repository](https://github.com/psyb0t/go-mistral)
- [go-mistral package documentation](https://pkg.go.dev/github.com/psyb0t/go-mistral)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup and endpoint examples; the skill guides changes to the current Go project when requested.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
