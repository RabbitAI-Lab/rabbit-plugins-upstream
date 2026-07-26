## Description: <br>
Generates a standalone HTML dashboard with stat cards, charts, and a filterable table from a local SQLite job application tracker. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenyuan99](https://clawhub.ai/user/chenyuan99) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers and career workflow users use this skill to turn their local application tracker into a browser-openable dashboard for reviewing pipeline status, trends, tags, and application details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated HTML report may contain personal job-search details such as company names, notes, links, and application status. <br>
Mitigation: Keep the report local unless sharing is intentional, and review the file before sending it to anyone else. <br>
Risk: The report can load Chart.js from a third-party CDN when opened, which may create a network request and may fail offline. <br>
Mitigation: Open the report offline for local-only viewing or bundle Chart.js locally when avoiding third-party requests is required. <br>
Risk: The skill depends on the configured SQLite tracker database and will not work with a non-SQLite tracker backend. <br>
Mitigation: Confirm the profile points to the SQLite backend and the expected database path before generating the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenyuan99/skills/html-report) <br>
- [Chart.js CDN dependency](https://cdn.jsdelivr.net/npm/chart.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, code] <br>
**Output Format:** [Standalone HTML file plus a concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads the configured SQLite tracker and writes a single HTML report; charts use Chart.js and degrade when the CDN is unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
