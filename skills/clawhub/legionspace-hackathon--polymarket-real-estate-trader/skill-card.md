## Description: <br>
Trades Polymarket prediction markets on housing prices, mortgage rates, Fed rate decisions, real estate crash scenarios, and regional property market milestones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to run a configurable Polymarket strategy for housing and macro-rate prediction markets, starting in paper mode and optionally enabling live orders after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Simmer trading API key, which grants trading authority. <br>
Mitigation: Install only when the key can be stored securely and restrict access to environments that are authorized to operate the trading account. <br>
Risk: Running the skill with the live flag can place real Polymarket orders using USDC. <br>
Mitigation: Use the default paper-trading mode first, then review position size, spread, days-to-resolution, and maximum-position settings before enabling live mode. <br>
Risk: Prediction-market signals can be wrong or stale, especially for narrative-driven housing crash and commercial real estate markets. <br>
Mitigation: Review the generated trade rationale and tune thresholds, market filters, and maximum concurrent positions for the operator's risk limits. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/polymarket-real-estate-trader) <br>
- [simmer-sdk on PyPI](https://pypi.org/project/simmer-sdk/) <br>
- [simmer-sdk on GitHub](https://github.com/SpartanLabsXyz/simmer-sdk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration] <br>
**Output Format:** [Console text with configurable execution parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to paper trading; live trading requires --live and SIMMER_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
