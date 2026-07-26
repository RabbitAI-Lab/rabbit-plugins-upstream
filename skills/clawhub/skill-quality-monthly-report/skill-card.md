## Description: <br>
基于质量月度数据生成专业的质量月报；当用户需要生成质量月报、汇总月度测试成果、进行多月数据对比分析时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, test, and engineering teams use this skill to turn monthly quality data from Excel, JSON, or manual input into a structured monthly report with metrics, PDCA summaries, trends, and an HTML deliverable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require Python and npm dependency installation before processing reports. <br>
Mitigation: Require explicit user approval before installing pandas, openpyxl, or mermaid-cli, and run dependency installation in an approved environment. <br>
Risk: Quality-report inputs, conversation history, and exported JSON or HTML files can contain sensitive project data. <br>
Mitigation: Avoid providing sensitive project data unless the workspace, conversation retention, and generated files are acceptable for the user's environment. <br>
Risk: Incomplete or inconsistent input data can lead to misleading monthly metrics or trend analysis. <br>
Mitigation: Use the skill's data validation and outline-confirmation step to identify gaps before producing the final report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-quality-monthly-report) <br>
- [Server-resolved GitHub source](https://github.com/duding-engicool/skill-quality-monthly-report) <br>
- [Data format specification](references/data_format.md) <br>
- [Analysis framework](references/analysis_framework.md) <br>
- [Report template](assets/report_template.md) <br>
- [Outline template](reports/outline_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, HTML, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown outline and report content, JSON metric data, and a single HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks the user to confirm the report outline before generating the final HTML report.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata); artifact frontmatter lists 1.1.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
