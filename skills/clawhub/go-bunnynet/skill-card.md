## Description:

Helps developers write Go code using go-bunnynet, an unofficial client for Bunny.net core API operations including CDN, DNS, statistics, and account management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Bunny.net core API operations into Go projects, including managing CDN pull zones, DNS, and account settings. It does not cover storage file transfers or the separate Stream API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account API keys could be exposed in source code or logs.

Mitigation: Use a least-privilege key stored in the environment or secret management; never hardcode or log it.

Risk: Generated code could modify or delete resources, purge caches, rotate keys, or close an account.

Mitigation: Review generated code and authorize account-changing calls only when explicitly requested.

## Reference(s):

- [go-bunnynet setup and reference](references/setup.md)
- [go-bunnynet package documentation](https://pkg.go.dev/github.com/psyb0t/go-bunnynet)
- [go-bunnynet project homepage](https://github.com/psyb0t/go-bunnynet)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-bunnynet)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated code before running account-changing operations.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
