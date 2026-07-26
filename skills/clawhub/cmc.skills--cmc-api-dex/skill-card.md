## Description: <br>
API reference for CoinMarketCap DEX endpoints including token lookup, pools, transactions, trending, and security analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose CoinMarketCap DEX endpoints, parameters, and curl request patterns for on-chain token lookup, pricing, liquidity, discovery, transaction, and security-analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CoinMarketCap API keys can be exposed if copied directly into prompts, examples, shell history, or shared logs. <br>
Mitigation: Use environment variables or a secret manager for real keys, and avoid pasting production credentials into generated commands. <br>
Risk: Queried token addresses and networks may reveal research or trading interests to CoinMarketCap. <br>
Mitigation: Use this skill only when CoinMarketCap DEX API reference help is intended, and choose API credentials and query practices that fit the sensitivity of the research. <br>
Risk: DEX security and market-data responses can inform trading decisions but do not remove market, contract, liquidity, or scam risk. <br>
Mitigation: Review risk scores, warnings, liquidity, holder concentration, taxes, and ownership flags before acting, and make decisions based on the user's risk tolerance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cmc.skills/skills/cmc-api-dex) <br>
- [DEX Discovery APIs](references/discovery.md) <br>
- [DEX Pairs APIs](references/pairs.md) <br>
- [DEX Platform APIs](references/platforms.md) <br>
- [DEX Security API](references/security.md) <br>
- [DEX Token APIs](references/tokens.md) <br>
- [Common Use Cases](references/use-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with endpoint descriptions, parameter tables, JSON examples, and curl command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API-key header examples, endpoint URLs, query parameters, JSON request bodies, and risk-check guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
