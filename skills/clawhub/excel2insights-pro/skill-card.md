## Description: <br>
Analyze and visualize Excel, CSV, and TSV data with automated statistics, quality checks, charts, and structured insight reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to inspect structured spreadsheet data, run statistical and data quality analysis, generate visualizations, and produce Markdown or HTML insight reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads spreadsheet contents, including row previews and categorical values, from files selected by the user. <br>
Mitigation: Use it only with data appropriate for the local agent environment, and avoid highly sensitive files unless output and log storage are controlled. <br>
Risk: Generated charts and reports can contain source data values, summaries, anomalies, and filenames. <br>
Mitigation: Review generated reports and chart files before sharing them outside the intended audience. <br>
Risk: The artifact uses unpinned minimum dependency versions, so future dependency changes could affect behavior. <br>
Mitigation: Pin and review Python dependencies before production deployment. <br>


## Reference(s): <br>
- [Excel2Insights Pro on ClawHub](https://clawhub.ai/cqdev-ai/skills/excel2insights-pro) <br>
- [Publisher profile](https://clawhub.ai/user/cqdev-ai) <br>
- [Demo walkthrough](references/demo-walkthrough.md) <br>
- [Demo report preview](references/demo-report-preview.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown or HTML reports, JSON analysis summaries, PNG chart files, and shell commands for local pipeline execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on user-selected spreadsheet files and writes analysis artifacts to an output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
