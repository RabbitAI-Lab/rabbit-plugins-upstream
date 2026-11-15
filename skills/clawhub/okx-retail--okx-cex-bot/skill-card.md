## Description:

Manage Grid bots (spot/contract/coin-margined), DCA Martingale bots (Spot DCA 现货马丁 / Contract DCA 合约马丁), Smart Portfolio bots (智能组合, auto-rebalancing multi-asset portfolio), and Recurring Buy strategies (定投, periodic fixed-amount multi-coin buys) on OKX. Covers create, stop, pause, amend, monitor P&L, TP/SL, margin/investment adjustment, AI-recommended parameters, and recommended zone backtest. Requires API credentials. Not for regular orders (okx-cex-trade), market data (okx-cex-market), or account info (okx-cex-portfolio).

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External OKX users can use the skill to review and manage Grid, DCA, Smart Portfolio, and Recurring Buy bots through the OKX CLI. It guides setup, checks the account profile and trading mode, and documents confirmation and follow-up checks for bot operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags a medium-confidence concern that high-impact actions could be taken without confirmation.

Mitigation: Review the skill before installation and require explicit confirmation of the action and its parameters before any bot write operation.

Risk: The security scan reports incomplete coverage because three local references were unresolved.

Mitigation: Review the unresolved referenced material and check how the installed tool version is controlled before use.

## Reference(s):

- [Grid Bot Command Reference](references/grid-commands.md)
- [DCA Bot Command Reference](references/dca-commands.md)
- [Recurring Buy Command Reference](references/recurring-commands.md)
- [Smart Portfolio Bot Command Reference](references/smart-portfolio-commands.md)
- [Cross-Skill Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Operational guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read bot status or request state-changing operations; authenticated use requires OKX API credentials or an OAuth session.]

## Skill Version(s):

1.5.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
