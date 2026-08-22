## Description:

在本地 Windows 电脑上查找、索引、检查并继续处理微信文件。适用于按文件名或内容搜索、自然语言日期与类型筛选、重复文件检测、打开文件位置，以及总结、提取或比较文件等后续任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cryptocxf](https://clawhub.ai/user/cryptocxf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search local WeChat or Weixin saved files on Windows, build a local index for repeated searches, detect exact duplicates, and continue with requested file processing such as summarizing, extracting, comparing, or organizing selected files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently index sensitive WeChat file names, paths, metadata, hashes, and extracted document text under the Windows user profile.

Mitigation: Install only when this local cache is acceptable, prefer explicit search roots, and delete the LOCALAPPDATA\Codex\wechat-file-finder index when cached content should no longer be retained.

Risk: The security verdict is suspicious because indexing has no built-in retention, deletion, encryption, or separate consent step.

Mitigation: Review the local scripts before running commands with ExecutionPolicy Bypass and deploy the skill only in environments where local indexing of WeChat files is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cryptocxf/skills/wechat-file-assistant)
- [Local index workflow](references/index-workflow.md)
- [Trusted metadata index](references/metadata-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with PowerShell commands, local file paths, JSON script output, and extracted document text when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches and indexes local Windows files; content extraction is best effort and may report unsupported or no-text statuses.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
