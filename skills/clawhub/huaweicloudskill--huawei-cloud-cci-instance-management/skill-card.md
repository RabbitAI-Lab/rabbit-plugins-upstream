## Description:

Guides agents through Huawei Cloud CCI container lifecycle operations, including namespaces, networks, workloads, public IP pools, status, logs, and metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to create, inspect, update, and remove Huawei Cloud CCI resources, and to diagnose workload status and logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive operations can remove workloads or cascade across a namespace if confirmation instructions are not followed.

Mitigation: Review the exact namespace and affected resources, and require explicit user confirmation before deletion.

Risk: Operations may target the wrong account or project, or run with credentials that have broader access than needed.

Mitigation: Verify that the CLI and helper target the intended account and project, and use narrowly scoped credentials.

Risk: Public network access and EIPPool creation can expose workloads or incur recurring charges.

Mitigation: Review network rules and explain EIPPool charges before asking for confirmation; keep Secret values private.

## Reference(s):

- [Skill release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cci-instance-management)
- [Publisher profile](https://clawhub.ai/user/huaweicloudskill)
- [Huawei Cloud CCI documentation](https://support.huaweicloud.com/cci/index.html)
- [CCI Network creation API](https://support.huaweicloud.com/api-cci/createNetworkingCciIoV1beta1NamespacedNetwork.html)
- [CCI operation catalog](references/cci-operation-catalog.md)
- [Common workflows](references/common-workflows.md)
- [Credential configuration](references/credential-configuration.md)
- [IAM policies](references/iam-policies.md)
- [Diagnosis playbooks](references/diagnosis-playbooks.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use user-provided regions and resource details; commands require appropriately scoped cloud credentials.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
