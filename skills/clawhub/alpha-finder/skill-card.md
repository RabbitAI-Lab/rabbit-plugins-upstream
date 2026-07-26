## Description: <br>
Alpha Finder (x402) helps agents research prediction markets across Polymarket, Kalshi, and other sources to assess probabilities, market sentiment, and arbitrage opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tzannetosgiannis](https://clawhub.ai/user/tzannetosgiannis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and traders use this skill to run paid x402-backed prediction-market research queries across Polymarket, Kalshi, social, code, and web sources for trading research, due diligence, portfolio tracking, and news impact analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a raw Base wallet private key for x402 payment handling. <br>
Mitigation: Use a dedicated low-balance Base wallet, avoid main wallet keys, prefer environment variables over plaintext files, and restrict file permissions for any local config file. <br>
Risk: Each query is sent to an external paid tool and can charge $0.03 USDC. <br>
Mitigation: Confirm the cost model with users before repeated use and monitor wallet balance or spending controls. <br>
Risk: The shell script dynamically fetches and runs an external npm package. <br>
Mitigation: Review the package source and version before use in sensitive environments, and run it only where the wallet key and query content are appropriate to share. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tzannetosgiannis/skills/alpha-finder) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and text market-analysis output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each query uses an external paid x402 tool and may charge $0.03 USDC on Base.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
