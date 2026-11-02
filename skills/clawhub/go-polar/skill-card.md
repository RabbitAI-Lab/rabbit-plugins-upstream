## Description:

Unofficial Go client for the Polar API, generated with oapi-codegen from Polar's published OpenAPI document. Package polar (github.com/psyb0t/go-polar) provides typed REST methods for products, customers, subscriptions, checkouts, orders, payments, benefits, usage events, meters, refunds and webhook management. Use when Go code needs the Polar API or already imports go-polar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Polar products and billing operations into Go applications through the unofficial go-polar client. It provides guidance for reading Polar data and making account changes when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-changing operations, including refunds and revocations, can alter Polar account data.

Mitigation: Perform these operations only when requested, and use a token with only the permissions and scopes required.

Risk: Bearer access tokens can expose account access if committed or logged.

Mitigation: Read the token from POLAR_ACCESS_TOKEN and never hardcode, commit, or log it or an Authorization header.

Risk: The unofficial Go dependency is outside the bundled-instructions security review.

Mitigation: Review and pin the dependency before production use, and test billing changes in the sandbox first.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-polar source repository](https://github.com/psyb0t/go-polar)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Polar API requests using the configured environment and access token.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
