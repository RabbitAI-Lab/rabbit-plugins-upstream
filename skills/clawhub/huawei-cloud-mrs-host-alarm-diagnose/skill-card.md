## Description:

Huawei Cloud MRS Host Alarm Diagnose analyzes MRS cluster alarms from user-provided alarm metadata and produces a Markdown diagnosis report with root cause, repair steps, and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

MRS operators, SREs, and support engineers use this skill to triage Huawei Cloud MRS cluster alarms by alarm ID, collect read-only diagnostic evidence through LakeWatch or MRS Manager APIs, and prepare repair and verification guidance for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles cluster credentials and operational access.

Mitigation: Install only in a controlled MRS operations environment and use least-privilege, read-only accounts where possible.

Risk: TLS verification may be disabled by default.

Mitigation: Turn TLS verification on and configure a trusted CA before operational use.

Risk: Bundled Manager APIs may go beyond read-only diagnosis.

Mitigation: Remove or restrict mutating Manager APIs and keep repair steps as human-reviewed runbook guidance rather than agent-executed actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-mrs-host-alarm-diagnose)
- [CLI Installation Guide - MRS Alarm Diagnosis](artifact/references/cli-installation-guide.md)
- [IAM Policies - MRS Alarm Diagnosis](artifact/references/iam-policies.md)
- [LakeWatch API Client](artifact/references/lakewatch-api-client.md)
- [MRS Manager API Client](artifact/references/manager-api-client.md)
- [Related Commands - MRS Alarm Diagnosis](artifact/references/related-commands.md)
- [Verification Method - MRS Alarm Diagnosis](artifact/references/verification-method.md)
- [Acceptance Criteria - MRS Alarm Diagnosis](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown diagnosis report with command snippets and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes alarm metadata, root cause analysis, repair suggestions, and verification method.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
