## Description: <br>
Excel2Insights helps agents analyze CSV, TSV, XLS, and XLSX datasets through local file loading, statistical summaries, data quality checks, chart generation, and structured insight reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users can use this skill to inspect tabular datasets, identify data quality issues, generate visualizations, and produce readable reports from spreadsheet-style files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided spreadsheets and generated reports or charts may contain sensitive source data. <br>
Mitigation: Use non-sensitive inputs when possible, choose a secure output directory, and delete generated reports, charts, and analysis JSON after use. <br>
Risk: Automated statistics, charts, and recommendations may be misleading if the input dataset is incomplete, inconsistent, or not representative. <br>
Mitigation: Review data quality findings and validate important conclusions before using the generated report for decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/excel2insights) <br>
- [Demo Walkthrough](references/demo-walkthrough.md) <br>
- [Demo Report Preview](references/demo-report-preview.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Command-line output, JSON analysis, Markdown or HTML reports, and PNG chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes derived analysis files, charts, and reports to a local output directory.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
