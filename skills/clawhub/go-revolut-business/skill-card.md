## Description:

Guides Go developers in using an unofficial typed client for the Revolut Business API, including authentication, API calls, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add a Go client for Revolut Business accounts, transactions, counterparties, payments, and transfers, with token-based authentication and typed responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked Revolut access token could expose Business API access.

Mitigation: Keep REVOLUT_ACCESS_TOKEN out of source control and logs; read it from the environment.

Risk: Payment, transfer, exchange, or delete calls may move money or remove data.

Mitigation: Develop in the sandbox and require explicit user confirmation before these calls.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go client project linked by the skill](https://github.com/psyb0t/go-revolut-business)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-revolut-business)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers token handling, sandbox use, and checking typed API responses.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
