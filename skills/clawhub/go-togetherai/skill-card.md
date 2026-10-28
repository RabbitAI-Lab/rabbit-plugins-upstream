## Description:

Unofficial Go client for the Together AI REST API, generated with oapi-codegen. `together.NewClientWithResponses(baseURL, opts...)` from `github.com/psyb0t/go-togetherai` returns a `*together.ClientWithResponses` with one typed `...WithResponse` method per endpoint (models, chat completions, completions, embeddings, images, fine-tuning, endpoints and more). Auth is a bearer API key set through `together.WithRequestEditorFn`; responses decode into `JSON200` and per-status error fields. Use when Go code needs to call Together AI or already imports go-togetherai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with the Together AI API through the typed go-togetherai client, including setup, authentication, requests, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can expose API credentials and send prompts or files to Together AI for processing.

Mitigation: Read the API key from an environment variable, never hardcode, commit, log, or print request headers, and send only data intended for Together AI to process.

Risk: Fine-tuning jobs, dedicated endpoints, and clusters can incur costs, while delete operations remove data.

Mitigation: Request paid resources or deletions only when the user explicitly asks for that action.

Risk: The integration depends on an external Go module.

Mitigation: Review and pin the external Go dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)

## Skill Output:

**Output Type(s):** [Guidance, Go code, Shell commands]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
