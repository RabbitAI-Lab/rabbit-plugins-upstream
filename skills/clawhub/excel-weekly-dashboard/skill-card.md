## Description: <br>
Designs refreshable Excel dashboards with Power Query, structured tables, validation, and pivot reporting for repeatable weekly KPI workbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, analysts, operators, and developers use this skill to design refreshable Excel KPI workbooks that ingest weekly files, validate rows, and drive pivot dashboards with refresh status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Power Query code could ingest unintended files if pointed at a broad or shared folder. <br>
Mitigation: Review the generated Power Query code and configure it to read from a dedicated folder containing only the intended business files. <br>
Risk: PDF or DOCX table extraction may be unreliable and can lead to incomplete or misleading dashboard data. <br>
Mitigation: Use user-provided CSV or XLSX exports when possible, and clearly mark extraction risk when PDF or DOCX-derived tables are used. <br>
Risk: Dashboard refreshes may silently publish partial or invalid data if query errors or row-count changes are missed. <br>
Mitigation: Include refresh status checks, row-count validation, visible error flags, and a stop-and-investigate checklist before publishing outputs. <br>


## Reference(s): <br>
- [Power Query folder ingest template](artifact/assets/power-query-folder-ingest-template.pq.md) <br>
- [Weekly refresh checklist](artifact/assets/refresh-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown plans with optional Power Query M code and markdown artifact specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only by default; file artifacts are generated only when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
