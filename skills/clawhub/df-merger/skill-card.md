## Description: <br>
Merge pandas DataFrames from multiple construction sources, handling different schemas, keys, and data quality issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, construction data analysts, and project teams use this skill to merge BIM, schedule, cost, quantity takeoff, resource, or sensor DataFrames with schema harmonization, key matching, and merge quality statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fuzzy or inferred DataFrame matches can produce incorrect links between construction records and affect cost or schedule decisions. <br>
Mitigation: Review matched keys, merge quality statistics, and ambiguous fuzzy matches before using outputs for project decisions. <br>
Risk: Construction project files may contain sensitive operational or commercial data. <br>
Mitigation: Provide only the specific files needed for the merge and avoid sharing unrelated project data. <br>
Risk: Exporting merged results can write data to an unintended path or format. <br>
Mitigation: Confirm export paths and formats before writing Excel, CSV, or JSON outputs. <br>


## Reference(s): <br>
- [Df Merger ClawHub Page](https://clawhub.ai/datadrivenconstruction/skills/df-merger) <br>
- [Data Driven Construction Homepage](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables, summary statistics, key findings, and optional Python code snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May offer Excel, CSV, or JSON export options when relevant; requires Python 3 and user-provided project data.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
