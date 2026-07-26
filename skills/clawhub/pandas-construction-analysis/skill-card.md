## Description: <br>
Comprehensive Pandas toolkit for construction data analysis. Filter, group, aggregate BIM elements, calculate quantities, merge datasets, and generate reports from structured construction data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, construction analysts, BIM coordinators, and project teams use this skill to analyze CSV, Excel, JSON, or user-provided construction datasets with Pandas. It supports filtering, grouping, aggregation, quantity take-off summaries, cost calculations, joins, pivots, and report exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CSV, Excel, or JSON exports may overwrite existing local project files if paths are reused. <br>
Mitigation: Review destination file paths before running export commands and write reports to a deliberate project output directory. <br>
Risk: Analysis results can be misleading if input construction data is incomplete, malformed, or uses unexpected column names or units. <br>
Mitigation: Validate inputs, confirm required columns and units, and report parsing or data-quality issues before relying on summaries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/pandas-construction-analysis) <br>
- [Data Driven Construction homepage](https://datadrivenconstruction.io) <br>
- [Pandas documentation](https://pandas.pydata.org/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables, summary findings, and Python/Pandas code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local CSV, Excel, or JSON report exports when relevant.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata; artifact/claw.json declares 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
