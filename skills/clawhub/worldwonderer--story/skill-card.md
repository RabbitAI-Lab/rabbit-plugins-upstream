## Description:

网络小说工具箱主入口。根据用户需求自动路由到对应 skill，并可启动本地 Dashboard。触发方式：/story、$story、/story dashboard、/网文、「我想写小说」「记住我的写作习惯」「打开工作台」「检查更新」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向网文作者，按创作、拆文、扫榜、审稿、资料查询等需求选择合适的写作助手，并在需要时打开本地工作台查看和编辑项目文件。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports that network mode exposes unauthenticated workspace read, overwrite, and deletion APIs; its review is incomplete.

Mitigation: Keep the Dashboard on its default local-only binding. Before enabling network mode, review the package and confirm that exposing workspace access is acceptable; review each update before approving it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story)
- [Release notes](https://github.com/zenstory-ai/oh-story-claudecode/releases)
- [Changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown text with routing guidance, command examples, or a local dashboard URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to companion skills; may provide a local dashboard URL when requested.]

## Skill Version(s):

1.0.43 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
