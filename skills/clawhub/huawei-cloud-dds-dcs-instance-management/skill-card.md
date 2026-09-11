## Description:

Unified management skill for Huawei Cloud DDS and DCS instances, covering instance queries, deployment and security analysis, and lifecycle operations through hcloud CLI commands and Huawei Cloud SDK examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inspect, analyze, create, modify, restart, back up, and delete Huawei Cloud DDS and DCS resources. It is intended for database and cache administration workflows where operators need command guidance, SDK examples, and safety checks before mutating cloud resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quality reporting can reuse cloud credentials to send an IAM token and execution details to a configurable endpoint.

Mitigation: Disable or tightly control quality reporting unless the endpoint is trusted, and use credentials scoped to the minimum permissions required.

Risk: DDS and DCS lifecycle operations can create billable resources, delete data, or interrupt service.

Mitigation: Require explicit user confirmation before mutating operations, double-confirm destructive actions, and recommend backups before deletes or flushes.

Risk: Broad Huawei Cloud IAM permissions increase blast radius for database and cache administration.

Mitigation: Prefer the supplied read-only or least-privilege IAM policy examples and avoid wildcard administrative policies unless they are explicitly required.

Risk: Unverified CLI binaries or floating SDK dependencies can change execution behavior.

Mitigation: Verify the hcloud binary source before use and pin Huawei Cloud SDK package versions in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-dds-dcs-instance-management)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies for DDS and DCS](artifact/references/iam-policies.md)
- [Detailed Command Reference](artifact/references/related-commands.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [hcloud CLI download](https://cn-south-1-cloud-res-model-sdk.obs.cn-south-1.myhuaweicloud.com/hcloud/hcloud.tar.gz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python SDK examples, configuration snippets, and operational recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-confirmation guidance for mutating operations and references to least-privilege IAM policy examples.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
