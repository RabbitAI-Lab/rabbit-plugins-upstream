## Description:

Queries the current Huawei Cloud account balance through the BSS Python SDK and returns currency, total debt, and per-account balance details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and cloud account administrators use this skill to check the current Huawei Cloud BSS account balance, debt amount, and sub-account balances before cost review, daily inspection, or pay-per-use resource creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends billing-result execution telemetry to an external operations service by default.

Mitigation: Set SKILL_QUALITY_DISABLE=1 unless telemetry to the skillsopr endpoint is intentionally approved.

Risk: The skill requires Huawei Cloud AK/SK credentials for the account whose balance is queried.

Mitigation: Use environment variables only, avoid hardcoded credentials, and grant least-privilege access such as bss:balance:view.

Risk: Broad BSS read permissions can expose more billing information than balance checks require.

Mitigation: Prefer the fine-grained bss:balance:view policy over broader BSS ReadOnlyAccess when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-billing-account-balance)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud BSS Endpoint](https://bss.myhuaweicloud.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text report or JSON object, with setup and execution guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports currency, debt_amount, and account balance entries; supports text or JSON output.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
