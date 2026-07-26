## Description: <br>
Assess construction data quality using completeness, accuracy, consistency, timeliness, and validity metrics with automated validation patterns, thresholds, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction data practitioners and project teams use this skill to assess user-provided construction datasets for missing values, invalid ranges, duplicate identifiers, stale records, and pattern mismatches. It helps produce structured findings, summary statistics, and optional report guidance for CSV, Excel, JSON, or direct input data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Construction datasets and generated quality reports may contain sensitive project data. <br>
Mitigation: Review the files provided to the skill and write Excel or CSV reports only to trusted local folders. <br>
Risk: Rule-based checks can miss project-specific data quality requirements or flag values that are valid for a particular project. <br>
Mitigation: Review thresholds, required columns, regex patterns, and category lists against the project's standards before relying on results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/datadrivenconstruction/skills/data-quality-check) <br>
- [DataDrivenConstruction Homepage](https://datadrivenconstruction.io) <br>
- [Great Expectations](https://greatexpectations.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables, summary statistics, key findings, Python code examples, and optional CSV, Excel, or JSON export guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided construction data and validation parameters; generated reports may be written to a local folder chosen by the user.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
