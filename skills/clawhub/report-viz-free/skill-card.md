## Description: <br>
Report Viz Free helps agents generate charts, structured visual summaries, and exportable reports from financial report data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and business users use this skill to create financial report visualizations, data summaries, and export-ready chart or report outputs from provided financial data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad read/exec capability and possible external financial-data or API-key use without tight runtime boundaries. <br>
Mitigation: Review before installing, restrict filesystem access to intended financial report inputs and outputs, and grant only the minimum API permissions needed. <br>
Risk: Financial report outputs can be wrong or misleading if source data, API responses, or generated visualizations are not verified. <br>
Mitigation: Validate input data and generated charts or reports against authoritative records before business or investment use. <br>
Risk: Commands, file exports, or external API calls may affect files or expose sensitive financial data. <br>
Mitigation: Require explicit user confirmation before command execution, file export, or external API calls, especially with private or proprietary data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/report-viz-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, chart and report descriptions, and optional shell-command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe generated SVG charts and exported report files; requires explicit user confirmation before file export, command execution, or external API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
