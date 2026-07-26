## Description: <br>
Web3 Trader helps agents prepare DEX swap and Hyperliquid trading workflows by requesting quotes, building transaction data, generating hosted swap previews or QR codes, and guiding users to review and sign transactions in their own wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bevanding](https://clawhub.ai/user/bevanding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare crypto swap and trading actions, compare quotes, generate transaction previews, and route users to wallet confirmation without the agent holding private keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill has real swap functionality and that its documentation overstates some high-risk automated trading features. <br>
Mitigation: Review the exact trade flow before use, verify every wallet prompt manually, and do not rely on advertised Hyperliquid or agent-wallet controls unless the relevant implementation is supplied and audited. <br>
Risk: Hosted preview links, QR codes, wallet addresses, and trade parameters can affect real crypto transactions. <br>
Mitigation: Treat those values as sensitive, confirm destination addresses, amounts, slippage, gas, and route details in the wallet, and start with small trades or test flows. <br>
Risk: The security guidance warns against placing trading private keys in ordinary environment variables. <br>
Mitigation: Do not provide private keys to the agent or local environment; use wallet-based signing or managed secret storage with strict limits. <br>


## Reference(s): <br>
- [Web3 Trader Skill Page](https://clawhub.ai/bevanding/web3-trader) <br>
- [MCP Remote Mode Reference](references/mcp-mode.md) <br>
- [Local CLI Mode Reference](references/local-cli.md) <br>
- [Security Guidelines](references/SECURITY.md) <br>
- [Configuration Example](references/config.example.yaml) <br>
- [Antalpha MCP Server](https://mcp-skills.ai.antalpha.com/mcp) <br>
- [0x Swap API Security](https://docs.0x.org/0x-swap-api/security) <br>
- [EIP-681 Standard](https://eips.ethereum.org/EIPS/eip-681) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown trade previews, JSON-style tool arguments and responses, shell commands, configuration snippets, and generated QR-code image guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference hosted swap preview URLs and local files for generated swap pages or QR codes.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
