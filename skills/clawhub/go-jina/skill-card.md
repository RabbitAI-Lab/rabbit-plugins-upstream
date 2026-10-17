## Description:

Guides Go developers in using an unofficial typed client for Jina AI embeddings, reranking, model information, chat completions, batch jobs, and web page reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Jina AI embeddings, reranking, batch jobs, and the Reader API into applications using typed client methods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text, documents, images, and Reader target URLs are sent to Jina AI.

Mitigation: Share only content and URLs approved for transmission to Jina AI.

Risk: The Jina AI API key could be exposed in source code or logs.

Mitigation: Keep JINA_API_KEY in the environment and do not commit or log it or authorization headers.

Risk: Batch job creation may incur charges, and cancellation may interrupt work.

Mitigation: Create or cancel batch jobs only when requested and only for jobs the task controls.

## Reference(s):

- [go-jina setup and API reference](references/setup.md)
- [go-jina project homepage (listed in skill metadata)](https://github.com/psyb0t/go-jina)
- [go-jina ClawHub release](https://clawhub.ai/psyb0t/skills/go-jina)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go examples and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides integration guidance rather than generating files directly.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
