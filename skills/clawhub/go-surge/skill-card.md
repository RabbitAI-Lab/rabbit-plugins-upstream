## Description:

Guides Go developers using the unofficial go-surge client to work with the Surge SMS API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Surge SMS messaging, contacts, phone numbers, accounts, and other API operations into Go projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the Surge API token could grant unauthorized API access.

Mitigation: Read SURGE_API_KEY from the environment; never hardcode, commit, or log it.

Risk: Sending messages or changing account resources can have real-world or billing effects.

Mitigation: Review the requested action and confirm destructive or billing-affecting changes before execution.

## Reference(s):

- [go-surge on ClawHub](https://clawhub.ai/psyb0t/skills/go-surge)
- [Setup and reference](references/setup.md)
- [go-surge package documentation](https://pkg.go.dev/github.com/psyb0t/go-surge)
- [go-surge project](https://github.com/psyb0t/go-surge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for using the go-surge client; requires Go and a Surge API token for live API calls.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
