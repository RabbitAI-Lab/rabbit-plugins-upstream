## Description:

Manage CloudRobo model-training and SimRL tasks, including setup, lifecycle operations, monitoring, and failure diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and machine-learning engineers use this skill to configure and manage CloudRobo model-training and simulation reinforcement-learning tasks, monitor their progress and resources, and investigate failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting approval rules and live verification steps can start compute jobs without clear consent.

Mitigation: Resolve approval rules and require explicit authorization before live training tests. Select the workspace explicitly, use restricted credentials and a disposable test workspace, and keep bundled tests away from production resources.

Risk: The external SDK implementation was not included in the reviewed release artifacts.

Mitigation: Review the external SDK separately before relying on its behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-train)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Task Configuration Catalog](artifact/references/task-config-catalog.md)
- [SDK Quick Start](artifact/references/sdk-quickstart.md)
- [API Paths](artifact/references/api-paths.md)
- [Dataflow Diagram](artifact/references/dataflow-diagram.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance, Diagnostic summaries]

**Output Format:** [Markdown with shell commands, JSON configuration examples, and diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific commands and configurations; some operations can start cloud training jobs.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
