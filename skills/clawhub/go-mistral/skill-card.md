## Description:

Guides Go developers in using an unofficial typed client for the Mistral AI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add an unofficial Go client to a project and implement Mistral AI API calls, including chat completions, embeddings, and model listing. It requires Go and a Mistral AI API key for authenticated calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial Go dependency is added to the project.

Mitigation: Review the dependency and its changes before installing or adopting it.

Risk: API calls can expose prompts, files, or credentials to an unintended endpoint.

Mitigation: Use the official Mistral AI base URL unless another endpoint is intended, and keep API keys in environment variables or a secret manager rather than source code or logs.

Risk: Fine-tuning and batch operations may incur charges; uploads and deletes may affect data.

Mitigation: Require explicit user approval before fine-tuning, batch, file upload, or delete operations.

## Reference(s):

- [go-mistral setup and reference](references/setup.md)
- [go-mistral ClawHub release](https://clawhub.ai/psyb0t/skills/go-mistral)
- [go-mistral Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-mistral)
- [go-mistral source repository (skill homepage)](https://github.com/psyb0t/go-mistral)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for Go projects using a Mistral AI API key.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
