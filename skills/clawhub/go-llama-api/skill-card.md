## Description:

Guides Go developers in using an unofficial typed client for Meta's Llama API, including chat completions, models, moderation, and uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill for guidance on adding the client, authenticating, and calling Meta's Llama API for chat, models, moderation, and file uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed in code, logs, or request headers.

Mitigation: Load LLAMA_API_KEY from the environment; do not hardcode, commit, or log the key or authorization headers.

Risk: Prompts and uploaded files are sent to Meta's Llama API.

Mitigation: Send only data approved for sharing with Meta, and upload files only when the user requests it.

Risk: Adding an unofficial Go dependency requires trusting its upstream code.

Mitigation: Review the upstream module before adding it to a project.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [go-llama-api repository](https://github.com/psyb0t/go-llama-api)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-llama-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers API responses, errors, and raw streaming responses.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
