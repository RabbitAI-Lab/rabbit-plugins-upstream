## Description:

Guides Go developers in using an unofficial typed client for the Intercom REST API to access and manage workspace resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Intercom contacts, conversations, messages, and other workspace resources into their applications, including requested updates and messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom credentials could be exposed in source code, logs, or shared output.

Mitigation: Use a least-privilege token from the environment; do not commit, log, or display it.

Risk: Generated requests could send messages, change customer data, or delete workspace resources.

Mitigation: Review code and requests before execution, and limit actions to the resources the user requested.

## Reference(s):

- [go-intercom release on ClawHub](https://clawhub.ai/psyb0t/skills/go-intercom)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Go project and an Intercom access token with appropriate scopes.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
