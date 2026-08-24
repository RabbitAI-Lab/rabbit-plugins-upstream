## Description:

Query OBS bucket and object listings, then export them to an Excel (.xlsx) report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and storage administrators use this skill to inventory Huawei Cloud OBS buckets and objects for audits, asset management, backup review, and storage cost analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends execution telemetry to a remote quality endpoint that the user-facing documentation does not clearly disclose.

Mitigation: Review telemetry acceptability before installation and set SKILL_QUALITY_DISABLE=1 when telemetry is not acceptable.

Risk: The skill enumerates Huawei OBS buckets and object metadata using configured AK/SK credentials.

Mitigation: Use least-privilege credentials scoped to obs:bucket:ListAllMyBuckets and obs:object:ListObject, and avoid running live tests against production credentials unless intentionally scoped.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-obs-list-excel)
- [IAM Policies](references/iam-policies.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Configuration guidance]

**Output Format:** [Excel (.xlsx) report with text status output and markdown command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bucket summary and object detail sheets; requires Huawei Cloud credentials and OBS read permissions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
