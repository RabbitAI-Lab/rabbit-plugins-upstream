## Description: <br>
Extract, clean, and organize legacy construction data from archives. Migrate historical project data, cost records, and schedules into modern formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction teams, data engineers, and analysts use this skill to extract legacy project, cost, schedule, labor, and material records from archives and convert them into structured data for benchmarking, trend analysis, risk review, and estimating calibration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect historical construction data files and legacy database exports, which may contain sensitive business records. <br>
Mitigation: Use trusted, explicitly selected files and run the agent in a constrained workspace when handling sensitive archives. <br>
Risk: Database export handling has a validation weakness noted by the server security evidence. <br>
Mitigation: Validate export paths and sources before opening them, and avoid paths supplied only through prompts or untrusted input. <br>


## Reference(s): <br>
- [Historical Data Manager on ClawHub](https://clawhub.ai/datadrivenconstruction/skills/historical-data-manager) <br>
- [datadrivenconstruction Homepage](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with structured tables, summary statistics, Python examples, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May offer Excel, CSV, or JSON export options; requires python3 and user-selected data files.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
