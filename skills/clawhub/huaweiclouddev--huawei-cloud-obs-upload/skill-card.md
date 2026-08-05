## Description: <br>
Upload local files or directories to Huawei Cloud OBS buckets, list buckets with capacity and object count, and schedule periodic uploads via crontab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud OBS object storage from an agent workflow: listing buckets with storage statistics, uploading local files or directories, and setting up recurring uploads when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help create persistent scheduled uploads through crontab or Task Scheduler. <br>
Mitigation: Review the local path, target bucket, schedule, generated script, and scheduled-task entry before enabling it; back up existing scheduled tasks and remove the entry when it is no longer needed. <br>
Risk: Huawei Cloud AK/SK credentials could be exposed or over-scoped if configured carelessly. <br>
Mitigation: Use interactive configuration or protected environment variables, avoid pasting AK/SK into chat, and use least-privilege bucket-scoped permissions without delete access. <br>
Risk: Incorrect bucket, region, or path choices could upload data to the wrong OBS location. <br>
Mitigation: Require the user to provide region, bucket, and local path explicitly, then verify the resolved command and upload result before relying on the workflow. <br>


## Reference(s): <br>
- [Task 1: List Buckets with Capacity and Object Count](references/task-list-buckets-with-stats.md) <br>
- [Task 2: Upload File or Directory](references/task-upload-file.md) <br>
- [Task 3: Scheduled Upload](references/task-scheduled-upload.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [OBS CES Monitoring Metrics Reference](references/obs-metrics.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Huawei Cloud OBS API Reference](https://support.huaweicloud.com/api-obs/obs_04_0001.html) <br>
- [Huawei Cloud obsutil Documentation](https://support.huaweicloud.com/utiltg-obs/obs_11_0001.html) <br>
- [Huawei Cloud CES ShowMetricData API](https://support.huaweicloud.com/api-ces/ces_03_0059.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local shell commands, OBS CLI commands, crontab entries, and verification steps for review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
