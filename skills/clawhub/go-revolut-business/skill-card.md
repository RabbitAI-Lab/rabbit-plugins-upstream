## Description:

Unofficial Go client for the Revolut Business REST API, generated with oapi-codegen. Package revolut (github.com/psyb0t/go-revolut-business) has revolut.NewClientWithResponses, which returns a client with one typed method per endpoint (accounts, transactions, counterparties, payments, transfers and more). Auth is a bearer access token set through revolut.WithRequestEditorFn, and responses decode into JSON200, JSON201 and JSONDefault fields. Use when Go code needs to call the Revolut Business API or already imports go-revolut-business.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls to the Revolut Business API, including account, transaction, counterparty, payment, and transfer operations. It helps them configure bearer-token authentication and select the sandbox or production API endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed bearer access token could allow unauthorized access to Revolut Business data or operations.

Mitigation: Read the token from an environment variable or secure credential store; never hardcode, commit, or log it, and do not print request headers.

Risk: Production payment, transfer, exchange, or delete operations can move funds or remove data.

Mitigation: Use the sandbox while developing and perform financial or destructive operations only when the user explicitly requests them.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go client repository](https://github.com/psyb0t/go-revolut-business)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-revolut-business)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-revolut-business)

## Skill Output:

**Output Type(s):** [Code, API Calls, Configuration instructions, Shell commands]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed API usage examples, authentication setup, and endpoint guidance.]

## Skill Version(s):

0.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
