## Description:

Orchestrates Huawei CloudRobo model development workflows across asset query, model training, inference deployment, and real-robot evaluation, including full and partial pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to run Huawei CloudRobo model workflows that select assets, prepare datasets, create training jobs, deploy inference services, and evaluate results on real robots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create or modify CloudRobo assets, training tasks, inference services, robot registrations, and dispatch tasks.

Mitigation: Use least-privilege CloudRobo credentials and require explicit user confirmation before mutating CLI commands.

Risk: Real-robot evaluation can initiate physical execution through dispatch tasks.

Mitigation: Confirm robot identity, online status, workspace safety, emergency stop readiness, and intended task before any dispatch create-task command.

Risk: Robot certificate exports create credential bundles that may grant robot access.

Mitigation: Store exported credential ZIPs outside project folders with restrictive permissions, transfer them securely, and delete or rotate them after onboarding.

Risk: Cloud access keys can be exposed if pasted into chat, logs, source files, or committed project artifacts.

Mitigation: Keep AK/SK values in environment variables, IAM roles, or a secrets manager, and avoid plaintext CLI configuration commands.

## Reference(s):

- [CloudRobo CLI Installation & Configuration Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Pipeline Templates & Quick Reference](references/pipeline-templates.md)
- [model_ext_metadata Construction Guide](references/model-ext-metadata.md)
- [OpenPI Model data.rename_map Construction](references/openpi-rename-map.md)
- [Robot Selection Guide](references/robot-selection-guide.md)
- [Fault Recovery Guide](references/fault-recovery.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Constraints](references/constraints.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline CLI commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces stage-by-stage CloudRobo workflow instructions, command arguments, polling checks, and result summaries.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
