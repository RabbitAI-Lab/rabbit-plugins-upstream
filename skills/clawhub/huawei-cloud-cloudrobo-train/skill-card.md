## Description:

Manage CloudRobo model training and simulation reinforcement learning tasks by creating pretrain and finetune jobs, managing task lifecycles, monitoring resource usage, logs, signed URLs, and events, and diagnosing failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to operate Huawei Cloud CloudRobo training and SimRL workflows through agent-guided CLI, SDK, and API commands. It helps create, inspect, update, stop, restart, resume, delete, monitor, and diagnose long-running training tasks in a CloudRobo workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudRobo create, restart, save-draft, checkpoint registration, update, stop, resume, clone, and delete operations can make real cloud changes and consume compute resources.

Mitigation: Require explicit final user confirmation before each mutating operation and use narrowly scoped CloudRobo credentials in a dedicated test workspace when evaluating the skill.

Risk: The included test script exercises live CloudRobo CLI paths and can restart or delete tasks when valid credentials are present.

Mitigation: Do not run the test script against production workspaces; review commands first and run only with disposable tasks and least-privilege access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-train)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [API Paths](references/api-paths.md)
- [SDK Quick Start](references/sdk-quickstart.md)
- [Task Config Reference](references/task-config-catalog.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and Python SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide long-running cloud task execution and monitoring when valid CloudRobo credentials and workspace access are available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
