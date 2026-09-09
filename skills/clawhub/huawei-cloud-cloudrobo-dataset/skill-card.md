## Description:

Manage Huawei Cloud CloudRobo data processing and evaluation tasks, including task creation, listing, status polling, log retrieval, output preview, algorithm discovery, pipeline orchestration, batch management, and failure diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage CloudRobo proc-tasks and eval-tasks across workspaces, troubleshoot failures with logs, preview generated outputs, and orchestrate processing-to-evaluation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudRobo credentials and workspace access can be exposed or overused during CLI and SDK operations.

Mitigation: Use a virtual environment with least-privilege non-production AK/SK credentials, prefer environment variables over plaintext files where possible, and avoid broad credential-filled environments.

Risk: TLS verification can be disabled for debugging, which weakens transport security.

Mitigation: Keep SSL verification enabled for normal use and treat disabled verification as temporary debugging only.

Risk: The SDK test mode can mishandle credentials or execute injected Python when run with untrusted task inputs.

Mitigation: Review the CloudRobo client package source and version before installation and do not run SDK test mode with untrusted TASK_ID values.

Risk: Create, restart, update, delete, log download, and preview actions can affect tasks or expose task data in the selected workspace.

Mitigation: Confirm the exact workspace, task IDs, and intended operation before allowing the agent to proceed.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Task Config Reference](references/task-config-catalog.md)
- [Interactive Workflow](references/interactive-workflow.md)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-dataset)
- [Publisher Profile](https://clawhub.ai/user/huaweiclouddev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands, JSON configuration examples, and diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CloudRobo CLI or SDK actions that require user confirmation before mutating tasks or accessing logs and preview links.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
