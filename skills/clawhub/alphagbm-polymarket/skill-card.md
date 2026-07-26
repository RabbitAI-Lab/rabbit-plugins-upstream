## Description: <br>
Integrates prediction market data (Polymarket) with options analysis to surface mispricing signals between event probabilities and options-implied probabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and financial research users use this skill to compare prediction-market probabilities with options-implied probabilities and identify event-driven mispricing signals for further review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may sound like actionable options trading advice based on probability comparisons. <br>
Mitigation: Treat outputs as research prompts only, verify data sources and assumptions independently, and do not rely on them as financial advice. <br>
Risk: Mock, stale, or incomplete market data can produce misleading probability spreads. <br>
Mitigation: Confirm current prediction-market data, options data, and model assumptions before using a surfaced signal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-polymarket) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with probability comparison tables, ranked signal summaries, and suggested options trade ideas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Treat generated trading ideas as research prompts, not financial advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
