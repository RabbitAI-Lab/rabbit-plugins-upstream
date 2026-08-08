## Description:

Lottery CN Research helps agents answer questions about major Chinese welfare and sports lottery games, fetch or import draw history, analyze statistics, generate number sets, and calculate probabilities and expected value.

This skill is ready for commercial/non-commercial use.

## Publisher:

[361066029](https://clawhub.ai/user/361066029)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Chinese lottery rules, normalize draw data, inspect historical statistics, generate preference-based number sets, and calculate lottery probabilities or expected value while preserving gambling-risk caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated lottery numbers or historical statistics could be mistaken for financial or investment advice.

Mitigation: Treat all number generation and analysis as entertainment or probability research, and keep the skill's caveat that strategies do not improve lottery odds.

Risk: Online history fetching contacts public lottery data sites that may change, fail, or return unexpected data.

Mitigation: Prefer trusted local draw-history files when reliability matters, and verify fetched data before using it for analysis.

Risk: Script output paths are controlled by command arguments.

Mitigation: Run the scripts in a trusted workspace and choose output paths intentionally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/361066029/skills/lottery-cn-research)
- [Chinese lottery game rules](references/games.md)
- [Historical draw data sources](references/data_sources.md)
- [Statistical analysis methods](references/analysis_methods.md)
- [OpenCai lottery data API](https://www.opencai.net/api/lottery/)
- [China Welfare Lottery](https://www.cwl.gov.cn/)
- [China Sports Lottery](https://www.lottery.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON files from scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local analysis files or normalized draw-history JSON when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
