## Description:

为小学高年级和初中学生生成符合词汇水平与兴趣的英语听力材料，并通过分步练习定位理解障碍。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆小学高年级和初中英语学习者，在监护人或教师适当陪同下按兴趣与词汇水平练习听力、分析词义或句式等理解难点，并在同意后将生词加入词汇库。

### Deployment Geography for Use:

中国大陆；其他地区使用前须调整课程、未成年人同意要求及危机求助渠道。

## Known Risks and Mitigations:

Risk: 学生档案或听力生词在未经学生及监护人同意时被记录或共享。

Mitigation: 仅在获得相应同意后使用或共享档案、存入生词；保留暂停记忆、限制共享及导出入口。

Risk: 在中国大陆以外沿用不适合当地的学制、未成年人同意规则或紧急求助电话。

Mitigation: 在其他地区使用前本地化课程、同意规则和危机转介渠道；未确认所在地时先询问。

Risk: 缺少语音合成或历史记录能力时，将文本练习误称听力训练或捏造长期进步数据。

Mitigation: 明确标注文本替代不是听力训练；没有跨会话数据时只呈现本次练习结果。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [听力话题模板与材料生成指南](references/listening-topic-templates.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外处置](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [中文对话与英文听力材料、词汇注释、理解题及练习反馈]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [语音能力不可用时改用文本替代；无跨会话统计能力时仅报告本次练习情况。]

## Skill Version(s):

2.4.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
