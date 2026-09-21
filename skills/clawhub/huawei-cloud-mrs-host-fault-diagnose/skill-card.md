## Description:

Diagnoses Huawei Cloud MRS service, instance, and host faults through progressive root cause localization using LakeWatch or MRS Manager API clients and the bundled diagnosis knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose Huawei Cloud MRS cluster faults when a cluster ID plus a service name or node name is available. It produces a root-cause-oriented diagnosis report with investigation steps, propagation analysis, and repair suggestions that require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated administrative cluster actions may be available even though the skill presents itself as read-only troubleshooting.

Mitigation: Before installation, reduce the API catalog to diagnosis-only endpoints and remove or strongly gate POST, PUT, DELETE, and wildcard proxy paths.

Risk: Credentials and cluster data are sensitive, and weak transport verification can expose them.

Mitigation: Use a least-privileged read-only account, enable TLS verification with a trusted CA, and avoid configuring admin credentials unless write-capable paths have been removed or strongly gated.

## Reference(s):

- [Acceptance Criteria - MRS Fault Diagnosis](references/acceptance-criteria.md)
- [CLI Installation Guide - MRS Fault Diagnosis](references/cli-installation-guide.md)
- [Fault Diagnosis Workflow Design](references/fault-diagnosis-workflow.md)
- [IAM Policies - MRS Fault Diagnosis](references/iam-policies.md)
- [LakeWatch API Client](references/lakewatch-api-client.md)
- [MRS Manager API Client](references/manager-api-client.md)
- [Related Commands - MRS Fault Diagnosis](references/related-commands.md)
- [Verification Method - MRS Fault Diagnosis](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown diagnosis report with command examples, tables, and repair suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repair actions are suggestions only and require user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
