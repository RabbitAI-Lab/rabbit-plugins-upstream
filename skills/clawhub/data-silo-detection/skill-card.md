## Description: <br>
Detect and map data silos in construction organizations, including disconnected data sources and integration opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction data teams, consultants, and developers use this skill to identify isolated systems, duplicate data, missing domain connections, and prioritized integration actions across construction organizations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reports may expose sensitive internal construction systems, owners, users, and integration gaps. <br>
Mitigation: Provide only project files or source metadata intended for analysis and handle generated reports as sensitive internal material. <br>
Risk: Generated integration recommendations may be incomplete or misaligned if source inventories are stale or partial. <br>
Mitigation: Validate input data before analysis and review recommendations with system owners before acting on them. <br>
Risk: Filesystem access can process local project files selected by the user. <br>
Mitigation: Limit file inputs to the specific CSV, Excel, JSON, or project data files required for the assessment. <br>


## Reference(s): <br>
- [Data Driven Construction](https://datadrivenconstruction.io) <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/data-silo-detection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown reports, structured tables, Python code examples, and optional CSV, Excel, or JSON export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include internal system names, owners, users, connectivity scores, detected silos, duplicate data issues, and integration roadmaps.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence, created 2026-02-15) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
