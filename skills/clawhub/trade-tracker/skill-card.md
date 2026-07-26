## Description: <br>
Trade Tracker analyzes local trade CSV files to summarize profit and loss, attribution by stock and time period, trading costs, holding duration, strategy tags, multi-strategy comparisons, and ASCII profit distribution charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to review trade history from CSV exports, analyze realized performance, compare strategy labels, and produce terminal or JSON reports for local trading retrospectives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade CSVs can contain sensitive financial history. <br>
Mitigation: Run the skill locally on files the user intends to analyze and avoid sharing generated reports unless they have been reviewed for sensitive data. <br>
Risk: The optional JSON output path can create or overwrite a local report file. <br>
Mitigation: Specify --output only for a deliberate destination and review the path before running the command. <br>
Risk: Trade analytics may be mistaken for investment advice. <br>
Mitigation: Use the output for retrospective analysis only and verify conclusions against source records before acting on them. <br>


## Reference(s): <br>
- [Trade Tracker on ClawHub](https://clawhub.ai/cqdev-ai/skills/trade-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Terminal text reports, ASCII charts, and optional JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads a user-selected CSV file locally and can write a JSON report when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact CHANGELOG.md and package.json mention 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
