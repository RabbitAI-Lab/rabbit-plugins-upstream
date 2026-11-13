## Description:

Unofficial Go client for the Polar API, generated with oapi-codegen from Polar's published OpenAPI document. Package polar (github.com/psyb0t/go-polar) provides typed REST methods for products, customers, subscriptions, checkouts, orders, payments, benefits, usage events, meters, refunds and webhook management. Use when Go code needs the Polar API or already imports go-polar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate a Go application with Polar's products, customers, subscriptions, orders, checkout and billing APIs. It guides client setup, typed requests and responses, pagination, and account operations requested by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Polar access token can authorize access to account data and operations that create, update, delete, refund, or revoke resources; the security scan was partial with medium confidence.

Mitigation: Use only the token type and scopes required for the requested operation, store it in POLAR_ACCESS_TOKEN, and never hardcode, commit, or log it. Review the unresolved references and use Polar's sandbox environment when appropriate.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-polar source repository](https://github.com/psyb0t/go-polar)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-polar)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
