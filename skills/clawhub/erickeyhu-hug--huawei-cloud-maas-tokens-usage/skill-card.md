## Description:

Query Huawei Cloud MaaS tokens usage statistics, including total tokens, prompt tokens, completion tokens, request counts, and error counts across supported service types and time ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to query Huawei Cloud MaaS token consumption, request volume, and error rates for preset services, user services, or custom endpoints over a selected time range.

### Deployment Geography for Use:

Global; operational API availability is limited by Huawei Cloud MaaS to the cn-southwest-2 region.

## Known Risks and Mitigations:

Risk: The skill uses Huawei Cloud credentials to call MaaS and IAM APIs.

Mitigation: Use least-privilege credentials limited to the required monitoring, service-read, and project-read permissions; avoid broad account keys.

Risk: The bundled API client disables TLS certificate verification for cloud API calls.

Mitigation: Do not use the skill in sensitive environments unless TLS verification is restored and reviewed.

Risk: The bundled quality SDK sends automatic execution reports to a non-Huawei endpoint by default.

Mitigation: Disable or explicitly approve telemetry before use, especially in environments with sensitive usage data.

## Reference(s):

- [Huawei Cloud MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html)
- [Task: Query Tokens Usage Statistics](references/task-query-tokens-usage.md)
- [Related APIs](references/related-apis.md)
- [IAM Permission Policies](references/iam-policies.md)
- [MaaS Monitoring Metrics Reference](references/maas-metrics.md)
- [Verification Method](references/verification-method.md)
- [Prerequisites Installation Guide](references/cli-installation-guide.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API Calls]

**Output Format:** [Markdown guidance with bash commands; script output as terminal text tables with optional JSON raw API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK credentials from environment variables or a credentials file; the bundled script sends quality telemetry by default unless disabled.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
