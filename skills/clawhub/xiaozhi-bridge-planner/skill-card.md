## Description:

帮助初中毕业生诊断八门学科的初高衔接缺口，并安排暑假与高一开学初期的补基础和入门预习计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中考结束到高一上学期期中的学生，用于找出影响高中起始内容的初中基础缺口，并据此安排每周复习与适量的入门预习。读取学习档案或提交提醒任务前，需要学生分别明确同意。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 学生学习档案可能包含个人信息，计划提醒也会产生额外数据使用。

Mitigation: 默认关闭档案共享与提醒；只有学生分别明确同意后才启用，并在启用前查看相关档案和提醒技能的说明。

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-bridge-planner)
- [初高衔接自查清单](references/bridge-checklists.md)
- [危机转介流程](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [个性化的中文学习计划与学科衔接建议，采用分周文本或 Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按学生回答、剩余周数与可用时间安排；每周保留完整休息日。档案读取和提醒交接仅在单独明确同意后启用。]

## Skill Version(s):

2.12.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
