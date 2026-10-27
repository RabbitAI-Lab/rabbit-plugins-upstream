## Description:

Guides Go developers using the unofficial go-polar client to integrate with the Polar API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and work with an unofficial typed client for Polar products, customers, subscriptions, billing, and other API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Polar access token with excessive privileges can expose account data or permit unintended changes.

Mitigation: Use a least-privilege token for the requested operation; keep it out of code, logs, and shared output.

Risk: Create, update, delete, refund, revoke, or webhook operations can change Polar account data.

Mitigation: Review each requested account-changing action before execution and prefer the sandbox for testing.

## Reference(s):

- [go-polar project homepage](https://github.com/psyb0t/go-polar)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)
- [Setup and usage reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains token handling, API responses, and pagination.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
