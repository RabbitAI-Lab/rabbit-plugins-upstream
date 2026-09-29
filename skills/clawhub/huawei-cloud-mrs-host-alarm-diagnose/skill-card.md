## Description:

Diagnoses Huawei Cloud MRS cluster alarms from user-provided alarm details, uses LakeWatch or MRS Manager data to identify likely root causes, and returns repair steps and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Operations engineers and support agents use this skill to triage Huawei Cloud MRS alarms when an alarm ID, occurrence time, and cluster context are available. It guides read-only diagnosis and produces root-cause findings, repair recommendations, and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-bearing API clients may send sensitive MRS or LakeWatch credentials while TLS verification is not safely configured.

Mitigation: Enable TLS verification with a trusted CA before use and avoid entering or storing plaintext credentials.

Risk: Manager APIs that can mutate users, alarms, or tasks exceed the stated read-only alarm diagnosis purpose.

Mitigation: Use least-privileged read-only accounts and remove, block, or isolate mutation APIs behind a separate admin-only workflow with explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-mrs-host-alarm-diagnose)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [LakeWatch API Client](references/lakewatch-api-client.md)
- [MRS Manager API Client](references/manager-api-client.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown diagnosis report with tables and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes alarm metadata, likely root cause, analysis basis, repair steps requiring user confirmation, and verification method.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
