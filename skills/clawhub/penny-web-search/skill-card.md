## Description:

Penny Web Search guides agents to use PennyAPI for paid real-time web search and structured Places lookup over x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ayoubsalem-spec](https://clawhub.ai/user/ayoubsalem-spec)

### License/Terms of Use:

MIT

## Use Case:

External developers and agents use this skill to retrieve current web information or structured local-business results through PennyAPI when model knowledge may be stale or location data is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned payment-capable npm commands may change behavior between installations.

Mitigation: Use pinned, reviewed versions of AgentCash and the skills installer instead of `@latest`.

Risk: Persistent paid-provider setup can lead to unintended spending.

Mitigation: Use a low-value wallet with explicit payment confirmation and spending limits.

Risk: Search and Places queries may disclose sensitive information to the paid provider.

Mitigation: Do not include secrets or confidential information in search or Places queries.

## Reference(s):

- [PennyAPI homepage](https://pennyregwatch.com)
- [Penny Web Search endpoint](https://pennyregwatch.com/v1/search)
- [Penny Places endpoint](https://pennyregwatch.com/web/places)
- [ClawHub skill page](https://clawhub.ai/ayoubsalem-spec/skills/penny-web-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with shell command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PennyAPI calls cost $0.004 USDC per call on Base and require an x402-capable client.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
