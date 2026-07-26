## Description: <br>
Supports OKX CEX trading workflows for placing, amending, canceling, and monitoring spot, swap, futures, options, and event-contract orders through the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to guide OKX CLI order workflows across spot, derivatives, options, and event contracts. It is intended for authenticated OKX accounts and includes demo/live mode checks, order confirmation steps, and post-trade verification guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide actions that connect to live OKX credentials and may place real trades. <br>
Mitigation: Use demo mode first, confirm live versus demo mode, and verify instrument, side, size, order type, leverage, and profile before any execution. <br>
Risk: Trade-direction suggestions for event contracts could be mistaken for financial advice. <br>
Mitigation: Treat event-contract UP/DOWN recommendations as decision support only and require the user to make the final trading choice. <br>
Risk: Market-data analysis scope boundaries may be unclear. <br>
Mitigation: Route market data, balances, P&L, and bot workflows to the appropriate companion skills before using this trading skill for order actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/numpy0001/okx-cex-trade) <br>
- [OKX homepage](https://www.okx.com) <br>
- [Trade Workflows & Examples](artifact/references/workflows.md) <br>
- [MCP Tool Reference & Output Conventions](artifact/references/templates.md) <br>
- [Spot Command Reference](artifact/references/spot-commands.md) <br>
- [Swap / Perpetual Command Reference](artifact/references/swap-commands.md) <br>
- [Futures / Delivery Command Reference](artifact/references/futures-commands.md) <br>
- [Options Command Reference](artifact/references/options-commands.md) <br>
- [Event Contract Commands - Full Parameter Reference](artifact/references/event-commands.md) <br>
- [Event Contract Workflows - Multi-Step Trading Scenarios](artifact/references/event-workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline OKX CLI commands, checklists, and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live/demo mode tags, profile references, confirmation prompts, and post-command verification steps.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
