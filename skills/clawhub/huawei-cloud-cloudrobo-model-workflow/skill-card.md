## Description:

Model development orchestration Skill covering asset query, model training, inference deployment, and real-robot evaluation in any combination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to guide CloudRobo model workflows that combine asset discovery, training, inference deployment, and real-robot evaluation. It is most useful when a request spans two or more stages, such as train plus deploy or deploy plus evaluate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through cloud write operations such as asset creation, training task creation, inference service creation, and dispatch task execution.

Mitigation: Require explicit user confirmation before each cloud write, including selected workspace, intended action, affected resource, and expected cost.

Risk: The workflow can execute real-robot tasks, and server security evidence flags the lack of a strong final safety and cost confirmation gate.

Mitigation: Before dispatch, require final confirmation of selected robot, task text, execution limits, emergency-stop readiness, and inference service status.

Risk: The skill relies on Huawei Cloud AK/SK credentials and may export robot certificate bundles.

Mitigation: Load credentials only from secure environment or configuration sources, never hardcode them, and treat exported robot certificates as secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-model-workflow)
- [Constraints](references/constraints.md)
- [CloudRobo CLI Installation & Configuration Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Pipeline Templates & Quick Reference](references/pipeline-templates.md)
- [model_ext_metadata Construction Guide](references/model-ext-metadata.md)
- [Robot Selection Guide](references/robot-selection-guide.md)
- [Verification Method](references/verification-method.md)
- [Fault Recovery Guide](references/fault-recovery.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged workflow instructions and status/result summaries; it does not directly return model artifacts.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
