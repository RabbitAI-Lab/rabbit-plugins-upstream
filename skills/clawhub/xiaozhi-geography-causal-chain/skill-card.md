## Description:

引导初高中学生逐步梳理地理现象的成因、过程与影响，补全原因题中的因果环节。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆初高中学生的地理辅导：通过逐环提问，帮助学生自己解释气候、地球运动、地势、板块运动与人地关系等现象，并完善原因类题目的作答。

### Deployment Geography for Use:

中国大陆（其他地区使用前需本地化课程、求助渠道和未成年人同意规则）

## Known Risks and Mitigations:

Risk: 未成年人学习档案、跨技能共享或提醒可能超出学生预期。

Mitigation: 默认不保存；启用档案、共享和提醒前分别取得同意，写入前逐条确认，并提供查看、更正、删除与暂停入口。

Risk: 中国大陆的课程范围和紧急求助渠道不适用于所有地区。

Mitigation: 仅按默认中国大陆教学场景部署；扩展至其他地区前本地化课程、紧急联系方式与未成年人同意设置。

Risk: 学生对话中可能出现自伤或其他超出学习辅导范围的危机信号。

Mitigation: 遇到危机信号时停止辅导，引导联系信任的成年人，并按确认的地区提供当地求助渠道。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-geography-causal-chain)
- [地理成因链参考指南](references/causal-chain-guide.md)
- [地理错因维度表](shared/geography-error-dimension-table.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [中文对话文本；按步骤提问并反馈因果链]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [默认仅限本次会话；经学生同意后可记录学习进展、交接错题或安排提醒。]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
