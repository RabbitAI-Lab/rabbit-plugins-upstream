## Description: <br>
Blockchain analytics and DeFi intelligence via Einstein's x402 micropayment services for token research, market analysis, whale tracking, smart money tracking, portfolio analysis, security scanning, launchpad monitoring, arbitrage, MEV, and Polymarket data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chuxo](https://clawhub.ai/user/chuxo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to run paid blockchain and DeFi analytics across supported chains, including market, wallet, launchpad, token-risk, MEV, arbitrage, NFT, and prediction-market queries. It is intended for users who can safely manage a dedicated Base USDC wallet for x402 payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a crypto private key and can authorize real USDC payments. <br>
Mitigation: Use a dedicated low-balance Base USDC wallet and do not use a main wallet or a wallet holding significant funds. <br>
Risk: Skipping payment confirmation can allow agent workflows to spend USDC without per-query approval. <br>
Mitigation: Keep payment confirmation enabled for normal agent use and avoid --yes or global auto-confirm unless spending is tightly bounded and monitored. <br>
Risk: Saving configuration to config.json can persist the wallet private key on disk. <br>
Mitigation: Prefer EINSTEIN_X402_PRIVATE_KEY or a secret manager; if config.json is used, restrict file permissions and ensure it is not committed. <br>
Risk: The free epstein-search command sends search terms to DugganUSA rather than the Einstein x402 service. <br>
Mitigation: Avoid submitting sensitive search terms to that command unless disclosure to the external search service is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chuxo/skills/einstein) <br>
- [Publisher profile](https://clawhub.ai/user/chuxo) <br>
- [Einstein homepage](https://emc2ai.io) <br>
- [Services catalog](references/services-catalog.md) <br>
- [Payment guide](references/payment-guide.md) <br>
- [Usage examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON service responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid analytics queries return structured data or AI-analyzed results; free service listing and Epstein file search return text or JSON without x402 payment.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
