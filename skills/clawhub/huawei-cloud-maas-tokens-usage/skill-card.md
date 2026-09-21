## Description:

Query Huawei Cloud MaaS token usage statistics, including total tokens, prompt tokens, completion tokens, request counts, and error counts for preset service, my service, or custom endpoints over supported time ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to check Huawei Cloud MaaS token consumption, request volume, and error counts from the MaaS ShowStatistics API. It supports routine usage monitoring for preset service, my service, and custom endpoint workloads.

### Deployment Geography for Use:

Global, with runtime API access limited to Huawei Cloud MaaS Southwest-Guiyang-1 (cn-southwest-2).

## Known Risks and Mitigations:

Risk: The skill reads Huawei Cloud credentials from environment variables or a user-specified credentials file to sign MaaS API requests.

Mitigation: Use temporary or least-privilege read-only IAM credentials, avoid pasting secrets into chat, and protect any credentials file with restrictive file permissions.

Risk: Dependency installation may use a selected pip package index or mirror.

Mitigation: Choose the package index deliberately and install only the documented Python dependencies needed for Huawei SDK signing and HTTPS requests.

Risk: Incorrect MaaS region, service type, or time range can produce failed or misleading usage queries.

Mitigation: Use the documented cn-southwest-2 region, supported service_type values 1, 2, or 4, and verify returned usage against the Huawei Cloud console when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-maas-tokens-usage)
- [Publisher Profile](https://clawhub.ai/user/huaweicloudskill)
- [Huawei Cloud MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html)
- [Task: Query MaaS Tokens Usage Statistics](references/task-query-tokens-usage.md)
- [Security Design: Credential Lifecycle and Tool Separation](references/security-design.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [MaaS Monitoring Metrics Reference](references/maas-metrics.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and tabular usage statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke a bundled Python script that reads Huawei credentials from environment variables or a user-specified credentials file and prints aggregate MaaS usage metrics.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
