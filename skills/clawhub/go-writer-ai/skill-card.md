## Description:

Provides Go developers with a typed client for calling the Writer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add go-writer-ai and call Writer services such as chat, completions, files, Knowledge Graphs, applications, PDF parsing, web search, and vision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded files are sent to Writer.

Mitigation: Send only content approved for Writer, and authorize uploads explicitly.

Risk: A Writer API key could be exposed through source code or logs.

Mitigation: Read the key from WRITER_API_KEY; do not hardcode, commit, or log it.

Risk: File and graph uploads or deletions can change remote Writer data.

Mitigation: Perform uploads or deletions only when requested and only for resources the task owns.

Risk: The Go client is unofficial.

Mitigation: Review the dependency before adding it to a project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-writer-ai)
- [Project homepage](https://github.com/psyb0t/go-writer-ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and API call guidance; requires Go and a Writer API key.]

## Skill Version(s):

0.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
