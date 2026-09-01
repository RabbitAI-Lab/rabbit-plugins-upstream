## Description:

Queries Huawei Cloud MaaS token, request, and error statistics through the ShowStatistics API for preset service, my service, or custom endpoint time ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to check Huawei Cloud MaaS token consumption, request volume, and error rate for a chosen service type and date range.

### Deployment Geography for Use:

Global; the supported MaaS statistics API region is cn-southwest-2.

## Known Risks and Mitigations:

Risk: Huawei Cloud access keys can be exposed if pasted into chat, stored in shell history, passed as CLI arguments, or logged.

Mitigation: Use temporary, least-privilege AK/SK when possible; provide credentials only through environment variables or a protected credentials file; never paste secrets into conversation or commands that expose values.

Risk: Broad account permissions increase impact if credentials are misused during a MaaS usage query.

Mitigation: Limit IAM permissions to the documented read-only MaaS statistics workflow and review the skill before installing with credentials that can access wider account resources.

Risk: Using a region outside the documented cn-southwest-2 workflow can fail or return unsupported MaaS statistics behavior.

Mitigation: Keep the MaaS statistics query region fixed to cn-southwest-2 unless authoritative release evidence documents another supported region.

## Reference(s):

- [Huawei Cloud MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html)
- [Task Query Tokens Usage](references/task-query-tokens-usage.md)
- [Security Design](references/security-design.md)
- [IAM Permission Policies](references/iam-policies.md)
- [MaaS Monitoring Metrics](references/maas-metrics.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting](references/troubleshooting.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [MaaS REST Usage Statistics Script](scripts/maas_rest_usage_stats.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash commands and tabular usage statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke a bundled Python script that returns MaaS token, request, error-rate, and period data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
