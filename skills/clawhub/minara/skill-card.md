## Description: <br>
Minara helps agents use the Minara CLI for crypto trading, wallet operations, perpetual futures, AI market analysis, market discovery, x402 payments, subscriptions, and premium credit workflows across EVM, Solana, and Hyperliquid contexts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lowesyang](https://clawhub.ai/user/lowesyang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Minara to route finance, crypto, wallet, market-data, subscription, and trading requests to the Minara CLI. The skill is intended for authenticated account workflows and requires explicit confirmation before fund-moving operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access authenticated crypto account data and assist with real trades, transfers, withdrawals, subscriptions, and perpetual futures workflows. <br>
Mitigation: Install only for users who intend to connect Minara to financial accounts; keep confirmation and Touch ID enabled and avoid --yes on fund-moving commands. <br>
Risk: Fund-moving commands can transfer assets or open, close, or modify trading positions. <br>
Mitigation: Require balance checks, explicit user confirmation, and a separate execution turn for each fund-moving action. <br>
Risk: Workspace setup can change future agent routing by editing CLAUDE.md, AGENTS.md, or MEMORY.md. <br>
Mitigation: Review and approve proposed workspace configuration edits before they are made. <br>
Risk: Perps autopilot may automate trading behavior with financial loss exposure. <br>
Mitigation: Enable autopilot only with risk limits the user understands, and check wallet/autopilot state before perps order confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lowesyang/skills/minara) <br>
- [Minara homepage](https://minara.ai) <br>
- [Workspace integration](artifact/setup.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Auth / Account / Config](artifact/references/auth.md) <br>
- [Balance / Assets](artifact/references/balance.md) <br>
- [AI Chat / Ask / Research](artifact/references/chat.md) <br>
- [Market Discovery](artifact/references/discover.md) <br>
- [Deposit / Receive](artifact/references/deposit.md) <br>
- [Swap (Buy / Sell)](artifact/references/swap.md) <br>
- [Transfer / Send / Pay](artifact/references/transfer.md) <br>
- [Withdraw](artifact/references/withdraw.md) <br>
- [Spot Limit Orders](artifact/references/limit-order.md) <br>
- [Perps Order (Market / Limit)](artifact/references/perps-order.md) <br>
- [Perps Positions / Close / Cancel / Leverage / Trades](artifact/references/perps-manage.md) <br>
- [Perps Wallets / Deposit / Withdraw / Fund Records](artifact/references/perps-wallet.md) <br>
- [Perps Autopilot / AI Analysis](artifact/references/perps-autopilot.md) <br>
- [Premium / Subscription](artifact/references/premium.md) <br>
- [Minara Examples](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI command execution steps, confirmation prompts, and structured result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke authenticated Minara CLI workflows and may propose workspace routing configuration updates.] <br>

## Skill Version(s): <br>
3.0.3 (source: server release metadata; artifact frontmatter shows 3.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
