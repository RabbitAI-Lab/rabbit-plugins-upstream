## Description:

Unofficial typed Go client and integration guidance for calling the Mistral AI REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or work with Go code that calls Mistral AI endpoints, including chat completions, embeddings, and model listing. It provides typed client usage, authentication, request and response handling, and endpoint discovery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed, or prompts and files could be sent to Mistral without approval.

Mitigation: Keep the key in an environment variable, never commit or log it, and send only approved data to Mistral.

Risk: Fine-tuning or batch jobs can incur charges, and delete operations remove data.

Mitigation: Require explicit user authorization before starting paid jobs or deleting data.

Risk: The client is unofficial and may require review before adoption.

Mitigation: Review the dependency version before adding it to a project.

## Reference(s):

- [Setup and reference guide](artifact/references/setup.md)
- [Go Mistral project](https://github.com/psyb0t/go-mistral)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-mistral)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-mistral)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use environment-variable references for API credentials.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
