## Description:

Unofficial Go client for the Jina AI APIs, generated with oapi-codegen. Package `jina` (`github.com/psyb0t/go-jina`) calls api.jina.ai for embeddings, reranking, the model list, chat completions (document OCR) and batch embedding jobs; package `jinareader` (`github.com/psyb0t/go-jina/reader`) calls r.jina.ai to read a web page as markdown, text, HTML or JSON. Every endpoint is a typed `...WithResponse` method on `ClientWithResponses`, auth is a bearer API key set through `WithRequestEditorFn`, and responses decode into `JSON200` and per-status error fields. Use when Go code needs Jina embeddings, a reranker or the Reader API, or already imports go-jina.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to install and use the go-jina client for Jina AI embeddings, reranking, model discovery, chat completions, batch jobs, and Reader API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, images, documents, and URLs used with the client are sent to Jina AI; batch jobs may incur charges.

Mitigation: Send only data approved for sharing with Jina AI, protect the API key, use a reviewed dependency version, and create or cancel only user-requested batch jobs.

Risk: The external dependency implementation was not audited.

Mitigation: Use a reviewed dependency version.

## Reference(s):

- [go-jina setup and API reference](artifact/references/setup.md)
- [go-jina package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)
- [go-jina ClawHub release](https://clawhub.ai/psyb0t/skills/go-jina)
- [go-jina project homepage](https://github.com/psyb0t/go-jina)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
