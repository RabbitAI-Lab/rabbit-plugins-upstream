## Description: <br>
Scenario-driven hedge recommendations for an existing stock position, classifying the holding situation and returning Long Put, Collar, Tier-down, or position-rule outputs with resolved option-chain details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to research hedge approaches for an existing single-stock position based on ticker, cost basis, and holding purpose. Outputs should be treated as educational research, with pricing independently verified before any trading decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce concrete options hedge ideas from broad investing prompts. <br>
Mitigation: Treat outputs as educational research, require user review, and do not use them as personalized financial advice or trade execution guidance. <br>
Risk: Option prices, strikes, and premiums may be stale or unsuitable for the user's actual account context. <br>
Mitigation: Verify option-chain pricing, costs, liquidity, suitability, and position sizing independently before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-hedge-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/clementgu) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance, API Calls] <br>
**Output Format:** [Markdown guidance and structured JSON-style hedge recommendation fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes scenario labels, rationale, resolved option strikes and prices, risk-control position rules, and bilingual English/Chinese fields where provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
