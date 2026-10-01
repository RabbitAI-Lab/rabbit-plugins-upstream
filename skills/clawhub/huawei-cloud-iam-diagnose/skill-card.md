## Description:

Analyzes Huawei Cloud IAM permission chains to estimate whether a user can perform an action on a resource, with a confidence grade and supporting trace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to investigate Huawei Cloud IAM access questions by tracing user, group, and agency permissions and reviewing a non-authoritative likelihood verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic runs can reveal sensitive IAM account structure.

Mitigation: Use a least-privilege read-only IAM identity and run diagnostic scripts manually rather than relying on broad auto-execution.

Risk: Setup scripts can install local dependencies or an optional CLI with unclear telemetry details.

Mitigation: Review installations before running them and consider setting SKILL_QUALITY_REPORT=0.

Risk: Access keys or secret keys could be exposed if entered in chat.

Mitigation: Configure credentials locally; do not paste keys into agent conversations.

Risk: Static analysis and incomplete IAM reads can produce a misleading access verdict.

Mitigation: Treat results as reference-only and verify consequential decisions through the IAM console, an actual API call, or audit logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-iam-diagnose)
- [Huawei Cloud CLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Permission verification method](artifact/references/verification-method.md)
- [Least-privilege IAM guidance](artifact/references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or JSON permission-chain trace and reference verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Likely has/likely has not/uncertain verdict, confidence grade, and chain evidence; not an authoritative access decision.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
