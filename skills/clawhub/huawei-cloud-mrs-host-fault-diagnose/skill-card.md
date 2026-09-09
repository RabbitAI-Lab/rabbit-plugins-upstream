## Description:

Diagnoses Huawei Cloud MRS service, instance, and host faults through progressive root-cause localization using LakeWatch data and a component knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to triage Huawei Cloud MRS cluster incidents, localize service, instance, or host-level root causes, and prepare operator-approved repair suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LakeWatch account with access to MRS logs, resource data, and Manager proxy reads.

Mitigation: Use a minimally scoped account limited to required clusters and read-only permissions.

Risk: Security evidence notes broader operational API access than the read-only diagnosis framing clearly bounds.

Mitigation: Remove or disable unused manager-access POST and generic endpoints where possible before deployment.

Risk: Repair and cleanup recommendations may affect running MRS services if executed without review.

Mitigation: Treat recommendations as manual operator actions requiring backup, explicit approval, and change-control review.

Risk: Improper TLS or credential configuration can expose operational data.

Mitigation: Set TLS verification for the environment and keep LakeWatch credentials encrypted with owner-only file permissions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-host-fault-diagnose)
- [Fault Diagnosis Workflow Design](artifact/references/fault-diagnosis-workflow.md)
- [LakeWatch API Client](artifact/references/lakewatch-api-client.md)
- [CLI Installation Guide - MRS Fault Diagnosis](artifact/references/cli-installation-guide.md)
- [IAM Policies - MRS Fault Diagnosis](artifact/references/iam-policies.md)
- [Verification Method - MRS Fault Diagnosis](artifact/references/verification-method.md)
- [Related Commands - MRS Alarm Diagnosis](artifact/references/related-commands.md)
- [Acceptance Criteria - MRS Fault Diagnosis](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown diagnosis report with command snippets and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fault metadata, diagnosis steps, propagation path, root cause analysis, and repair suggestions requiring user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
