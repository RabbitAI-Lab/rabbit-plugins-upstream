## Description:

Manage CloudRobo model training and SimRL tasks, including creating pretrain and finetune jobs, controlling task lifecycle, monitoring status, logs, and resource use, and diagnosing failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Huawei Cloud CloudRobo training and simulation reinforcement learning work from an agent, including task creation, draft workflows, monitoring, and failure diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start, restart, resume, stop, delete, save, or register CloudRobo training resources, which may spend compute or alter jobs.

Mitigation: Use least-privilege CloudRobo credentials, require an explicit workspace ID, and add human confirmation before any command that spends compute or changes tasks.

Risk: The included test script can create drafts, restart them, and delete tasks after only a brief terminal warning.

Mitigation: Run tests only in a controlled workspace with disposable task IDs and review each mutating step before execution.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [API Paths](references/api-paths.md)
- [SDK Quick Start](references/sdk-quickstart.md)
- [Task Config Reference](references/task-config-catalog.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Dataflow Diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CloudRobo task IDs, status reports, logs, signed URLs, and diagnostics through CLI or SDK calls.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
