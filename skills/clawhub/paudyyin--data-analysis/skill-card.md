## Description: <br>
Analyze data, generate visualizations, query databases, build reports, automate spreadsheets, and turn raw data into clear, actionable insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and business operators use this skill to scope decision-oriented analyses, validate metric definitions, select appropriate charts, and produce stakeholder-ready briefs from SQL data, spreadsheets, dashboards, exports, or ad hoc tables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may request access to broad data sources such as spreadsheets, databases, dashboards, exports, or local files. <br>
Mitigation: Limit access to the specific files, databases, and spreadsheets intended for the analysis. <br>
Risk: Spreadsheet edits, non-read-only SQL, package installation, or publishing reports could change data or expose sensitive analysis. <br>
Mitigation: Require explicit confirmation before any spreadsheet modification, non-read-only SQL execution, package installation, or publication of reports based on sensitive data. <br>
Risk: Ambiguous metrics, weak samples, confounding, or data quality issues can lead to misleading recommendations. <br>
Mitigation: Use metric contracts, document caveats, quantify uncertainty, and downgrade or block conclusions when the data cannot support the claim. <br>


## Reference(s): <br>
- [Data Analysis Skill Page](https://clawhub.ai/paudyyin/skills/data-analysis) <br>
- [Homepage](https://clawic.com/skills/data-analysis) <br>
- [metric-contracts.md](artifact/metric-contracts.md) <br>
- [chart-selection.md](artifact/chart-selection.md) <br>
- [decision-briefs.md](artifact/decision-briefs.md) <br>
- [pitfalls.md](artifact/pitfalls.md) <br>
- [techniques.md](artifact/techniques.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with structured analysis, tables, code snippets, and command suggestions when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chart recommendations, metric contracts, SQL or Python examples, uncertainty notes, caveats, and decision briefs.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, package.json, and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
