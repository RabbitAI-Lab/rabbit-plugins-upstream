## Description: <br>
CornerStone MCP x402 skill for agents provides payment-protected tools for stock predictions, backtests, bank linking, and agent or borrower scoring with Aptos and EVM payment flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[josephrp](https://clawhub.ai/user/josephrp) <br>

### License/Terms of Use: <br>
GPL-2.0-only with Responsible AI License (RAIL) terms <br>


## Use Case: <br>
External developers and autonomous agent operators use this skill to connect agents to x402-protected financial MCP tools, manage local Aptos and EVM wallets, attest wallets, and call paid prediction, backtest, bank-linking, and score APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and use local crypto wallets for paid MCP tools. <br>
Mitigation: Use dedicated low-balance wallets, avoid mainnet keys unless required, and require human confirmation before any transaction. <br>
Risk: Bundled Moltbook files and broad transfer, swap, and contract helpers expand the behavior beyond the core x402 finance tools. <br>
Mitigation: Review or remove unrelated bundled files and unused transaction helpers before deployment. <br>
Risk: Runtime self-updates from remote curl downloads can change executable behavior after review. <br>
Mitigation: Disable or block runtime self-update flows in controlled deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/josephrp/skills/autonomous-agent) <br>
- [Clawdis homepage metadata](https://github.com/FinTechTonic/autonomous-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-like tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool results may include wallet addresses, balances, payment receipts, prediction data, backtest metrics, bank-link tokens, or score values.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
