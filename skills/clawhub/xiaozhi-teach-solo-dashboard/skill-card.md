## Description:

为独立教师只读汇总课表、学员记录、作业、家长沟通和课时包，生成每日工作台及优先事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向独立教师，从现有工作空间整理当天七项教学与运营待办，依据记录标记需要关注的学员，并选出最重要的三件事；不代替教师修改记录或联系家长。

### Deployment Geography for Use:

中国大陆；其他地区须先本地化求助渠道、学制和未成年人数据保护要求。

## Known Risks and Mitigations:

Risk: 宽泛的日程规划请求可能意外展示敏感的学员和家长记录。

Mitigation: 仅在教师明确要求工作台时读取并展示相关记录；收紧通用日程提示的触发条件。

Risk: 工作台汇总可能暴露未成年人的身份及家庭敏感信息。

Mitigation: 仅展示化名及完成任务所需的低敏信息，并在分享前核对授权。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [日工作台模板](references/dashboard-template.md)
- [七区块输出模板](references/daily-dashboard-block-templates.md)
- [工作台完整示例](references/daily-dashboard-full-sample.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [中文 Markdown 七区块工作台]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [只读汇总；展示风险标记依据、待办事项和今日三件事。]

## Skill Version(s):

2.8.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
