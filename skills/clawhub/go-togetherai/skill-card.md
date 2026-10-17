## Description:

Guides Go developers in using an unofficial typed client for the Together AI REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Together AI models and services into applications, including chat completions, embeddings, and model listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed API key could allow unauthorized requests.

Mitigation: Use TOGETHER_API_KEY from the environment; do not commit, hardcode, or log the key.

Risk: Prompts or files sent to Together AI may contain sensitive information.

Mitigation: Send sensitive prompts or files only when intended and appropriate.

Risk: Fine-tuning, dedicated resources, and delete operations may incur charges or remove data.

Mitigation: Confirm with the user before paid or destructive operations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-togetherai)
- [Go client project homepage](https://github.com/psyb0t/go-togetherai)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authenticated Together AI API requests and response handling.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
