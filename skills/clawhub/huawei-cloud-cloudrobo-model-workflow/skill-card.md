## Description:

Orchestrates CloudRobo asset lookup, model training, inference deployment, and real-robot evaluation in full or partial model-development workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to coordinate CloudRobo model-development workflows, from asset and dataset selection through training and inference deployment, with optional real-robot evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery guidance may restart a robot task after manual cancellation without a renewed safety check.

Mitigation: Require an operator readiness check before each dispatch and fresh authorization after cancellation; keep cancelled tasks stopped by default.

Risk: Workflow writes and robot/cloud access can expose user data, credentials, certificates, or incur resource costs.

Mitigation: Confirm dataset paths, cloud destinations, and resource costs before writes; protect cloud keys and exported robot certificates, and verify the external CLI source and version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-model-workflow)
- [CLI installation guide](artifact/references/cli-installation-guide.md)
- [IAM policies](artifact/references/iam-policies.md)
- [Robot selection guide](artifact/references/robot-selection-guide.md)
- [Fault recovery guide](artifact/references/fault-recovery.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, JSON configuration, Operational guidance, Workflow status and evaluation summaries]

**Output Format:** [Markdown with CLI examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow steps and result summaries depend on the user-provided task, assets, dataset, workspace, and service or robot identifiers.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
