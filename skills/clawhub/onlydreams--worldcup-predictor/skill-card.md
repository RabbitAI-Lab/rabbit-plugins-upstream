## Description: <br>
Use when analyzing or predicting World Cup or international football matches, especially when the user asks for match forecasts, score predictions, betting-market comparison, card or discipline forecasts, group qualification scenarios, knockout-stage scenarios, style matchup, player availability, post-match review, or iterative model corrections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onlydreams](https://clawhub.ai/user/onlydreams) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to structure informational World Cup and international football forecasts, live updates, post-match reviews, and rules or referee controversy analysis. It helps agents combine market baseline, verified match data, team news, context, style matchup, and uncertainty notes instead of relying on a single signal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Football predictions and exact-score forecasts can be incorrect or overinterpreted as guaranteed outcomes. <br>
Mitigation: Present forecasts as uncertain informational analysis, include confidence levels and failure modes, and state missing or unchecked evidence layers. <br>
Risk: Odds and betting-market data could be mistaken for betting or financial advice. <br>
Mitigation: Use market data only as an analytical input and include a disclaimer that the output is not betting advice, financial advice, or an instruction to wager. <br>
Risk: Public sports-data, news, and market pages may be unavailable, stale, localized, or blocked. <br>
Mitigation: Name the source layers actually read, record the evidence cutoff or page state, and mark blocked or missing sources as unavailable rather than inferring from them. <br>


## Reference(s): <br>
- [World Cup Predictor Skill Page](https://clawhub.ai/onlydreams/skills/worldcup-predictor) <br>
- [Prediction Framework](references/prediction-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with compact tables, evidence snapshots, confidence notes, failure modes, and disclaimers when odds or betting markets are used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces informational analysis only; predictions are uncertain and should not be treated as betting advice, financial advice, guaranteed outcomes, or instructions to wager.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
