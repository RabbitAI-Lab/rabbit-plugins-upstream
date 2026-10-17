## Description:

Guides Go developers in using an unofficial typed client for Cerebras inference, including completions and model lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on Go applications use this skill to add Cerebras inference calls, handle typed responses and errors, and look up available models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if embedded in code or logged with request headers.

Mitigation: Keep the Cerebras API key in an environment variable; do not commit it or log request headers.

Risk: Prompts sent through the client reach the configured API endpoint.

Mitigation: Confirm the endpoint and avoid sending sensitive prompts without appropriate approval.

Risk: Installing the Go module fetches third-party code.

Mitigation: Confirm that you trust the upstream Go module before installing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-cerebras)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authentication, response handling, and model queries.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
