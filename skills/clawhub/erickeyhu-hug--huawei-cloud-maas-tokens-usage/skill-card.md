## Description: <br>
Query Huawei Cloud MaaS token usage statistics, including total tokens, prompt tokens, completion tokens, total requests, and total errors through the MaaS ShowStatistics API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to query Huawei Cloud MaaS usage metrics, monitor token consumption, request counts, and error rates, and inspect usage over selected time ranges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud credentials may be exposed or mishandled during setup. <br>
Mitigation: Use a least-privilege Huawei Cloud key, provide credentials only through environment variables or a local credentials file, and avoid any example or command that prints access key values. <br>
Risk: HTTPS certificate verification is disabled in the included request path. <br>
Mitigation: Replace the disabled certificate verification with normal certificate validation or an explicit trusted CA bundle before using the script. <br>
Risk: The skill queries usage and monitoring data from Huawei Cloud services. <br>
Mitigation: Grant only the documented minimum IAM permissions needed for MaaS metrics and project lookup. <br>


## Reference(s): <br>
- [Huawei Cloud MaaS ShowStatistics API](https://support.huaweicloud.com/api-maas/ShowStatistics.html) <br>
- [Task: Query MaaS Tokens Usage Statistics](references/task-query-tokens-usage.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [IAM Permission Policy](references/iam-policies.md) <br>
- [MaaS Monitoring Metrics Reference](references/maas-metrics.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting and Practical Experience](references/troubleshooting.md) <br>
- [Prerequisites Installation Guide](references/cli-installation-guide.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and tabular metric summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Huawei Cloud API usage summaries, error rates, and optional raw JSON responses when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
