## Description: <br>
Analyzes one BTC or ETH derivatives setup using current public Deribit, Hyperliquid, and Polymarket data for read-only strategy research without executing trades or claiming certainty. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frederica123](https://clawhub.ai/user/frederica123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill for read-only BTC or ETH derivatives research, combining public volatility, funding, basis, price-level, and prediction-market context into a strategy-analysis dossier. It supports market review and reassessment planning, not trade execution or investment certainty. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts public Deribit, Hyperliquid, and Polymarket endpoints, so analysis quality depends on source availability, timestamps, rule text, and public quote quality. <br>
Mitigation: Review source availability, timestamps, volatility-surface fit warnings, prediction-market rules, and agreement between independent sources before relying on the analysis. <br>
Risk: The skill saves market snapshots and strategy-card JSON locally, which can create retained market-research records on the user's machine. <br>
Mitigation: Set CRYPTO_STRATEGY_OUTPUT_DIR to an appropriate location and review saved files under local retention and access policies. <br>
Risk: Financial-analysis outputs could be misread as investment advice, exact trade instructions, or expected returns. <br>
Mitigation: Keep outputs framed as not investment advice, preserve setup-fit scores as fit indicators only, and avoid exact option instruments, size, leverage, win rate, payoff ratio, or profit guarantees. <br>
Risk: The release depends on an MCP Python package version range that users should keep patched. <br>
Mitigation: Install a patched MCP dependency version within the disclosed range and review dependency updates before deployment. <br>


## Reference(s): <br>
- [Crypto Market Strategist on ClawHub](https://clawhub.ai/frederica123/skills/crypto-market-strategist) <br>
- [Deribit public API endpoint](https://www.deribit.com/api/v2/public) <br>
- [Hyperliquid public Info API endpoint](https://api.hyperliquid.xyz/info) <br>
- [Polymarket Gamma API endpoint](https://gamma-api.polymarket.com) <br>
- [Polymarket CLOB API endpoint](https://clob.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance backed by JSON analysis and locally saved JSON research bundles] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only BTC or ETH strategy analysis, deterministic setup-fit scores, evidence identifiers, and local strategy-card JSON; does not place orders or request credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
