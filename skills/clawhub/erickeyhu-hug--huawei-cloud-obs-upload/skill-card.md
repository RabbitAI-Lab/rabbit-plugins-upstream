## Description: <br>
Upload local files or directories to Huawei Cloud OBS buckets, list OBS buckets with capacity and object count, and schedule periodic uploads via crontab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud OBS uploads, inspect bucket capacity and object counts, and create periodic upload jobs from local directories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload local files or directories to Huawei Cloud OBS buckets, which could expose unintended local data if broad paths are used. <br>
Mitigation: Use a dedicated export directory, review the exact local path, bucket, and prefix before uploading, and avoid broad paths such as a home directory. <br>
Risk: The skill can create persistent scheduled uploads without strong cleanup safeguards. <br>
Mitigation: Inspect any cron or Task Scheduler entry after creation, document how to disable it, and remove scheduled jobs when they are no longer needed. <br>
Risk: OBS operations require cloud credentials and can affect customer storage resources. <br>
Mitigation: Use least-privilege or temporary credentials, avoid putting secrets directly on command lines, and confirm required IAM permissions before running commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-obs-upload) <br>
- [Publisher profile](https://clawhub.ai/user/erickeyhu-hug) <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [IAM Permission Policies](artifact/references/iam-policies.md) <br>
- [Task 1: List Buckets with Capacity and Object Count](artifact/references/task-list-buckets-with-stats.md) <br>
- [Task 2: Upload File or Directory](artifact/references/task-upload-file.md) <br>
- [Task 3: Schedule Periodic Upload](artifact/references/task-scheduled-upload.md) <br>
- [Related APIs](artifact/references/related-apis.md) <br>
- [Verification Method](artifact/references/verification-method.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Huawei Cloud OBS bucket names, regions, prefixes, credential setup instructions, and scheduled upload commands supplied or confirmed by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
