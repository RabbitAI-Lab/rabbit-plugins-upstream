## Description:

An unofficial, typed Go client generated from Polar's published OpenAPI document that helps Go projects call Polar API endpoints for products, customers, subscriptions, checkouts, orders, payments, benefits, usage events, meters, refunds, and webhook management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Go client in Go projects to call Polar API endpoints for products, customers, subscriptions, orders, checkouts, and related billing operations. It also guides installation, authentication, pagination, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Polar access token grants access to account operations and could be exposed through source code, logs, or requests.

Mitigation: Read the token from the environment, use only the required token type and scopes, and never hardcode, commit, or log it or print Authorization headers.

Risk: Create, update, delete, refund, and revoke operations can change Polar account data.

Mitigation: Call write operations only when requested, and use the sandbox environment when that is the environment the user requested.

Risk: The security scan was partial because two references were unresolved, leaving some evidence incomplete.

Mitigation: Before installing, consider whether you trust the publisher and are comfortable providing a Polar access token for the intended operations.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-polar on GitHub](https://github.com/psyb0t/go-polar)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise setup and usage guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated requests that access or change Polar account data.]

## Skill Version(s):

0.3.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
