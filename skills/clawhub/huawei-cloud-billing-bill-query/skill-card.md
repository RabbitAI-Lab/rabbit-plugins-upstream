## Description:

Queries Huawei Cloud BSS bills, resource fee records, and monthly cost breakdowns for the current account within a single billing cycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Huawei Cloud account billing data for monthly expense checks, cost review, resource fee inspection, and budget analysis within one billing cycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing workflows can expose sensitive cost and resource information through automatic execution telemetry.

Mitigation: Review telemetry behavior before installation; for privacy-sensitive use, set SKILL_QUALITY_DISABLE=1 or route SKILL_QUALITY_ENDPOINT to an organization-controlled endpoint.

Risk: Huawei Cloud credentials with broad billing permissions may expose more account information than the skill requires.

Mitigation: Use a least-privilege credential with bss:bill:view only, or review the broader BSS ReadOnlyAccess policy before use.

Risk: The skill only supports one billing cycle and may not answer multi-month, balance, export, invoice, recharge, or refund requests.

Mitigation: Confirm the requested task is a read-only bill, resource fee, or monthly breakdown query for a single YYYY-MM billing cycle before running it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-billing-bill-query)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud BSS global endpoint](https://bss.myhuaweicloud.com)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Text or JSON billing reports, plus Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results are scoped to one billing cycle; JSON output is available with --format json.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
