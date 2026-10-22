## Description:

Helps developers write Go code using the unofficial go-btse client for BTSE REST and WebSocket APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build Go integrations for BTSE market data, account information, trading, wallets, earn products, OTC quotes, and WebSocket messages. It also helps projects already using go-btse find the appropriate client methods and types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BTSE API credentials could be exposed or granted excessive permissions.

Mitigation: Keep API keys scoped and protected; read them from environment variables and never hardcode, commit, or log them.

Risk: Production orders, transfers, withdrawals, redemptions, or accepted quotes can change a financial account.

Mitigation: Prefer testnet first and perform account-changing actions only when the user explicitly requests them.

## Reference(s):

- [go-btse setup and reference](references/setup.md)
- [go-btse package documentation](https://pkg.go.dev/github.com/psyb0t/go-btse)
- [go-btse project homepage](https://github.com/psyb0t/go-btse)
- [go-btse on ClawHub](https://clawhub.ai/psyb0t/skills/go-btse)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance for REST and WebSocket integrations]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
