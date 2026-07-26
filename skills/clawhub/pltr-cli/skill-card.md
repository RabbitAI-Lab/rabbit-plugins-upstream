## Description: <br>
Helps agents use the pltr CLI to query datasets, run SQL, manage builds, ontologies, projects, users, streams, AI agents, and ML models in Palantir Foundry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjor](https://clawhub.ai/user/anjor) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, data engineers, administrators, and analysts use this skill to get concise guidance and command examples for operating Palantir Foundry through pltr-cli, including data access, SQL analysis, orchestration, permissions, and model-related workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Guidance can include commands that modify or delete Foundry resources, permissions, users, groups, schedules, streams, imports, or transactions. <br>
Mitigation: Use least-privilege accounts and non-production profiles where possible, and require explicit approval before delete, --force, --yes, --confirm, --execute, permission, administration, stream reset, or production schedule operations. <br>
Risk: Incorrect RIDs or profile selection can target the wrong Foundry resource or environment. <br>
Mitigation: Review every RID, branch, folder, schedule, and profile before running generated commands; prefer preview, dry-run, or read-only checks when available. <br>
Risk: Tokens and OAuth secrets are required for some authentication flows and could be exposed through unsafe handling. <br>
Mitigation: Protect Foundry tokens and OAuth secrets, avoid placing secrets in shared logs or command history, and use dedicated non-production or limited-scope credentials when practical. <br>
Risk: Language-model commands may send prompts or data to external model providers. <br>
Mitigation: Require explicit approval and data-handling review before external model calls, especially when prompts may contain sensitive or regulated data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anjor/skills/pltr-cli) <br>
- [Quick Start & Authentication](reference/quick-start.md) <br>
- [Dataset Commands](reference/dataset-commands.md) <br>
- [SQL Commands](reference/sql-commands.md) <br>
- [Orchestration Commands](reference/orchestration-commands.md) <br>
- [Ontology Commands](reference/ontology-commands.md) <br>
- [Admin Commands](reference/admin-commands.md) <br>
- [Filesystem Commands](reference/filesystem-commands.md) <br>
- [Connectivity Commands](reference/connectivity-commands.md) <br>
- [Language Models Commands](reference/language-models-commands.md) <br>
- [Streams Commands](reference/streams-commands.md) <br>
- [Functions Commands](reference/functions-commands.md) <br>
- [AIP Agents Commands](reference/aip-agents-commands.md) <br>
- [Models Commands](reference/models-commands.md) <br>
- [Data Analysis Workflow](workflows/data-analysis.md) <br>
- [Data Pipeline Workflow](workflows/data-pipeline.md) <br>
- [Permission Management Workflow](workflows/permission-management.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include pltr-cli commands, Foundry RID patterns, profile selection, output-format options, and workflow steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
