## Description: <br>
Crypto helps OpenClaw agents look up real-time cryptocurrency prices, gas costs, trending tokens, wallet balances, ENS and Basename resolution, token information, chain data, and price conversions through public endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to answer crypto data lookup requests, including token prices, gas estimates, wallet balances, ENS or Basename resolution, token metadata, supported chains, and price conversions. It is intended for data presentation and calculations, not financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, ENS or Basename identifiers, token symbols, and similar lookup terms may be sent to public third-party services. <br>
Mitigation: Use only public lookup data, avoid private keys or seed phrases, and disclose that wallet or name lookups can reveal interest in specific accounts or tokens. <br>
Risk: Crypto prices, gas estimates, balances, and trending-token data can be stale, volatile, or misleading. <br>
Mitigation: Present timestamped data, avoid financial advice, and state that trending status does not indicate safety or investment quality. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/plagtech/skills/crypto-skill) <br>
- [Spraay Gateway](https://gateway.spraay.app) <br>
- [Spraay Docs](https://docs.spraay.app) <br>
- [DexScreener API](https://docs.dexscreener.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and live API or RPC lookup results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; sends public lookup terms such as token symbols, wallet addresses, and ENS or Basename identifiers to third-party services.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
