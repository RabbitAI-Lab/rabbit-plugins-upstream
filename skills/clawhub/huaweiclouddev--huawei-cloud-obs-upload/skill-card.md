## Description:

Upload local files or directories to Huawei Cloud OBS buckets, list OBS buckets with capacity and object count, and schedule periodic uploads via crontab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to upload files or directories to Huawei Cloud OBS, inspect bucket capacity and object counts, and configure recurring uploads with OS-level scheduling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI installation commands and OBS upload operations may affect the local system or cloud resources if run without review.

Mitigation: Review every proposed command before execution and prefer verified, version-pinned Huawei CLI and obsutil installers.

Risk: Huawei Cloud AK/SK credentials could be exposed if pasted into chat or passed directly on a command line.

Mitigation: Do not share AK/SK values in conversation; configure credentials through secure local CLI flows or environment variables and use least-privilege OBS/CES permissions.

Risk: Generated upload scripts and scheduled tasks can repeatedly move local data to OBS.

Mitigation: Inspect generated scripts, target buckets, prefixes, schedules, and logs before enabling cron or Task Scheduler entries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-obs-upload)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Task 1: List Buckets with Capacity and Object Count](references/task-list-buckets-with-stats.md)
- [Task 2: Upload Local File or Directory to Target Bucket](references/task-upload-file.md)
- [Task 3: Schedule Periodic Upload of Local Directory to Target Bucket](references/task-scheduled-upload.md)
- [IAM Permission Policies](references/iam-policies.md)
- [OBS CES Monitoring Metrics Reference](references/obs-metrics.md)
- [Related APIs](references/related-apis.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)
- [OBS IAM Authorization](https://support.huaweicloud.com/perms-cfg-obs/obs_40_0001.html)
- [OBS Monitoring Metrics Description](https://support.huaweicloud.com/usermanual-obs/obs_03_0010.html)
- [OBS API Reference](https://support.huaweicloud.com/api-obs/obs_04_0001.html)
- [obsutil CLI Tool](https://support.huaweicloud.com/utiltg-obs/obs_11_0001.html)
- [CES ShowMetricData API](https://support.huaweicloud.com/api-ces/ces_03_0059.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate upload scripts and crontab or Task Scheduler entries for user review before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
