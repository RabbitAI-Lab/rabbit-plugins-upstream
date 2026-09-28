## Description:

通过让学生用自己的话解释、举例和迁移知识，评估理解深度并指出卡住的环节。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文中小学学生及陪同的家长、教师，通过讲解与追问检验单个知识点的理解程度，给出掌握等级、薄弱环节及下一步建议。小学阶段需家长或教师在场。

### Deployment Geography for Use:

中国大陆；在其他地区使用前须本地化语言、课程、同意规则和危机求助信息。

## Known Risks and Mitigations:

Risk: 中国中小学的语言、课程和危机求助信息可能不适用于其他地区。

Mitigation: 仅在预期的中文中小学场景使用；扩大范围前本地化课程、语言、同意规则与危机求助方式。

Risk: 未经同意共享学习记录或发送复测提醒可能暴露未成年人的学习信息。

Mitigation: 平台须落实学生当次明确请求及相应共享、提醒同意门槛；否则只提供会话内反馈。

Risk: 学习挫败表达可能掩盖需要立即帮助的危机信号。

Mitigation: 遇到危机信号时停止学习流程，按所在地区的求助与转介指引处理。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [费曼五跳状态机](references/feynman-5jump-statemachine.md)
- [费曼测试追问话术参考库](references/feynman-dialogue-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [中文对话及 Markdown 评估报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [给出 A–D 掌握等级、理解深度、卡住环节及下一步建议；默认仅在当前会话使用。]

## Skill Version(s):

2.7.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
