## Description: <br>
Fund Flow is a local CSV analysis skill for ranking A-share stock or sector fund flows, comparing main-force and retail net inflows, detecting trends, aggregating sectors, comparing against an index, scoring fund strength, and producing ASCII trend charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent workflows use this skill to inspect intentionally selected CSV fund-flow datasets, summarize main-force versus retail flow, rank securities or sectors, and export optional JSON analysis results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked by broad stock-analysis wording and could analyze an unintended CSV file or write JSON to an unintended path. <br>
Mitigation: Run it only with CSV files and output paths the user explicitly selects, and review the command arguments before execution. <br>
Risk: Fund-flow rankings and trend scores can be mistaken for investment advice or treated as conclusive market signals. <br>
Mitigation: Present results as dataset-derived analysis only and require human review before any financial decision. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Terminal text reports and optional JSON files generated from local CSV input.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include rankings, trend summaries, sector aggregation, timeframe summaries, index comparison, fund-strength scores, and ASCII trend charts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
