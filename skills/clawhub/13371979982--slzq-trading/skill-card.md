## Description:

三立期货AI交易助手 helps an agent use 三立智期 futures APIs to retrieve market data, account state, positions, orders, news, and holding rankings, and to support simulated trading plus user-confirmed live cloud orders and stop-profit/stop-loss workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[13371979982](https://clawhub.ai/user/13371979982)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to 三立智期 for Chinese futures market lookup, simulated account onboarding, account and order queries, and explicitly confirmed trading operations. It is intended to keep live trading actions user-directed and to route trigger-based live orders to server-side cloud order workflows rather than agent polling.

### Deployment Geography for Use:

Global; service use depends on access to 三立智期 accounts, the configured API endpoint, and applicable futures-trading eligibility.

## Known Risks and Mitigations:

Risk: The skill can persist trading keys and access futures-trading account data.

Mitigation: Install only when account access is intended, protect configured keys, and rotate any key that may have been exposed.

Risk: The skill can affect live trading accounts when configured for live use.

Mitigation: Keep the environment in sim mode unless the user understands live-trading risk, and require explicit user confirmation before any live order, modification, or cancellation.

Risk: Custom or plaintext API domains can redirect sensitive trading traffic to an untrusted endpoint.

Mitigation: Use the default HTTPS API endpoint unless a custom endpoint is fully trusted.

Risk: Package text restricts independent verification of the provider.

Mitigation: Verify the company through regulator-controlled sources before relying on provider claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/13371979982/skills/slzq-trading)
- [Publisher profile](https://clawhub.ai/user/13371979982)
- [Usage notes](artifact/references/usage-notes.md)
- [Open API index](artifact/references/api.md)
- [OpenAPI specification](artifact/references/openapi.yaml)
- [MCP runtime README](artifact/runtime/mcp/README.md)
- [Company FAQ](artifact/references/company-faq.md)
- [Official company website](https://www.sxslqh.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with structured MCP or HTTP tool-call instructions and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SLZQ_OPENCLAW_API_KEY, SLZQ_OPENCLAW_DOMAIN, and SLZQ_OPENCLAW_ENV; unauthenticated onboarding can issue a simulated-trading key after risk disclosure and SMS verification.]

## Skill Version(s):

1.5.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
