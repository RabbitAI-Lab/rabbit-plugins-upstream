## Description: <br>
Earn yield on USDC by supplying to the Moonwell Flagship USDC vault on Base. Use when depositing USDC, withdrawing from the vault, checking position/APY, or generating yield reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergey1997](https://clawhub.ai/user/sergey1997) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and DeFi users use this skill to configure a wallet, check USDC vault position and APY, deposit or withdraw USDC, auto-compound rewards, and generate yield reports for the Moonwell Flagship USDC vault on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill manages real funds through a hot wallet and can approve tokens or submit live Base transactions. <br>
Mitigation: Use a dedicated wallet with limited funds, keep only intended assets available, and review transaction previews before execution. <br>
Risk: The auto-compound path uses Odos to assemble swap transactions before depositing USDC back into the vault. <br>
Mitigation: Review Odos transaction details and expected outputs before allowing an agent to run compounding. <br>
Risk: Security evidence flags broad transaction-signing authority with limited confirmation safeguards. <br>
Mitigation: Require human approval for deposits, withdrawals, approvals, and compounding, especially when balances or routes differ from expectations. <br>


## Reference(s): <br>
- [Gekko Yield on ClawHub](https://clawhub.ai/sergey1997/skills/gekko-yield) <br>
- [Base RPC endpoint](https://mainnet.base.org) <br>
- [Odos quote API](https://api.odos.xyz/sor/quote/v2) <br>
- [Odos assemble API](https://api.odos.xyz/sor/assemble) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate live blockchain transaction prompts, wallet configuration guidance, and position or yield report summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
