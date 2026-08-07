## Description: <br>
Query Huawei Cloud OBS statistics, including bucket capacity and object counts, extranet and intranet download traffic with month-over-month comparison, and total request counts with month-over-month comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operations engineers and developers use this skill to inspect Huawei Cloud OBS bucket inventory, capacity, traffic, and request activity. It helps generate the required hcloud, obsutil, and helper-script commands while preserving user-confirmed regions, buckets, and time ranges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential exposure can occur if Huawei Cloud access keys are placed directly on command lines or pasted into chat. <br>
Mitigation: Use a dedicated least-privilege read-only IAM user or temporary credentials, prefer interactive or environment-based local configuration, and do not paste AK/SK values into chat. <br>
Risk: The skill needs local tools that can access Huawei Cloud OBS and CES account data. <br>
Mitigation: Grant only the OBS bucket listing, bucket read, object read, and CES metric read permissions needed for the intended buckets and regions. <br>
Risk: Downloaded hcloud or obsutil binaries could be tampered with before installation. <br>
Mitigation: Download tools from Huawei Cloud sources and verify binaries before use. <br>
Risk: Delete operations against OBS buckets or objects are irreversible and outside the statistics use case. <br>
Mitigation: Refuse delete, empty-bucket, and batch-delete requests and direct users to perform any destructive changes manually through approved Huawei Cloud workflows. <br>


## Reference(s): <br>
- [Task 1: List Buckets with Capacity and Object Counts](references/task-list-buckets-with-stats.md) <br>
- [Task 2: Query Extranet/Intranet Download Traffic](references/task-query-traffic.md) <br>
- [Task 3: Query Total Requests](references/task-query-requests.md) <br>
- [OBS CES Monitoring Metrics Reference](references/obs-metrics.md) <br>
- [Related Huawei Cloud OBS and CES APIs](references/related-apis.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Huawei Cloud OBS Monitoring Metrics](https://support.huaweicloud.com/usermanual-obs/obs_03_0010.html) <br>
- [Huawei Cloud CES ShowMetricData API](https://support.huaweicloud.com/api-ces/ces_03_0059.html) <br>
- [Huawei Cloud obsutil CLI Tool](https://support.huaweicloud.com/utiltg-obs/obs_11_0001.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python helper-script invocations, and plain-text metric reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-confirmed Huawei Cloud region, bucket name, time range, and locally configured hcloud/obsutil credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
