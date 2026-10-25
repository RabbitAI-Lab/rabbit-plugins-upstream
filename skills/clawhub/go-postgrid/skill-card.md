## Description:

Guides Go developers in using an unofficial PostGrid client for physical mail and address verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations for PostGrid print and mail resources and address verification, including authentication and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing PostGrid API credentials in source code or logs.

Mitigation: Load POSTGRID_API_KEY from the environment; do not hardcode, commit, or log it.

Risk: Live mail, targeted lists, bulk verification, or resource changes can cause unintended actions and charges.

Mitigation: Use a test key in development and require an explicit user request before live, billable, cancel, or delete operations.

Risk: Retrying mail creation after an uncertain response may duplicate physical mail.

Mitigation: Check whether the first request succeeded before retrying creation.

## Reference(s):

- [ClawHub go-postgrid release](https://clawhub.ai/psyb0t/skills/go-postgrid)
- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-postgrid)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for PostGrid authentication, endpoint selection, and response handling.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
