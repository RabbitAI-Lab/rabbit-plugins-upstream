## Description: <br>
Robonet helps agents use Robonet's MCP server to explore market data, create and refine trading strategies, run backtests, and manage live Hyperliquid or Polymarket deployments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickemmons](https://clawhub.ai/user/nickemmons) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and trading teams use this skill to build, test, optimize, and deploy crypto or prediction-market trading strategies through Robonet's authenticated MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live deployment or restart actions can trade real funds without strong confirmation guardrails. <br>
Mitigation: Require a separate explicit confirmation before deployment or restart, and verify symbol, leverage, account, and risk limits before execution. <br>
Risk: The MCP server can use API keys, wallets, vaults, and credit accounts connected to Robonet. <br>
Mitigation: Install only when the publisher and Robonet account context are trusted, use secure API-key handling, and prefer a low-balance or isolated account. <br>
Risk: Generated or optimized trading strategies may backtest well but perform poorly in live markets. <br>
Mitigation: Backtest first across sufficient data and multiple periods, then monitor active deployments so they can be stopped quickly. <br>


## Reference(s): <br>
- [Robonet Skill Page](https://clawhub.ai/nickemmons/skills/robonet-workbench) <br>
- [Robonet MCP Tools Catalog](artifact/shared-references/tool-catalog.md) <br>
- [Robonet Dashboard](https://robonet.finance) <br>
- [Jesse Framework Docs](https://jesse.trade) <br>
- [Allora Network](https://allora.network) <br>
- [Hyperliquid](https://hyperliquid.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with MCP tool calls, tool responses, and generated Python strategy code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include trading strategy code, backtest metrics, deployment identifiers, and account or credit status from authenticated Robonet tools.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
