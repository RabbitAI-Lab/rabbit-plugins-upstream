## Description: <br>
Earn yield on USDC by supplying to the Moonwell Flagship USDC vault on Base. Use when depositing USDC, withdrawing from the vault, checking position/APY, or generating yield reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gekkoai001](https://clawhub.ai/user/gekkoai001) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to manage a Base wallet's USDC yield workflow: configure a wallet, deposit to or withdraw from the Moonwell Flagship USDC vault, check position/APY, generate reports, and compound WELL/MORPHO rewards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sign real-money DeFi transactions from a hot wallet. <br>
Mitigation: Use a dedicated Base wallet with limited funds and manually review approvals, contract targets, transaction previews, and amounts before executing commands. <br>
Risk: The compounding command can move funds using third-party swap data with limited validation. <br>
Mitigation: Keep unrelated USDC and reward tokens out of the wallet before compounding, and review swap routes, slippage, token approvals, and destination contracts before use. <br>
Risk: Wallet configuration depends on a private key available at runtime. <br>
Mitigation: Store the private key only in the intended environment variable, avoid committing it to files or shell history, and rotate the wallet if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gekkoai001/skills/gekkoai-yield) <br>
- [Publisher profile](https://clawhub.ai/user/gekkoai001) <br>
- [Base RPC endpoint](https://mainnet.base.org) <br>
- [Odos quote API endpoint](https://api.odos.xyz/sor/quote/v2) <br>
- [Odos assemble API endpoint](https://api.odos.xyz/sor/assemble) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text, Markdown-style reports, plain text, and JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can initiate Base transactions for deposits, withdrawals, token approvals, reward swaps, and vault compounding when run with a configured wallet.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
