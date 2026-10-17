## Description:

Guides Go developers in using an unofficial typed client to call the Mistral AI REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and configure the go-mistral client for chat completions, embeddings, model listing, and other Mistral AI operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external Go dependency must be installed and trusted.

Mitigation: Review the Go module before adding it to a project.

Risk: Prompts and files sent through the client go to Mistral AI; the API key grants access to the service.

Mitigation: Share only intended data, keep MISTRAL_API_KEY in an environment variable or secret manager, and never commit or log it.

Risk: Fine-tuning and batch jobs can incur charges, and delete operations can remove data.

Mitigation: Run cost-incurring or delete operations only when intentionally requested.

## Reference(s):

- [go-mistral on ClawHub](https://clawhub.ai/psyb0t/skills/go-mistral)
- [go-mistral setup and reference](references/setup.md)
- [go-mistral project homepage](https://github.com/psyb0t/go-mistral)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers bearer-token authentication, typed API calls, and response handling.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
