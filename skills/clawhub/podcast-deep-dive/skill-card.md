## Description:

将小宇宙或喜马拉雅的播客单集整理为带时间戳、区分说话人的文字稿，并提供深度摘要分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

适用于希望将播客单集转成可检索文字并快速理解内容的听众与研究者；可按说话人查看带时间戳的转写稿，并阅读主旨、结构和对谈要点等摘要。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 技能说明中存在让用户在聊天中粘贴 Cue API Key 的设置指引，可能暴露凭证。

Mitigation: 仅在本机配置 CUE_API_KEY，不要在聊天中发送密钥；如已分享，请撤销并更换。

Risk: 播客链接会发送至 Cue 远程服务，解析内容会交由模型处理；提交内容也会消耗服务积分。

Mitigation: 提交敏感内容前先确认服务的数据保留条款；避免提交涉密或未授权的私人内容。

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/podcast-deep-dive)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [带时间戳和说话人标记的转写稿，以及结构化摘要分析]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [包含主旨、结构大纲、分人对谈要点及提及内容；说话人编号不代表已核实的真实身份。]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
