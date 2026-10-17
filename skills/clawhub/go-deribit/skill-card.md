## Description:

Guides Go developers in using an unofficial Deribit client for REST requests and WebSocket subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Deribit market-data, account, trading, and WebSocket integrations to Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private API credentials or tokens may be exposed.

Mitigation: Store tokens in environment variables or a secrets manager; never commit or log them.

Risk: Production orders, withdrawals, transfers, and account changes can affect funds or account access.

Mitigation: Develop against testnet and perform production financial or account actions only when explicitly requested.

## Reference(s):

- [go-deribit skill release](https://clawhub.ai/psyb0t/skills/go-deribit)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go toolchain required; private requests require authenticated credentials.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
