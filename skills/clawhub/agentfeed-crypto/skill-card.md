## Description:

Guides agents in accessing paid AgentFeed market data, token checks, sanctions lookups, and fixed-purpose tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seekdaseek](https://clawhub.ai/user/seekdaseek)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can guide agents to retrieve live crypto market data, check tokens and wallets, and use paid research or language tools. The skill explains the API's payment and prepaid-key options; it does not place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid calls or prepaid-key purchases can incur unexpected charges.

Mitigation: Get approval first; check the route and current price, verify the recipient in a fresh payment challenge, and set a spending cap.

Risk: A leaked prepaid API key can be used to spend its balance.

Mitigation: Keep the key out of chats and logs and store it as a secret.

## Reference(s):

- [AgentFeed API documentation](https://x402.ochinimus.app/openapi.json)
- [AgentFeed homepage](https://x402.ochinimus.app)
- [AgentFeed repository](https://github.com/seekdaseek/agentfeed)
- [ClawHub skill listing](https://clawhub.ai/seekdaseek/skills/agentfeed-crypto)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown instructions and HTTP examples; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route-specific query parameters and payment options]

## Skill Version(s):

1.3.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
