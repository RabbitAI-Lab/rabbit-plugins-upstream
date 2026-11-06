## Description:

为初中和高中数学提供五层进阶练习，帮助学生定位当前练习层级并逐步提升。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向初中和高中学生，用于围绕已学会的数学知识点开展分层练习、获得逐级提示，并查看训练进展。需要保存学习档案或跨技能共享时，应先按学生和监护人适用的同意规则选择数据控制。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 学习记录可能被保留或在技能间共享；宿主的存储和同意执行不由本技能包验证。

Mitigation: 启用前检查宿主的数据保留与共享控制；按需要选择不共享，或使用“这次不要记忆”避免本次读取和保存记录。

Risk: 每周提醒和档案写回涉及学生数据及持续联系。

Mitigation: 仅在学生同意后请求提醒或写回；确认适用的学生与监护人同意设置。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [初中数学梯度示例](artifact/references/gradient-levels.md)
- [高中数学梯度示例：高一](artifact/references/math-hs1-gradient-levels.md)
- [高中数学梯度示例：必修后半](artifact/references/math-hs2-gradient-levels.md)
- [高中数学梯度示例：选择性必修](artifact/references/math-hs3-gradient-levels.md)
- [提示阶梯](artifact/shared/hint-ladder.md)
- [危机例外处置](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [中文对话与练习题、Markdown 成长总结，以及可供同意后交接的 JSON 记录或提醒请求]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按知识点和当前层级定制；记录写回与提醒取决于可用平台能力及相应同意。]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter, server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
