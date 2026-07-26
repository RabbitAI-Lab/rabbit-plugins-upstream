## Description: <br>
Record Keeper helps agents create, archive, index, search, and status-track structured work records across 13 fixed record categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckystarry](https://clawhub.ai/user/luckystarry) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and team agents use this skill to turn meetings, requirements, plans, reports, tasks, administrative notes, and related work updates into consistently named Markdown records with local status tracking and searchable indexing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Record contents and search queries may be sent to SiliconFlow when the embedding workflow uses SILICONFLOW_API_KEY. <br>
Mitigation: Use this skill with confidential, customer, HR, incident, or regulated records only after the SiliconFlow data flow is approved by the organization. <br>
Risk: The indexing workflow can persist record-derived embeddings and metadata in a local SQLite database. <br>
Mitigation: Protect the workspace vectors directory, review retention expectations, and disable or replace indexing when local-only archiving is required. <br>
Risk: Mandatory indexing after record creation or modification can reduce user control over outbound data flow. <br>
Mitigation: Confirm indexing is desired before deployment, and withhold SILICONFLOW_API_KEY or modify the workflow in environments that should not call third-party embedding services. <br>


## Reference(s): <br>
- [Record Keeper skill page](https://clawhub.ai/luckystarry/skills/record-keeper) <br>
- [Vector index guide](references/vector-index.md) <br>
- [Status transition guide](references/status-transitions.md) <br>
- [Meeting record template](references/meeting.md) <br>
- [Requirement template](references/requirement.md) <br>
- [Plan template](references/plan.md) <br>
- [Report template](references/report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown records with shell commands for indexing and status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates records under records/YYYY-MM/ and may maintain a local SQLite vector index under vectors/embeddings.db.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
