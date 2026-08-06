## Description:

Get live on-chain data from The Graph through paid GraphQL subgraph queries over x402, using USDC from a wallet controlled by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use PayQL to discover live The Graph subgraphs, quote USDC pricing, and run paid read-only GraphQL queries for on-chain data without managing an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid queries spend real USDC from the configured wallet, and repeated agent-driven queries can spend the wallet balance over time.

Mitigation: Use a dedicated low-balance Base wallet or a managed wallet with spend controls, and keep PAYQL_MAX_USD_PER_QUERY low.

Risk: PAYQL_PRIVATE_KEY is a financial secret that can spend wallet USDC if exposed through harness configuration, logs, sync, screenshots, or shared chats.

Mitigation: Never use a primary, valuable, or reused wallet key; keep the private key out of commits and shared channels, or use a harness-managed wallet.

## Reference(s):

- [The Graph x402 gateway recipe](references/gateway.md)
- [PayQL ClawHub listing](https://clawhub.ai/paulieb14/skills/payqlskill)
- [PayQL repository](https://github.com/PaulieB14/payql)
- [x402 protocol](https://x402.org)
- [Ampersend managed wallet option](https://ampersend.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, GraphQL, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include subgraph discovery steps, free price checks, paid query requests, wallet status guidance, and settlement receipt interpretation.]

## Skill Version(s):

0.1.5 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
