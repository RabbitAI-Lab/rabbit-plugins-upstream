## Description:

Provides an unofficial typed Go client for Polar API operations, including products, customers, subscriptions, payments, and webhook management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the unofficial go-polar package to Go projects and call Polar APIs for commerce and billing workflows. It guides authentication, environment selection, request and response handling, and pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Polar bearer tokens could be exposed through source code, logs, or request output.

Mitigation: Read tokens from the environment, never hardcode or log them, and use the minimum required scopes.

Risk: Create, update, delete, refund, and revoke operations can change Polar account data.

Mitigation: Run account-changing operations only when the user explicitly requests them; use the sandbox when testing.

Risk: The client is unofficial, and this review covers the bundled guidance rather than its downloaded dependency.

Mitigation: Review and pin the external Go dependency before production use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-polar package documentation](https://pkg.go.dev/github.com/psyb0t/go-polar)
- [go-polar project homepage](https://github.com/psyb0t/go-polar)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the generated Go client; callers handle token refresh and list pagination.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
