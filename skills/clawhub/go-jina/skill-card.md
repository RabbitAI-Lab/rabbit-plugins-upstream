## Description:

Helps Go developers use typed clients for Jina AI embeddings, reranking, model listings, document OCR, batch jobs, and web-page reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and operate Jina AI API clients for embeddings, reranking, document processing, batch jobs, and Reader page extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the client adds a third-party Go module to the project.

Mitigation: Review the dependency before adding it with the Go toolchain.

Risk: API calls send selected content or URLs to Jina AI.

Mitigation: Send only inputs the user approves sharing with Jina AI.

Risk: Exposed API keys or unintended batch-job actions can affect the Jina account.

Mitigation: Keep JINA_API_KEY in the environment and out of logs; create or cancel batch jobs only when requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-jina)
- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)
- [Module homepage listed in skill metadata](https://github.com/psyb0t/go-jina)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers API-key handling, request construction, and HTTP error checks.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
