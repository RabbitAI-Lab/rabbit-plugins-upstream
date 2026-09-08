## Description:

Zyfai Yield Automation helps agents guide users through wallet-connected Zyfai SDK workflows for earning passive DeFi yield on Ethereum Mainnet, Base, and Arbitrum with USDC, WETH, and EURC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pauldefi](https://clawhub.ai/user/pauldefi)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to configure Zyfai SDK wallet connections and guide deposit, withdrawal, portfolio, strategy, APY, and agent-registration workflows for DeFi yield automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-connected actions can move real assets into DeFi protocols and expose users to smart-contract, liquidity, backend, and market risks.

Mitigation: Require explicit user approval before deposits, withdrawals, strategy changes, cross-chain settings, or identity registration, and present chain, asset, amount, destination, and minimum-balance details before execution.

Risk: Raw private keys or poorly protected API keys can compromise wallet control or service access.

Mitigation: Prefer wallet-provider, KMS-backed, or wallet-as-a-service signing, store API keys securely, and avoid hardcoded or long-lived raw private keys in production.

Risk: The identity-registry capability creates an additional on-chain action outside the core yield flow.

Mitigation: Call agent identity registration only after a specific user request and confirmation of the smart wallet address and target chain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pauldefi/skills/zyfai-sdk)
- [Zyfai documentation](https://docs.zyf.ai)
- [Zyfai API key portal](https://sma.zyf.ai)
- [SDK API key creation endpoint](https://sma.zyf.ai/api/sdk-api-keys/create)
- [Zyfai SDK demo](https://github.com/ondefy/zyfai-sdk-demo)
- [Zyfai MCP server](https://mcp.zyf.ai/mcp)
- [Agent registration metadata](https://www.zyf.ai/.well-known/agent-registration.json)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with TypeScript, JSON, HTTP, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet connection, API key, deposit, withdrawal, portfolio, strategy, APY, and agent-registration examples for Zyfai SDK workflows.]

## Skill Version(s):

1.0.13 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
