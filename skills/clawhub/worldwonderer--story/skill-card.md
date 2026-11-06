## Description:

网络小说工具箱主入口。根据用户需求自动路由到对应 skill，并可启动本地 Dashboard。触发方式：/story、$story、/story dashboard、/网文、「我想写小说」「记住我的写作习惯」「打开工作台」「检查更新」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文网文作者，用于识别写作、规划、分析、调研、审稿、导入和项目管理需求，并转交给相应的写作技能；也可按需启动本地 Dashboard。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed deletion permanently removes files.

Mitigation: Use a dedicated writing folder, keep manuscript backups, and check the target before confirming deletion.

Risk: The local Dashboard can edit project files while its server is running.

Mitigation: Keep it bound to localhost and stop its Node process when finished.

Risk: The optional npm update installer is unpinned.

Mitigation: Check the release and approve updates deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story)
- [Project link listed in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Project releases](https://github.com/zenstory-ai/oh-story-claudecode/releases)
- [Project changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Natural-language guidance and routed skill calls; shell command for the local Dashboard when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some routes require companion skills installed in the same skills root.]

## Skill Version(s):

1.0.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
