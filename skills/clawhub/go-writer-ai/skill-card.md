## Description:

Unofficial Go client for the Writer (writer.com) API, generated from Writer's OpenAPI spec. `writer.NewClientWithResponses("https://api.writer.com", auth)` from `github.com/psyb0t/go-writer-ai` gives typed methods for chat (`ChatWithResponse`), text completions (`CompletionsWithResponse`), models (`ModelsWithResponse`), files (`GatewayGetFilesWithResponse`, `GatewayUploadFileWithBodyWithResponse`), Knowledge Graphs (`CreateGraphWithResponse`, `QuestionWithResponse`), no-code applications (`GenerateContentWithResponse`), the PDF parser, web search and vision, with responses decoded into `JSON200`. Auth is a Bearer API key set through a `RequestEditorFn`. Use when Go code needs to call the Writer API or already imports go-writer-ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with the Writer API through the go-writer-ai client. It provides setup, authentication, endpoint, response handling, upload, and streaming guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded files are sent to Writer and may contain sensitive information.

Mitigation: Send only user-authorized content and review the applicable data-handling requirements before sending it.

Risk: A leaked Writer API key could allow unauthorized API access.

Mitigation: Read the key from WRITER_API_KEY; never hardcode, commit, log, or print request headers containing it.

Risk: File or Knowledge Graph deletion can remove data.

Mitigation: Delete only items the user explicitly asked to remove and that the task owns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-writer-ai)
- [go-writer-ai source repository](https://github.com/psyb0t/go-writer-ai)
- [go-writer-ai package documentation](https://pkg.go.dev/github.com/psyb0t/go-writer-ai)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
