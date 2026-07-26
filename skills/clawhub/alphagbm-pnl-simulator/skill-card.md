## Description: <br>
P&L simulation engine for single-leg and multi-leg option positions, including payoff diagrams, time-based P&L, scenario analysis, breakevens, and probability distributions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and trading-tool agents use this skill to simulate option-position P&L, compare risk/reward, evaluate breakevens, and run price, implied-volatility, time-decay, and Monte Carlo scenarios before acting on a trade idea. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Option-position and scenario details may be sent to AlphaGBM's remote API. <br>
Mitigation: Use mock/demo data or avoid entering sensitive portfolio details unless the user trusts AlphaGBM's service and data handling. <br>
Risk: Simulation outputs can be misleading if the user provides stale prices, incorrect implied volatility, or incomplete position details. <br>
Mitigation: Ask the user to confirm ticker, spot price, leg details, expirations, entry prices, quantities, and scenario assumptions before presenting results as decision support. <br>
Risk: P&L and probability estimates are analytical outputs, not investment advice or guaranteed outcomes. <br>
Mitigation: Frame results as scenario analysis and encourage independent review before trading. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-pnl-simulator) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown narrative with structured JSON-style simulation results and scenario summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include payoff arrays, time-series P&L curves, breakevens, maximum profit and loss, probability of profit, expected value, and stress-test scenarios.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
