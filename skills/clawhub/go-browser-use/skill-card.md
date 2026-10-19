## Description:

Helps developers write Go integrations with the unofficial go-browser-use client for Browser Use Cloud API v4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build Go applications that create and monitor Browser Use Cloud runs and manage sessions, browsers, files, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client is unofficial and interacts with a paid cloud account.

Mitigation: Use it only when the user intends to use Browser Use Cloud from Go; review account-impacting actions before executing them.

Risk: An exposed API key could grant unauthorized account access.

Mitigation: Provide the key through the environment or a secret store; never hardcode or log it.

Risk: Runs, files, profiles, integrations, and deletion or purge actions can affect account state or incur charges.

Mitigation: Perform only user-requested operations and confirm destructive or paid actions before proceeding.

## Reference(s):

- [ClawHub go-browser-use release](https://clawhub.ai/psyb0t/skills/go-browser-use)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-browser-use)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Browser Use Cloud API key.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
