## Description: <br>
Query DeFi portfolios, token holdings, NFTs, transactions, and prices across 50+ chains via the Zapper API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zivhm](https://clawhub.ai/user/zivhm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and wallet operators use this skill to query wallet balances, DeFi positions, NFT holdings, token prices, recent transactions, and claimable rewards through Zapper's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses and lookup activity are sent to Zapper when the skill queries portfolio, token, NFT, transaction, price, or reward data. <br>
Mitigation: Install only if this sharing is acceptable, pass a specific address when you do not intend to query every configured wallet, and keep wallet configuration private. <br>
Risk: The skill requires a Zapper API key for API access. <br>
Mitigation: Use a dedicated Zapper API key and keep the key out of shared files and logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zivhm/skills/openclaw-zapper-api) <br>
- [Zapper homepage](https://zapper.xyz) <br>
- [Zapper developer dashboard](https://zapper.xyz/developers) <br>
- [Zapper API documentation](https://build.zapper.xyz/docs/api/) <br>
- [Zapper GraphQL API reference](references/API.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Plain text summaries or raw JSON from Python CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a ZAPPER_API_KEY; may use wallet labels from ~/.config/zapper/addresses.json; transaction history is limited to 30 days.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
