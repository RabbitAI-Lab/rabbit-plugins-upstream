## Description:

Guides Go developers in using an unofficial BTSE client for spot, futures, wallet, earn, OTC, and WebSocket integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to install and work with an unofficial BTSE client for market data, account information, trading, and WebSocket messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production trading, transfers, withdrawals, earn actions, or OTC quote acceptance can change an account.

Mitigation: Use testnet by default and execute production account-changing actions only with explicit user intent.

Risk: Exposed or overprivileged API credentials can allow unintended account access.

Mitigation: Scope keys to minimum permissions, load them from environment variables, and never put them in source code or logs.

## Reference(s):

- [go-btse release on ClawHub](https://clawhub.ai/psyb0t/skills/go-btse)
- [go-btse setup reference](references/setup.md)
- [go-btse project homepage](https://github.com/psyb0t/go-btse)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers testnet and production environments, credentials, and response handling.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
