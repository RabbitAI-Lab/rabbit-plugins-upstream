## Description:

Guides Go developers in using an unofficial typed client for the xAI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and work with a typed xAI API client for chat, embeddings, media generation, and other supported endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The xAI API key could be exposed in source code or logs.

Mitigation: Keep XAI_API_KEY in environment or secret storage; do not commit keys or log request headers.

Risk: API calls can incur charges or modify stored files, skills, and responses.

Mitigation: Run cost-incurring, upload, and delete calls only when requested, and scope changes to named or task-created resources.

Risk: Adding an unreviewed third-party Go dependency may introduce supply-chain risk.

Mitigation: Review github.com/psyb0t/go-xai before adopting it in a Go project.

## Reference(s):

- [go-xai setup and reference](references/setup.md)
- [go-xai project homepage](https://github.com/psyb0t/go-xai)
- [go-xai ClawHub listing](https://clawhub.ai/psyb0t/skills/go-xai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and an xAI API key to use the client.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
