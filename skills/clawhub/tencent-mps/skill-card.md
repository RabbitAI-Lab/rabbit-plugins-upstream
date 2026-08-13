## Description:

Tencent MPS helps agents generate commands for Tencent Cloud Media Processing Service workflows across video, audio, image processing, AI generation, content understanding, COS file operations, task lookup, usage checks, and comparison pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills)

### License/Terms of Use:

MIT

## Use Case:

Developers and media operators use this skill to choose the correct Tencent Cloud MPS script and produce executable Python commands for processing, generating, analyzing, querying, uploading, downloading, and comparing media assets. It is intended for users who already control the relevant Tencent Cloud credentials, COS buckets, source media, and processing permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run scripts with Tencent Cloud and COS credentials and may generate links or logs for processed media.

Mitigation: Use a dedicated least-privilege Tencent Cloud account and bucket, avoid sensitive or unauthorized media, and treat generated links and logs as sensitive.

Risk: Processing tasks can incur Tencent Cloud costs, especially if expensive jobs are repeated or submitted without confirmation.

Mitigation: Prefer dry-run first, require explicit confirmation before processing tasks, avoid manually repeating incomplete jobs, and use Tencent Cloud billing alerts or limits.

Risk: Duplicate-detection evasion, voice cloning, face swap, watermark removal, and similar workflows can be misused.

Mitigation: Use these workflows only for authorized content and do not use them to bypass platform rules, remove protected marks, or process people or media without permission.

Risk: Runtime package upgrades can change SDK behavior after installation.

Mitigation: Review dependency changes before upgrading and test commands in dry-run or a controlled environment before production use.

## Reference(s):

- [Tencent MPS pricing](https://cloud.tencent.com/document/product/862/36180)
- [Tencent MPS request regions](https://cloud.tencent.com/document/product/862/37572)
- [ProcessMedia API](https://cloud.tencent.com/document/api/862/37578)
- [ProcessImage API](https://cloud.tencent.com/document/api/862/112896)
- [CreateAigcImageTask API](https://cloud.tencent.com/document/api/862/114562)
- [CreateAigcVideoTask API](https://cloud.tencent.com/document/api/862/126965)
- [CreateAigcAudioTask API](https://cloud.tencent.com/document/api/862/132830)
- [Tencent Cloud Python SDK](https://github.com/TencentCloud/tencentcloud-sdk-python)
- [Tencent COS Python SDK](https://github.com/tencentyun/cos-python-sdk-v5)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processing tasks should show TaskId values, use dry-run when appropriate, and present generated links as Markdown links.]

## Skill Version(s):

1.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
