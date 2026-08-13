## Description: <br>
Query Huawei Cloud MaaS tokens usage statistics, including total tokens, prompt tokens, completion tokens, total requests, and total errors for preset service, my service, or custom endpoints over configured time ranges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to query Huawei Cloud MaaS token consumption, request counts, and error rates for usage monitoring and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary reports that the bundled script disables TLS certificate verification while handling Huawei Cloud credentials. <br>
Mitigation: Review before installing, use least-privilege Huawei Cloud credentials, avoid sharing AK/SK values in chat, and do not run the bundled script unless TLS verification is restored or replaced with a secure CA-bundle option. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-maas-tokens-usage) <br>
- [MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html) <br>
- [Task Query Tokens Usage](references/task-query-tokens-usage.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [IAM Permission Policy](references/iam-policies.md) <br>
- [MaaS Monitoring Metrics Reference](references/maas-metrics.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting and Practical Experience](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and optional tabular command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke a bundled Python script that calls Huawei Cloud APIs and can print raw JSON responses when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
