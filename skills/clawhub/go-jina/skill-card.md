## Description:

Guides Go developers in using the unofficial go-jina client for Jina AI embeddings, reranking, document OCR, batch jobs, and web page reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Jina AI embeddings, reranking, document OCR, and Reader responses into applications, including projects that already import go-jina.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text, images, documents, and Reader URLs may be shared with Jina AI.

Mitigation: Send only content the user approves sharing with Jina AI.

Risk: API credentials could leak through source code or logs.

Mitigation: Read JINA_API_KEY from the environment; do not commit it or log Authorization headers.

Risk: Batch requests may incur charges, and batch cancellation affects active jobs.

Mitigation: Create or cancel batch jobs only when requested, and cancel only jobs owned by the task.

## Reference(s):

- [go-jina on ClawHub](https://clawhub.ai/psyb0t/skills/go-jina)
- [go-jina setup and reference](references/setup.md)
- [go-jina Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains typed API calls, authentication, response handling, and Reader options.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
