## Description:

Unofficial Go client for the Together AI REST API, generated with oapi-codegen. `together.NewClientWithResponses(baseURL, opts...)` from `github.com/psyb0t/go-togetherai` returns a `*together.ClientWithResponses` with one typed `...WithResponse` method per endpoint (models, chat completions, completions, embeddings, images, fine-tuning, endpoints and more). Auth is a bearer API key set through `together.WithRequestEditorFn`; responses decode into `JSON200` and per-status error fields. Use when Go code needs to call Together AI or already imports go-togetherai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External developers use this skill to add or work with the typed Go client for Together AI, including model, chat, completion, embedding, image, fine-tuning, and endpoint operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Together AI receives prompts and files included in API requests.

Mitigation: Send only content intended for Together AI and keep the API key in an environment variable; do not hardcode, commit, or log it.

Risk: Fine-tuning, dedicated endpoint, and cluster operations can incur charges, while delete operations remove data.

Mitigation: Request paid or destructive operations only when the user has asked for them.

Risk: Dependency changes may affect the client used by a project.

Mitigation: Pin and review the dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [GitHub repository](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go client usage, request examples, and response-handling guidance; the library itself does not write files.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
