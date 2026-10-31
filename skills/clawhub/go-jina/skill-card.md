## Description:

Guides Go developers in using typed clients for Jina AI embeddings, reranking, chat completions, batch embedding jobs, and the Reader API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to integrate Jina AI embeddings, reranking, chat completions, batch jobs, and web page reading into a Go project. It provides setup, authentication, request, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, images, documents, and URLs submitted through the client are sent to Jina AI services.

Mitigation: Send only content the user approves sharing with Jina AI.

Risk: An API key could be exposed through source code, commits, or logs.

Mitigation: Read the key from JINA_API_KEY, keep it out of code and commits, and never log the Authorization header.

Risk: Batch job creation can incur charges, and cancellation stops a job.

Mitigation: Create or cancel only jobs the task owns and only when requested.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-jina repository](https://github.com/psyb0t/go-jina)
- [go-jina Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)
- [go-jina Reader package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina/reader)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance; no files are read or written by the library.]

## Skill Version(s):

0.4.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
