## Description:

Guides Go developers in using an unofficial typed client for Meta's Llama API, including chat, models, moderation, and uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use a Go client for Meta's Llama API in applications that need chat completions, model listings, moderation, or file uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Llama API key in source code, logs, or shared output.

Mitigation: Read LLAMA_API_KEY from the environment; do not commit, print, or log credentials or request headers.

Risk: Prompts and uploaded files may contain data not intended for Meta.

Mitigation: Send only data the user approves and upload files only when explicitly requested.

Risk: Adding an unreviewed third-party Go dependency to production code.

Mitigation: Review the client dependency and its transitive dependencies before adoption.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-llama-api)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-llama-api)
- [Go client homepage](https://github.com/psyb0t/go-llama-api)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers Bearer authentication, typed requests and responses, streaming, and error handling.]

## Skill Version(s):

0.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
