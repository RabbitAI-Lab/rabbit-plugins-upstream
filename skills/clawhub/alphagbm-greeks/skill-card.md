## Description: <br>
Greeks dashboard for any option contract or multi-leg position, covering first-order Greeks, second-order Greeks, individual and position-level Greeks, and scenario heatmaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to calculate and interpret option sensitivities for single contracts or multi-leg positions. It supports position risk review, theta decay analysis, gamma exposure checks, vega risk analysis, and scenario heatmaps across underlying price and implied volatility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends option parameters and related market-analysis inputs to AlphaGBM using the user's API key. <br>
Mitigation: Confirm the user is comfortable sharing those inputs with AlphaGBM and avoid submitting confidential trading data unless approved. <br>
Risk: Options Greeks and scenario heatmaps are analytical estimates and may be unsuitable as standalone trading advice. <br>
Mitigation: Treat outputs as decision-support analysis and verify assumptions, market data, and risk decisions independently. <br>


## Reference(s): <br>
- [AlphaGBM Website](https://alphagbm.com) <br>
- [AlphaGBM API Base URL](https://alphagbm.zeabur.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-greeks) <br>
- [Publisher Profile](https://clawhub.ai/user/clementgu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown explanations with JSON-style Greeks, net position values, scenario heatmap data, and concise analytical insights.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include per-leg Greeks, aggregated net Greeks, Greeks per unit of capital, risk concentration, and scenario grids.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
