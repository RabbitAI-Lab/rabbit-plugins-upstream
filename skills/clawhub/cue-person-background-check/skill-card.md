## Description:

用 Cue 穿透人物的全生命周期工商与司法轨迹——剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向 IPO 与重大交易团队、合作方准入人员及高管候选人核查人员，整理目标人物公开可查的工商任职、对外投资、司法风险与行政处罚记录，形成供专业人士复核的背调底稿。

### Deployment Geography for Use:

中国

## Known Risks and Mitigations:

Risk: 将 Cue API Key 粘贴到聊天中可能暴露凭据。

Mitigation: 通过受保护的本地配置或环境变量私下配置密钥；已经在聊天中分享的密钥应予以更换。

Risk: 研究查询会发送给 Cue，生成的报告链接可能对获得链接的人可见。

Mitigation: 发送查询前确认可向 Cue 提交相关信息；分享报告前检查链接的可见范围，并仅向获授权的接收者分享。

Risk: 公开记录整理出的背调材料可能被误当作已核实的最终结论，或用于未经同意的雇佣等决策。

Mitigation: 逐条复核来源并由专业人士确认；用于雇佣决策等场景前，取得被核查人同意并遵守适用法律。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-person-background-check)
- [Cue service health check](https://cuecue.cn/api/health)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [结构化 Markdown 背调底稿，含来源链接及可用时的 Cue 原始报告链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按身份核验、工商任职、对外投资、司法风险、行政处罚及关联企业图谱组织；需提供目标人物姓名，可附已知关联企业。]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
