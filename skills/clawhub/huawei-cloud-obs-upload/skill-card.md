## Description:

Upload local files or directories to Huawei Cloud OBS buckets, list bucket capacity and object counts, and schedule periodic uploads with operating-system schedulers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud OBS upload workflows: listing buckets with storage statistics, uploading local files or directories, and creating scheduled uploads after confirming the local path, target bucket, prefix, credentials, and directory-structure behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide installation of Huawei Cloud CLI tools and obsutil.

Mitigation: Verify Huawei CLI and obsutil downloads before running installers.

Risk: Scheduled uploads can continue sending the selected local folder until the scheduled task is removed.

Mitigation: Review the exact local folder, target bucket, prefix, and schedule before enabling a scheduled upload, and remove the scheduled task when it is no longer needed.

Risk: Cloud credentials or overbroad IAM permissions could expose OBS resources.

Mitigation: Use least-privilege IAM credentials without delete permissions and never paste AK/SK values into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-obs-upload)
- [CLI installation guide](artifact/references/cli-installation-guide.md)
- [IAM permission policies](artifact/references/iam-policies.md)
- [OBS metrics reference](artifact/references/obs-metrics.md)
- [Upload file or directory workflow](artifact/references/task-upload-file.md)
- [Scheduled upload workflow](artifact/references/task-scheduled-upload.md)
- [Bucket listing with statistics workflow](artifact/references/task-list-buckets-with-stats.md)
- [Verification method](artifact/references/verification-method.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and optional scheduler or upload script snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce OS-specific crontab or Task Scheduler commands; does not request cloud access keys in chat.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
