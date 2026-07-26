## Description: <br>
PayQL helps agents discover live The Graph subgraphs, check per-query USDC pricing, and query on-chain data through x402 payment flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use PayQL to add paid, live on-chain data retrieval for DeFi, DEX, NFT, ENS, token, and governance workflows. It supports a discover, price, and query loop where agents can quote cost before executing paid reads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid queries can spend real USDC from the configured wallet. <br>
Mitigation: Use a dedicated low-balance Base wallet and run the free price check before paid queries. <br>
Risk: A raw private key in harness configuration can be exposed through logs, sync, screenshots, or accidental sharing. <br>
Mitigation: Treat the harness config as secret, never use a primary or reused private key, and consider a managed or harness wallet with spend caps. <br>


## Reference(s): <br>
- [PayQL on ClawHub](https://clawhub.ai/paulieb14/skills/payqlskill) <br>
- [Gateway recipe and examples](references/gateway.md) <br>
- [x402](https://x402.org) <br>
- [Ampersend managed wallet option](https://ampersend.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, GraphQL examples, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents through paid x402 data queries that spend USDC from a user-controlled wallet.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
