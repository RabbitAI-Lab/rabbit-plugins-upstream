## Description:

Upload local files or directories to Huawei Cloud OBS (Object Storage Service) buckets, list OBS buckets with capacity and object count, and schedule periodic uploads via crontab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to upload local files or directories to Huawei Cloud OBS buckets, inspect bucket capacity and object counts, and configure periodic uploads with Huawei Cloud CLI and obsutil.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local data to Huawei Cloud OBS, including recursive directory uploads.

Mitigation: Review local paths and directory contents before upload, and use least-privilege IAM permissions scoped to required buckets and upload actions.

Risk: Credential mishandling could expose Huawei Cloud AK/SK secrets.

Mitigation: Do not paste AK/SK values into the conversation; configure credentials through supported local CLI or environment-variable methods.

Risk: Scheduled uploads can repeatedly transfer files without further user review.

Mitigation: Inspect cron or Task Scheduler entries before enabling them and confirm the schedule, source directory, destination bucket, and log location.

## Reference(s):

- [Task 1: List Buckets with Capacity and Object Count](references/task-list-buckets-with-stats.md)
- [Task 2: Upload Local File or Directory to Target Bucket](references/task-upload-file.md)
- [Task 3: Schedule Periodic Upload of Local Directory to Target Bucket](references/task-scheduled-upload.md)
- [Related APIs - Huawei Cloud OBS Object Storage Management](references/related-apis.md)
- [IAM Permission Policies - Huawei Cloud OBS Object Storage Management](references/iam-policies.md)
- [OBS CES Monitoring Metrics Reference - Huawei Cloud OBS Object Storage Management](references/obs-metrics.md)
- [Verification Method - Huawei Cloud OBS Object Storage Management](references/verification-method.md)
- [Acceptance Criteria: huawei-cloud-obs-upload](references/acceptance-criteria.md)
- [CLI Installation Guide - Huawei Cloud OBS Object Storage Management](references/cli-installation-guide.md)
- [Troubleshooting - Huawei Cloud OBS Object Storage Management](references/troubleshooting.md)
- [Huawei Cloud OBS monitoring metrics documentation](https://support.huaweicloud.com/usermanual-obs/obs_03_0010.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided target paths, bucket names, regions, schedules, and preconfigured Huawei Cloud credentials; does not handle delete operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
