## Description:

钉钉 AI 听记（妙记）读取封装。当用户要查询/读取 AI 听记的列表、摘要、语音转写原文（逐字稿）、关键词、待办或音频地址时使用。基于 dws CLI（钉钉官方 Workspace CLI）。写文档走 dingtalk-doc，建待办走 dingtalk-todo，日程走 dingtalk-calendar。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Employees, external collaborators, and developers use this skill to read DingTalk AI meeting minutes through the official dws CLI, including lists, summaries, transcripts, keywords, todos, and audio links. It also supports local archival, incremental sync, and controlled mirroring of minute outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can bulk-copy sensitive DingTalk meeting transcripts, summaries, todos, metadata, audio URLs, and optional audio files into local archives or external folders.

Mitigation: Choose private local destinations, avoid shared or cloud-synced folders unless intended, restrict file permissions, and review mirrored outputs before sharing.

Risk: Sync and mirror commands can move more meeting content than expected.

Mitigation: Use dry-run or list-only modes first, select narrow date ranges or explicit archive targets, and confirm the destination before writing files.

Risk: The setup flow references a remote shell installer for the dws CLI.

Mitigation: Verify the DingTalk Workspace CLI installer source before execution and install only when the user intends to use local DingTalk minute archive or export workflows.

## Reference(s):

- [AI 听记读取命令参考](artifact/references/01-commands.md)
- [安装、授权与常见坑](artifact/references/02-setup.md)
- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/dingtalk-minutes)
- [Publisher project homepage](https://github.com/cat-xierluo/legal-skills)
- [DingTalk Workspace CLI](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text guidance with shell commands, JSON-oriented CLI output handling, and generated local files for archives or mirrors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local dws CLI access and optional Python standard-library scripts; archived transcripts, summaries, todos, metadata, audio URLs, and optional audio files should be treated as sensitive business data.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and changelog report 0.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
