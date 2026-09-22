## Description:

Manage CloudRobo data processing and data evaluation tasks, including algorithm discovery, task creation and monitoring, log retrieval, output preview, pipeline orchestration, batch operations, and failure diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to guide agents through CloudRobo dataset processing and evaluation workflows in a configured workspace. It helps prepare task configurations, run CloudRobo CLI or SDK operations, poll task status, inspect logs, preview outputs, and diagnose failed jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles CloudRobo AK/SK credentials and workspace access.

Mitigation: Use least-privilege credentials, prefer environment variables over plaintext config files, and avoid hardcoding or exposing credentials in logs.

Risk: The skill can guide create, update, restart, and delete operations for CloudRobo tasks.

Mitigation: Require explicit user confirmation before mutating actions and verify workspace IDs, task IDs, and task configuration before execution.

Risk: Insecure debugging settings can weaken transport security or expose request details.

Mitigation: Keep SSL verification enabled in production and avoid traffic logging when requests may contain credentials or sensitive workspace data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-dataset)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Interactive Workflow](references/interactive-workflow.md)
- [Task Config Reference](references/task-config-catalog.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON task configurations, and Python SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudRobo CLI commands, SDK calls, API paths, status summaries, log analysis, confirmation prompts, and troubleshooting recommendations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
