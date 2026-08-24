## Description:

Upload local files or directories to Huawei Cloud OBS (Object Storage Service) buckets, list OBS buckets with capacity and object count, and schedule periodic uploads via crontab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud OBS upload workflows, including bucket inventory with storage statistics, file or directory uploads, and scheduled incremental uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent scheduled uploads from local directories.

Mitigation: Review the exact source directory, bucket, prefix, and schedule; verify the cron or Task Scheduler entry before enabling it.

Risk: Cloud access keys and secret keys could be exposed through chat, shell history, or insecure configuration commands.

Mitigation: Do not paste AK/SK into chat; prefer interactive or environment-based credential configuration and keep credential handling out of logs.

Risk: Overbroad OBS permissions increase the impact of mistakes during upload and monitoring workflows.

Mitigation: Use least-privileged IAM permissions with no delete permissions and scope access to the intended buckets where possible.

Risk: Remote installer scripts or downloaded CLI tools may introduce supply-chain risk.

Mitigation: Inspect installer scripts before running them and verify tool source, version, and integrity before installation.

## Reference(s):

- [Task 1: List Buckets with Capacity and Object Count](references/task-list-buckets-with-stats.md)
- [Task 2: Upload Local File or Directory to Target Bucket](references/task-upload-file.md)
- [Task 3: Schedule Periodic Upload of Local Directory to Target Bucket](references/task-scheduled-upload.md)
- [IAM Permission Policies](references/iam-policies.md)
- [OBS CES Monitoring Metrics Reference](references/obs-metrics.md)
- [Related APIs](references/related-apis.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [obsutil Documentation](https://support.huaweicloud.com/utiltg-obs/obs_11_0001.html)
- [OBS API Reference](https://support.huaweicloud.com/api-obs/obs_04_0001.html)
- [CES API Reference](https://support.huaweicloud.com/api-ces/ces_03_0001.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Huawei Cloud CLI, obsutil, crontab, or Task Scheduler commands for user review and execution.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
