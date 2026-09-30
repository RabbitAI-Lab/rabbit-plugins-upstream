## Description:

为中文 K12 学习请求选择合适的学习技能、避免重复协作，并在用户同意后汇总五维全景月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文 K12 学生及陪同使用的家长或教师：按学习问题路由至错题、理解、笔记、计划或专注技能，并在用户请求且授权后生成学习系统月报。

### Deployment Geography for Use:

中国大陆（其他地区使用前须本地化危机转介和隐私规则）

## Known Risks and Mitigations:

Risk: 跨技能共享、长期学习档案或家长与教师可见内容可能暴露学生信息。

Mitigation: 先确认相应授权，仅使用当前任务所需的最小摘要，并尊重暂停共享或记忆的请求。

Risk: 在中国大陆以外沿用默认危机求助渠道或隐私规则可能不适用。

Mitigation: 部署前按当地情况调整危机转介渠道和隐私规则；不确定所在地时先确认地区。

Risk: 缺少跨会话数据时，月报中的历史统计可能不完整。

Mitigation: 只汇总已授权、可取得的会话内容，并清楚说明报告范围，不编造历史数字。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [一周多技能联动示例](references/one-week-linkage-record.md)
- [技能交接协议](schemas/handover-protocol.schema.json)
- [隐私授权与提醒规则](shared/vocab.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文文本或 Markdown 月报]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按需路由、去重与授权范围内的摘要；不自行讲题或发送提醒。]

## Skill Version(s):

2.8.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
