## Description:

Guides Go developers using the unofficial go-ibkr client to access Interactive Brokers accounts, market data, and orders through the Web API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code for Interactive Brokers Web API account and portfolio queries, market data lookups, and user-authorized order management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order actions can affect a real brokerage account.

Mitigation: Require the user's explicit request for each order action and use paper trading during development.

Risk: Exposed OAuth tokens can allow unauthorized account access.

Mitigation: Keep tokens out of source code and logs; load them from a protected environment or the user's token flow.

Risk: Disabling TLS verification beyond a local gateway can expose brokerage traffic.

Mitigation: Limit any verification bypass to a tightly controlled local Client Portal Gateway; verify TLS for other hosts.

## Reference(s):

- [Go Ibkr setup and reference](references/setup.md)
- [Go Ibkr project homepage](https://github.com/psyb0t/go-ibkr)
- [Go Ibkr on ClawHub](https://clawhub.ai/psyb0t/skills/go-ibkr)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Text and Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers local gateway or OAuth authentication and parsed API responses.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
