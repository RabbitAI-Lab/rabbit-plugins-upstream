## Description:

Unofficial Go client for the Revolut Business REST API, generated with oapi-codegen. Package revolut (github.com/psyb0t/go-revolut-business) has revolut.NewClientWithResponses, which returns a client with one typed method per endpoint (accounts, transactions, counterparties, payments, transfers and more). Auth is a bearer access token set through revolut.WithRequestEditorFn, and responses decode into JSON200, JSON201 and JSONDefault fields. Use when Go code needs to call the Revolut Business API or already imports go-revolut-business.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add or work with a typed Go client for the Revolut Business API, including reading account and transaction data and implementing requested payment or transfer operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was marked partial because a path-like reference did not resolve; its benign verdict is not a guarantee of safety.

Mitigation: Review the referenced setup material and skill contents before installation.

Risk: Payment, transfer, exchange, and delete operations can move money or remove data.

Mitigation: Only call these operations when the user has requested the action, and prefer the sandbox while developing.

Risk: Bearer access tokens could be exposed if they are hardcoded, committed, or logged.

Mitigation: Read tokens from an environment variable or secure credential store, and never log request headers.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-revolut-business)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-revolut-business)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for using the Revolut Business API client in Go.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
