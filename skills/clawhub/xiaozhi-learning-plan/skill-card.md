## Description:

帮助学生把学习目标拆成可执行的 30 天计划（小学高段按周安排），并在学生开启后跟进执行偏差。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生在家长或老师陪同下，用它按近期目标和可用时间制定周计划或 30 天学习计划；学生分别同意后，也可生成家长看板或将任务交给提醒服务。

### Deployment Geography for Use:

中国大陆为默认使用场景；其他地区需调整课程与求助信息。

## Known Risks and Mitigations:

Risk: The instructions conflict about access to student records and what parents may see.

Mitigation: Until the publisher reconciles the profile field lists, plan only from information in the current conversation, keep consent checks in place, exclude emotional judgments from parent dashboards, and review parent-facing output before sharing.

Risk: Storage, consent enforcement, and reminder delivery depend on separate skills that were not included in this review.

Mitigation: Review those connected skills before relying on persistence, consent enforcement, or reminder delivery.

## Reference(s):

- [学习计划模板](references/plan-templates.md)
- [学段与时间参数](shared/grade-bands.md)
- [授权与提醒约定](shared/vocab.md)
- [危机处理例外](shared/crisis-exception.md)
- [交接协议](shared/handover-protocol.schema.json)
- [ClawHub 技能发布页](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [中文学习计划、周安排及可选的家庭看板（Markdown）]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [家庭看板、档案读取和提醒入队各需单独明确同意。]

## Skill Version(s):

2.12.6 (source: server-resolved release evidence; artifact frontmatter agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
