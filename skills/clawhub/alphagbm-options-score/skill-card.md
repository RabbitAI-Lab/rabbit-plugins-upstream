## Description: <br>
Score and rank options contracts for any ticker using AlphaGBM's multi-factor scoring model, returning scored option chains with top contracts highlighted. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to evaluate, compare, and rank options contracts by strategy, score breakdown, liquidity, volatility, Greeks balance, and risk-return profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Options scores and top-pick rankings may be mistaken for financial advice or trade recommendations. <br>
Mitigation: Present outputs as informational analysis only, and require users to independently verify assumptions, risks, liquidity, suitability, and possible losses before trading. <br>
Risk: High-risk trading outputs may omit enough uncertainty context for a user to understand downside exposure. <br>
Mitigation: Show score breakdowns, ATR safety details, risk-return labels, and cautionary context alongside any ranked contract output. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API Base URL](https://alphagbm.zeabur.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-options-score) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/clementgu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown tables and narrative analysis with API request examples and scored JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scores range from 0 to 100 and should include score breakdowns, ATR safety information for sell strategies, and risk-return labels.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
