## Description:

Guides Go developers in using an unofficial typed client for the Revolut Business API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Revolut Business accounts, transactions, counterparties, payments, and transfers into their applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revolut access tokens are sensitive financial credentials.

Mitigation: Read tokens from the environment; do not hardcode, commit, or log them.

Risk: Payment, transfer, exchange, or delete operations can move money or remove data.

Mitigation: Prefer the sandbox during development and require explicit user confirmation before writing code for these operations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-revolut-business)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-revolut-business)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
