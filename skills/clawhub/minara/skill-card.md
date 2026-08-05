## Description: <br>
Crypto trading & wallet, and AI market analysis via Minara CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lowesyang](https://clawhub.ai/user/lowesyang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route crypto wallet, spot trading, perpetual futures, market discovery, AI analysis, x402 payment, and Minara account workflows through the Minara CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route an agent into Minara wallet, trading, balance, account, x402 payment, and perpetual futures workflows. <br>
Mitigation: Install only when this access is intended, require explicit confirmation for every fund-moving operation, and avoid confirmation-bypass flags such as --yes. <br>
Risk: Incorrect recipient, chain, token, or x402 payment details can move funds to the wrong destination. <br>
Mitigation: Verify full wallet addresses, x402 recipients, chains, token contracts, and balances before approving any transaction. <br>
Risk: Autopilot represents live automated trading and can lose funds. <br>
Mitigation: Treat autopilot as live trading, review wallet status before manual perps orders, and disable or avoid autopilot where manual control is required. <br>
Risk: The release includes workspace routing persistence and self-update behavior. <br>
Mitigation: Review and approve writes to agent config or memory files, and inspect CLI or skill update prompts before accepting them. <br>


## Reference(s): <br>
- [Minara homepage](https://minara.ai) <br>
- [ClawHub skill page](https://clawhub.ai/lowesyang/skills/minara) <br>
- [Setup](setup.md) <br>
- [Auth / Account / Config](references/auth.md) <br>
- [Agent Authentication Recovery](references/auth-recovery.md) <br>
- [Balance / Assets](references/balance.md) <br>
- [AI Chat / Ask / Research](references/chat.md) <br>
- [Market Discovery](references/discover.md) <br>
- [Swap (Buy / Sell)](references/swap.md) <br>
- [Transfer / Send / Pay](references/transfer.md) <br>
- [Withdraw](references/withdraw.md) <br>
- [Deposit / Receive](references/deposit.md) <br>
- [Limit Orders](references/limit-order.md) <br>
- [Perps Order (Market / Limit)](references/perps-order.md) <br>
- [Perps Positions / Close / Cancel / Leverage / Trades](references/perps-manage.md) <br>
- [Perps Wallets / Deposit / Withdraw / Fund Records](references/perps-wallet.md) <br>
- [Perps Autopilot](references/perps-autopilot.md) <br>
- [Interactive Commands - Agent Bypass Guide](references/interactive-commands.md) <br>
- [Premium / Subscription](references/premium.md) <br>
- [Minara Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with CLI command execution steps, confirmation tables, and summarized Minara CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fund-moving operations require a separate user confirmation turn; the skill also includes workspace routing configuration guidance.] <br>

## Skill Version(s): <br>
3.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
