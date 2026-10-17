## Description:

Guides Go developers in using the unofficial go-julep client to make typed requests to the Julep API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to a project, authenticate with an API key, and implement Julep agent, session, task, and related API calls with typed responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Julep API key could permit unauthorized account access.

Mitigation: Read JULEP_API_KEY from the environment; do not hardcode, commit, or log it.

Risk: Generated delete, update, secret, file, execution, or billing-impacting calls can change the Julep account.

Mitigation: Review generated code before running it and perform account-changing operations only when the user requests them.

## Reference(s):

- [go-julep setup and reference](artifact/references/setup.md)
- [go-julep on ClawHub](https://clawhub.ai/psyb0t/skills/go-julep)
- [Project homepage listed in skill metadata](https://github.com/psyb0t/go-julep)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers API-key authentication and typed Julep response handling.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
