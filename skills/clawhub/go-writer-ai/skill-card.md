## Description:

Guides Go developers in using an unofficial typed client for Writer's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use a Go client for Writer chat, completions, files, Knowledge Graphs, and other Writer API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial client may not meet a project's dependency requirements.

Mitigation: Review the client before installing and using it.

Risk: Writer API calls send prompts and uploaded files to Writer.

Mitigation: Send only data approved for the task, and upload files only when requested.

Risk: The Writer API key could be exposed in source code or logs.

Mitigation: Keep WRITER_API_KEY in the environment; do not commit or log it.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-writer-ai)
- [Go client homepage (listed by the skill)](https://github.com/psyb0t/go-writer-ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Writer API key in WRITER_API_KEY.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
