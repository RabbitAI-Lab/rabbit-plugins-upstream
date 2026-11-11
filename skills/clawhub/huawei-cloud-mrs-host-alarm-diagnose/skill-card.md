## Description:

Diagnoses Huawei Cloud MRS cluster alarms from supplied alarm details and produces root-cause analysis, repair guidance, and verification steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

MRS operators and on-call engineers use the skill to investigate supported cluster alarms from alarm IDs and event details, then review diagnostic findings and proposed remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied configurations disable TLS certificate verification by default, which can expose credentials to interception.

Mitigation: Before entering production credentials, enable verify_ssl:true and configure the cluster's trusted CA in both configurations.

Risk: Read-only diagnosis guidance conflicts with available administrative actions, and some operational procedures need review.

Mitigation: Use a narrowly scoped diagnostic account and an API allowlist that excludes administrative writes and database-password retrieval; have an administrator review cleanup, restart, SSH, permission, and disk-test procedures.

Risk: Live API responses, deployment permissions, and service-side authorization have not been tested.

Mitigation: Verify permissions and authorization behavior in the target deployment before relying on diagnosis results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-mrs-host-alarm-diagnose)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)
- [LakeWatch API Client](artifact/references/lakewatch-api-client.md)
- [MRS Manager API Client](artifact/references/manager-api-client.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown diagnosis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes alarm details, evidence-based root-cause analysis, repair proposals for user review, and verification steps.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
