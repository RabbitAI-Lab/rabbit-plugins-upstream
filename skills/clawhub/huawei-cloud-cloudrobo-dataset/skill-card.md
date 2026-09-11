## Description:

Manage CloudRobo data processing and data evaluation tasks, including algorithm discovery, task lifecycle operations, status polling, log retrieval, output previews, processing-to-evaluation pipelines, batch task management, and failure diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Huawei Cloud CloudRobo processing and evaluation workflows from an agent, including creating tasks, monitoring progress, retrieving logs, previewing outputs, and diagnosing failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential or workspace access misuse could expose or alter CloudRobo resources.

Mitigation: Use dedicated least-privileged AK/SK credentials, protect local CloudRobo config files, and review the active workspace before running commands.

Risk: Disabling TLS verification can weaken transport security.

Mitigation: Keep TLS verification enabled; use CLOUDROBO_VERIFY_SSL=false only for tightly controlled debugging.

Risk: Logs, previews, and temporary OBS URLs may reveal sensitive dataset or job information.

Mitigation: Treat retrieved logs, previews, downloads, and temporary URLs as sensitive and share them only with authorized users.

Risk: Create, update, delete, restart, and batch operations can affect live processing or evaluation tasks.

Mitigation: Require explicit user confirmation and review task IDs, workspace IDs, and JSON task configuration before executing mutating commands.

Risk: Unreviewed client package installation may introduce supply-chain exposure.

Mitigation: Install in a trusted isolated environment and pin and review the hw-cloudrobo-client package version before use.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Interactive Workflow](references/interactive-workflow.md)
- [Task Config Reference](references/task-config-catalog.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudRobo CLI commands, task JSON, polling steps, log analysis, and operational checklists for user review.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
