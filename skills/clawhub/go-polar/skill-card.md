## Description:

Unofficial Go client for the Polar API, generated with oapi-codegen from Polar's published OpenAPI document. Package polar (github.com/psyb0t/go-polar) provides typed REST methods for products, customers, subscriptions, checkouts, orders, payments, benefits, usage events, meters, refunds and webhook management. Use when Go code needs the Polar API or already imports go-polar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when Go projects need typed access to the Polar API, including reading or managing products, customers, subscriptions, orders, and related billing resources. It guides dependency setup, API calls, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Polar bearer token could be exposed if it is committed or included in logs.

Mitigation: Read the token from POLAR_ACCESS_TOKEN, grant only the scopes needed for the task, and avoid logging it or requests containing its Authorization header.

Risk: The security scan had partial coverage because two local path-like references were unresolved.

Mitigation: Review the unresolved references and relevant source before relying on the scan as complete coverage.

Risk: Create, update, delete, refund, and revoke calls can change Polar account data.

Mitigation: Make these calls only when the user requested the specific account change.

## Reference(s):

- [Setup and reference guide](references/setup.md)
- [go-polar repository](https://github.com/psyb0t/go-polar)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)
- [go-polar on ClawHub](https://clawhub.ai/psyb0t/skills/go-polar)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
