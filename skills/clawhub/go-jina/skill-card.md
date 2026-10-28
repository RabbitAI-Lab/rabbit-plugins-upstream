## Description:

Unofficial Go client for the Jina AI APIs, generated with oapi-codegen. Package `jina` (`github.com/psyb0t/go-jina`) calls api.jina.ai for embeddings, reranking, the model list, chat completions (document OCR) and batch embedding jobs; package `jinareader` (`github.com/psyb0t/go-jina/reader`) calls r.jina.ai to read a web page as markdown, text, HTML or JSON. Every endpoint is a typed `...WithResponse` method on `ClientWithResponses`, auth is a bearer API key set through `WithRequestEditorFn`, and responses decode into `JSON200` and per-status error fields. Use when Go code needs Jina embeddings, a reranker or the Reader API, or already imports go-jina.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add typed client calls for Jina AI embeddings, reranking, chat completions, batch embedding jobs, and the Reader API to a Go project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if hardcoded, committed, or logged.

Mitigation: Read the Jina API key from the JINA_API_KEY environment variable and avoid logging the Authorization header.

Risk: Text, images, documents, and requested URLs are sent to Jina AI services.

Mitigation: Send only content the user agrees to share with Jina AI.

Risk: Batch embedding jobs can incur charges, and cancelling a job stops that job.

Mitigation: Create or cancel only batch jobs requested by the user and owned by the task.

Risk: Requests could be sent to an untrusted API endpoint if a base URL is misconfigured.

Mitigation: Use trusted Jina base URLs: https://api.jina.ai for jina and https://r.jina.ai for jinareader.

## Reference(s):

- [go-jina setup and reference](references/setup.md)
- [go-jina on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-jina)
- [go-jina source repository](https://github.com/psyb0t/go-jina)
- [go-jina ClawHub release](https://clawhub.ai/psyb0t/skills/go-jina)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides integration guidance and examples; the library does not read or write project files.]

## Skill Version(s):

0.4.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
