## Description: <br>
Detect mispriced correlations between Polymarket prediction markets. Cross-market arbitrage finder for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sbaker5](https://clawhub.ai/user/sbaker5) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External agents and developers use PolyEdge to compare two Polymarket prediction markets, estimate correlation-driven mispricing, and receive a confidence-rated trading signal or hold/skip result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hosted or deployed API use can make outbound calls to Polymarket, Base RPC providers, BaseScan, and api.nshrt.com, and may require USDC payment for requests. <br>
Mitigation: Use the local analyzer for market comparison when payment or outbound service use is not desired; confirm network and payment expectations before hosted API use. <br>
Risk: The dashboard can expose public wallet and payment activity if deployed without authentication. <br>
Mitigation: Limit dashboard exposure, review wallet visibility before deployment, and avoid using sensitive wallet infrastructure for public dashboards. <br>
Risk: Correlation estimates are rough, rely on manually curated or category-level patterns, and do not account for market liquidity or slippage. <br>
Mitigation: Treat signals as decision support only and independently review market conditions, liquidity, and trading risk before acting. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/sbaker5/skills/polyedge) <br>
- [PolyEdge hosted API](https://api.nshrt.com/) <br>
- [PolyEdge dashboard](https://api.nshrt.com/dashboard) <br>
- [Polymarket Gamma API](https://gamma-api.polymarket.com) <br>
- [BaseScan API](https://api.basescan.org/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON analysis with optional Markdown instructions and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Correlation outputs include market summaries, estimated mispricing, confidence, and action signals such as HOLD, SKIP, BUY_YES_B, or BUY_NO_B.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata; artifact frontmatter is 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
