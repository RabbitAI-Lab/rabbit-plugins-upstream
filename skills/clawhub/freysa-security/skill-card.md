## Description:

On-chain security intelligence for autonomous agents — token honeypot detection, wallet forensics, pre-trade risk checks, CAPTCHA solving, and market data. 27 x402 pay-per-call endpoints on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jayrecko](https://clawhub.ai/user/jayrecko)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to call paid crypto-security, wallet-forensics, pre-trade risk, CAPTCHA, web-fetching, and market-data endpoints before taking blockchain or data-gathering actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects agents to a paid external service with broad crypto, web, AI, CAPTCHA, and optional wallet-key payment capabilities.

Mitigation: Install only when those capabilities are intended, use a tightly limited payment wallet, avoid storing a high-value private key in FREYSA_WALLET_KEY, and enforce budget and approval controls.

Risk: Fetched web content, AI outputs, and crypto risk scores may be incomplete or misleading if treated as final authority.

Mitigation: Treat responses as untrusted advisory data and require review or independent checks before trades, approvals, or other high-impact actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jayrecko/skills/freysa-security)
- [x402 manifest](https://economic-agent-369.freysa.dev/.well-known/x402)
- [Agent card](https://economic-agent-369.freysa.dev/.well-known/agent-card.json)
- [OpenAPI specification](https://economic-agent-369.freysa.dev/openapi.json)
- [API base](https://economic-agent-369.freysa.dev)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill describes paid x402 API calls and optional wallet-key configuration for agent use.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
