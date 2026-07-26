## Description: <br>
Guides agents in creating, reading, editing, validating, and quality-checking Excel .xlsx workbooks and CSV/TSV imports with OfficeCLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iceyliu](https://clawhub.ai/user/iceyliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build, inspect, edit, and validate spreadsheet workbooks, including financial models, dashboards, trackers, charts, pivot tables, and CSV/TSV imports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup instructions include one-line remote installer commands that execute downloaded scripts directly. <br>
Mitigation: Review the OfficeCLI project and installer source first; prefer a pinned release from the releases page and verify its checksum or signature before installation. <br>
Risk: OfficeCLI commands mutate workbook files during execution, so failed multi-step command sequences can leave partial changes. <br>
Mitigation: Run commands incrementally, check each exit code and output, keep backups for important workbooks, and validate the workbook before delivery. <br>


## Reference(s): <br>
- [OfficeCLI releases](https://github.com/iOfficeAI/OfficeCLI/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces procedural guidance and OfficeCLI command examples for spreadsheet creation, editing, inspection, and QA.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
