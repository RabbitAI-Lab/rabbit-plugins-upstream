## Description:

将学生一周的学习记录整理为有证据、有结论和下一步行动的周报，并引导学生自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 学生，在一周学习结束时梳理知识进展、薄弱点和下周优先行动；小学学段须由家长或老师陪同使用。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: 学生学习记录可能通过长期记忆、跨技能共享、家长报告或提醒被不当披露。

Mitigation: 部署前核查学生同意和查看、更正、删除、暂停及共享控制；家庭分享、摘要写回和提醒均须符合学生授权。

Risk: 中国大陆课程、未成年人同意规则及紧急求助渠道在其他地区可能不适用。

Mitigation: 用于其他地区前，核查并本地化课程假设、监护要求及当地有效求助渠道。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [周报文案参考模板](references/review-report-template.md)
- [交接协议模式](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文文本或 Markdown 周报及对话式复盘]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [以学习证据为依据；仅在学生授权后生成家庭分享版、写回成长摘要或安排提醒。]

## Skill Version(s):

2.7.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
