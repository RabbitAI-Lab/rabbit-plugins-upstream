## Description:

将学生一周的学习记录整理成有证据、有结论、有下周行动重点的复盘报告，并引导学生自我反思。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生使用本技能梳理一周的学习进展、薄弱点和下周优先事项；经学生授权，可生成家庭分享版和学习系统交接摘要。

### Deployment Geography for Use:

中国大陆；其他地区使用前需本地化同意规则和危机求助资源。

## Known Risks and Mitigations:

Risk: 月报摘要交给学习系统协调器的路径未纳入随附的交接模式，可能造成未经充分约束的学生数据传递。

Mitigation: 安装前在交接模式中明确接收方、传递内容和学生当次同意要求，并核对实际交接流程。

Risk: 周报和家庭分享涉及学生学习记录及可能敏感的情绪信息。

Mitigation: 确认学生身份和授权后才读取、分享或写回记录；尊重学生对家庭分享及情绪内容的拒绝。

Risk: 非中国大陆部署可能沿用不适用的同意规则或危机求助渠道。

Mitigation: 部署前按当地要求调整授权规则和危机资源，并由人员审查相关指引。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [周报文案参考模板](references/review-report-template.md)
- [交接协议模式](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)
- [危机转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown 周报或三问版，以及经同意的结构化交接记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [家庭分享版须经学生授权；数据不足时标明结论的不确定性。]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
