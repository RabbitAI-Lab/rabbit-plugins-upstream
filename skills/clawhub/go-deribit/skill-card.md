## Description:

Guides agents writing Go code for Deribit REST calls and WebSocket subscriptions using the unofficial go-deribit client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to implement Deribit market-data, trading and account workflows through REST or WebSocket APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated trading, withdrawal, transfer or account-administration calls may affect a live account.

Mitigation: Use testnet first and review each account-changing call before running it against production.

Risk: Credentials used for private API calls may be exposed in source control or logs.

Mitigation: Load DERIBIT_ACCESS_TOKEN from the environment; do not hardcode, commit or log secrets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-deribit)
- [Skill setup and API guidance](references/setup.md)
- [go-deribit library homepage](https://github.com/psyb0t/go-deribit)
- [go-deribit package documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST requests, WebSocket subscriptions and dependency setup.]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
