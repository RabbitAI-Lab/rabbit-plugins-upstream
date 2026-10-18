## Description:

Guides Go developers using an unofficial Kalshi client to access market and account data, stream updates, and sign API requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that reads Kalshi market data, manages an account when explicitly requested, and consumes live market streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing Kalshi API private keys or signed headers could compromise an account.

Mitigation: Keep private keys out of source control and logs; do not print signed headers.

Risk: Orders, transfers, and account or API-key changes can affect a real account.

Mitigation: Use the demo environment while developing and review these actions before running them against a real account.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-kalshi)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go toolchain required for installation and compilation.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
