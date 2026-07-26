## Description: <br>
Recommends multi-leg options strategies from a ticker and market view, including spreads, condors, straddles, and income plays with P&L profile, breakevens, Greeks, and probability of profit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, traders, and agent builders use this skill to compare options strategy templates for a ticker and market view before planning a multi-leg position. It helps select ranked strategies with expected payoff, breakeven, Greeks, and probability-of-profit details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live API use may send ticker symbols, market views, risk preferences, and strategy parameters to AlphaGBM. <br>
Mitigation: Avoid highly sensitive portfolio or trading-intent details unless external-service use is acceptable; use sanitized inputs or demo data where appropriate. <br>
Risk: Options strategy recommendations can be incorrect, incomplete, or unsuitable for a user's financial situation. <br>
Mitigation: Treat output as analysis rather than trading authority and require human review before any trade decision. <br>
Risk: Some options strategies described by the skill can carry high or unlimited loss exposure. <br>
Mitigation: Review max loss, assignment risk, capital requirements, and broker suitability constraints before using any recommended strategy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-options-strategy) <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown guidance with structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Strategy recommendations may include ranked multi-leg trades, payoff profile, breakevens, Greeks, risk/reward ratio, and rationale.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
