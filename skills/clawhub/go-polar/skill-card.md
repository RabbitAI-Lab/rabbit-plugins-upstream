## Description:

Helps Go developers use the unofficial go-polar client to integrate with the Polar API for products, customers, subscriptions, checkouts, billing, and other account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the go-polar dependency, configure authentication, and write code that reads or changes Polar account data when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked Polar access token could expose account data or enable unauthorized actions.

Mitigation: Keep POLAR_ACCESS_TOKEN out of source, logs, and request output; use only the scopes required for the operation.

Risk: Create, update, delete, refund, revoke, or webhook operations can change a real Polar account.

Mitigation: Prefer the sandbox for testing and confirm the requested action and environment before running it against production.

## Reference(s):

- [go-polar on ClawHub](https://clawhub.ai/psyb0t/skills/go-polar)
- [go-polar project homepage (listed in skill)](https://github.com/psyb0t/go-polar)
- [Setup and usage reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Text and Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide edits to a Go project; does not itself produce Polar API results.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
