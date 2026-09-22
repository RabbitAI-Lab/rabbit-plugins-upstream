## Description:

Huawei Cloud CCI (Cloud Container Instance) full lifecycle management using hcloud CLI for namespaces, networks, deployments, statefulsets, pods, EIPPools, logs, metrics, and status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud CCI serverless container resources from the command line, including provisioning, status inspection, logging, scaling, updating, and cleanup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact Huawei Cloud CCI changes, including resource creation, update, deletion, pod execution, Secrets, and RBAC-related operations.

Mitigation: Use narrowly scoped Huawei Cloud credentials, start in a non-production project, and require explicit human review before executing high-impact commands.

Risk: Documented two-step confirmation reduces destructive-operation risk but should not be treated as a complete technical control.

Mitigation: Review delete and collection-delete proposals carefully, verify resource names and namespaces, and run only after explicit user confirmation.

Risk: The network helper uses separate credential environment variables from hcloud CLI, which can lead to permission mismatches or unintended credential scope.

Mitigation: Configure helper credentials with least privilege, verify required IAM permissions before use, and avoid exposing AK, SK, or security-token values in commands or output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cci-instance-management)
- [Credential Configuration for hcloud CLI](references/credential-configuration.md)
- [IAM Permission Policies for CCI Operations](references/iam-policies.md)
- [CCI Common Workflows](references/common-workflows.md)
- [CCI Operation Catalog](references/cci-operation-catalog.md)
- [CCI Parameter Format Rules](references/parameter-format.md)
- [Namespace Lifecycle Management](references/task-namespace-management.md)
- [Network Lifecycle Management](references/task-network-management.md)
- [Deployment Lifecycle Management](references/task-deployment-management.md)
- [StatefulSet Management](references/task-statefulset-management.md)
- [Pod Management](references/task-pod-management.md)
- [EIPPool Management](references/task-eippool-management.md)
- [Logs and Status Queries](references/task-logs-and-status.md)
- [Troubleshooting Guide for CCI hcloud CLI Issues](references/troubleshooting.md)
- [Step-by-Step Verification Process for CCI Skill Functionality](references/verification-method.md)
- [Acceptance Criteria: Correct vs Error Patterns for CCI Operations](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands, JSON-oriented command output guidance, and helper-script usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose cloud resource operations that require user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
