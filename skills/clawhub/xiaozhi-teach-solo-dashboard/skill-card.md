## Description:

为独立教师只读汇总课表、学员跟进、家长沟通和课时包记录，生成按优先级排列的每日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师在获准查阅学员记录的中文 K12 辅导场景中，用它汇总当天课程和待办、识别有数据依据的跟进事项，并确定今日三件要事。

### Deployment Geography for Use:

中国大陆；其他地区须先本地化危机求助信息

## Known Risks and Mitigations:

Risk: 按请求导出工作空间记录可能泄露大量学员资料。

Mitigation: 仅供获准查阅记录的教师使用；只导出所需学员或记录范围，保留化名，不将导出内容粘贴到无关工具或聊天。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [日工作台模板](artifact/references/dashboard-template.md)
- [七区块模板](artifact/references/daily-dashboard-block-templates.md)
- [日工作台示例](artifact/references/daily-dashboard-full-sample.md)
- [独立教师工作空间数据结构](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [七区块中文 Markdown 工作台或按需提供文本记录导出]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [只读汇总；风险提示附记录依据，学员以化名呈现。]

## Skill Version(s):

2.11.2 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
