## Description:

Query Huawei Cloud MaaS token usage, request counts, error counts, and error rates for preset services, user services, or custom endpoints over configurable time ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Huawei Cloud MaaS token consumption, request volume, and error rates for cost, quota, and service monitoring workflows.

### Deployment Geography for Use:

Global; the Huawei Cloud MaaS monitoring API used by the skill is limited to cn-southwest-2.

## Known Risks and Mitigations:

Risk: The release evidence reports unsafe TLS defaults while using Huawei Cloud credentials.

Mitigation: Review before installing; use least-privilege credentials only after TLS verification is fixed or execution is contained in an approved environment.

Risk: The release evidence reports automatic execution-detail reporting to a separate operations endpoint.

Mitigation: Install only if this reporting is acceptable, or disable it with SKILL_QUALITY_DISABLE=1 before running the skill.

Risk: The skill handles cloud access keys and secret keys.

Mitigation: Do not provide credentials in chat; use environment variables or a protected credentials file, and avoid production credentials unless the security concerns are resolved.

## Reference(s):

- [Task: Query MaaS Tokens Usage Statistics](references/task-query-tokens-usage.md)
- [Related APIs](references/related-apis.md)
- [MaaS Monitoring Metrics Reference](references/maas-metrics.md)
- [IAM Permission Policy](references/iam-policies.md)
- [Verification Steps and Methods](references/verification-method.md)
- [Prerequisites Installation Guide](references/cli-installation-guide.md)
- [Acceptance Criteria: Correct/Error Pattern Comparison](references/acceptance-criteria.md)
- [Troubleshooting](references/troubleshooting.md)
- [Huawei Cloud MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and tabular usage statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON when the user requests raw API responses.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
