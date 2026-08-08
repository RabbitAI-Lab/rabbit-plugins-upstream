## Description: <br>
Query Huawei Cloud OBS statistics, including bucket capacity and object counts, extranet or intranet traffic, total requests, and month-over-month comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and cloud administrators use this skill to inspect Huawei Cloud OBS bucket inventory, storage usage, traffic, and request trends. It helps produce CLI commands, configuration guidance, and terminal reports for read-oriented OBS and CES monitoring tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Huawei Cloud access keys or secrets may be exposed if users paste credentials into chat or command examples. <br>
Mitigation: Use interactive or secure credential configuration, prefer environment variables where appropriate, and do not ask for, echo, or print AK/SK values. <br>
Risk: Overbroad IAM permissions could allow actions beyond the skill's read-oriented statistics scope. <br>
Mitigation: Use least-privilege, read-only OBS and CES permissions, preferably scoped to the required buckets. <br>
Risk: The skill can query upload traffic and error metrics in addition to download traffic and request counts. <br>
Mitigation: Install and use it only when those OBS bucket metadata and monitoring queries are intended. <br>
Risk: Incorrect CES metric names, timestamp units, or time-range interpretation can produce misleading usage reports. <br>
Mitigation: Confirm region, bucket, and time range with the user, use CES namespace SYS.OBS, millisecond timestamps, and the documented traffic and request metrics. <br>
Risk: OBS delete or empty-bucket requests are destructive and outside this skill's intended behavior. <br>
Mitigation: Refuse delete operations and direct the user to manage destructive actions manually through Huawei Cloud tools. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-obs-stats) <br>
- [Task: List Buckets With Stats](references/task-list-buckets-with-stats.md) <br>
- [Task: Query Traffic](references/task-query-traffic.md) <br>
- [Task: Query Requests](references/task-query-requests.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [OBS CES Monitoring Metrics](references/obs-metrics.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Huawei Cloud OBS Monitoring Metrics](https://support.huaweicloud.com/usermanual-obs/obs_03_0010.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional Python helper-script output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-confirmed region, bucket, time range, and configured Huawei Cloud credentials; helper scripts produce terminal reports with month-over-month comparisons.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
