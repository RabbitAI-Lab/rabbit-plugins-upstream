## Description: <br>
Analyzes manufacturing floor quality data for inspection, process defect, finished-goods inspection, and nonconformance records, including data cleaning, defect statistics, and chart-based reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing quality, process, and operations teams use this skill to inspect uploaded or pasted quality records, identify key defect fields, clean inconsistent tabular data, summarize defect distributions, and prioritize the most frequent issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded manufacturing quality files may contain confidential production or inspection data that is parsed into derived JSON and report artifacts. <br>
Mitigation: Use approved local storage and output locations, and review generated reports before sharing them outside the intended audience. <br>
Risk: Generated HTML reports may load an external Google Fonts resource. <br>
Mitigation: For confidential or air-gapped environments, remove or block the Google Fonts link before opening or distributing generated reports. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-manufacturing-quality-data-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-manufacturing-quality-data-analysis) <br>
- [Field mapping reference](references/field_mapping.md) <br>
- [Cleaning rules reference](references/cleaning_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, JSON intermediate results, shell command examples, and HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce timestamped HTML reports with data overview, statistical tables, visual charts, quality conclusions, and remediation priority guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
