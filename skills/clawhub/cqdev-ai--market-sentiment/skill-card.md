## Description: <br>
Analyzes CSV market data with a four-dimension sentiment model, producing a 0-100 score, market state, trend views, and decision-support suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to evaluate market sentiment from CSV inputs, review score breakdowns and trends, and pass a market-state parameter into stock-planner workflows. Its outputs are decision support and should be independently reviewed before any trading decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Finance-related scores, market states, positions, and thresholds may be mistaken for investment advice. <br>
Mitigation: Treat outputs as decision support only and require independent suitability review before any trading decision. <br>
Risk: Incorrect, incomplete, stale, or mismapped CSV market data can distort sentiment scores and suggestions. <br>
Mitigation: Verify input data quality, column mappings, and date coverage before relying on analyzer output. <br>
Risk: Automatically feeding the planner parameter into downstream stock-planner workflows can propagate unsuitable guidance. <br>
Mitigation: Review the market-state mapping and planner threshold behavior before automating workflow integration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cqdev-ai/skills/market-sentiment) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Terminal text reports and JSON summaries from CSV input, with command examples for running analyzer modes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can emit JSON to a file with --output; suggested positions, thresholds, and planner parameters are advisory only.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release, package.json, CHANGELOG released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
