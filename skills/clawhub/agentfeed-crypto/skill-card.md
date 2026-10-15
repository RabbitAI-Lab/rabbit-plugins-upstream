## Description:

Guides agents through AgentFeed's paid crypto market data, token checks, research and compliance lookups, and fixed-purpose content tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seekdaseek](https://clawhub.ai/user/seekdaseek)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve current crypto market data, assess Solana tokens, screen wallets against sanctions lists, and run targeted research or content tasks through AgentFeed. Paid requests require user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API requests can incur charges or be sent to an unexpected payment recipient.

Mitigation: Confirm the listed price and obtain user approval before paying; verify amount, asset, network, and payTo from a fresh 402 challenge.

Risk: Queries and supplied addresses, URLs, emails, domains, or text are sent to AgentFeed.

Mitigation: Share only the data needed for the requested task and ensure the user is comfortable sending it to the service.

Risk: A prepaid API key can be used by anyone who obtains it.

Mitigation: Keep the bearer key out of chats and logs, and obtain approval before buying a key pack.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/seekdaseek/skills/agentfeed-crypto)
- [AgentFeed API documentation](https://x402.ochinimus.app/openapi.json)
- [AgentFeed homepage](https://x402.ochinimus.app)
- [Repository link listed in skill metadata (not verified release provenance)](https://github.com/seekdaseek/agentfeed)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown or plain text with JSON API results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance; paid calls require user approval and return time-sensitive data.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
