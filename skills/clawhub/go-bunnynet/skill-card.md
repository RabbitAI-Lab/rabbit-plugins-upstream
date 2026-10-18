## Description:

Helps developers write Go code using the unofficial go-bunnynet client for Bunny.net core API operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations for Bunny.net core account operations, including CDN, DNS, storage zone configuration, statistics and billing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bunny.net account API keys can be exposed in generated code or logs.

Mitigation: Read the key from the environment; do not hardcode, commit or log it.

Risk: Generated account operations can create, change or delete resources, purge caches, rotate keys or affect billing.

Mitigation: Review generated code and run consequential operations only when explicitly requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-bunnynet)
- [go-bunnynet repository and README](https://github.com/psyb0t/go-bunnynet)
- [go-bunnynet package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Guidance, Shell commands]

**Output Format:** [Go source code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers the Bunny.net core API, not storage file transfers or the separate Stream API.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
