## Description:

An unofficial, typed Go client for accessing Polar API resources from Go applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Polar API calls to Go applications, including operations for products, customers, subscriptions, payments, and billing. It is useful when a project already uses github.com/psyb0t/go-polar or needs an unofficial Polar client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer access tokens could be exposed if hardcoded, committed, or logged.

Mitigation: Read the token from POLAR_ACCESS_TOKEN and never print or log requests containing the Authorization header.

Risk: Create, update, delete, refund, and revoke operations can change Polar account data.

Mitigation: Perform these operations only when the user requested the change, and use the environment and token scopes they specified.

Risk: The security scan was partial because two local references could not be resolved.

Mitigation: Review the skill and verify any unresolved references before installation or use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)
- [Project repository](https://github.com/psyb0t/go-polar)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Polar API; account-changing operations require the user's request.]

## Skill Version(s):

0.3.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
