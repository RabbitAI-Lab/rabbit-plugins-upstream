## Description:

将财报或公告中的投资性房地产披露整理为逐项附原句和来源定位的登记表，并明确标出未取到的信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

财务分析人员和研究人员可用此技能，从年报、半年报或公告中登记投资性房地产的计量模式、余额、转换与处置信息，并逐项保留可回查的原文依据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 使用长附件解析服务时，可能会向外部服务发送文件内容。

Mitigation: 提交前检查附件是否含敏感信息，并确认组织允许将其发送至该服务。

Risk: 检查脚本首次运行会在用户目录写入持久化使用标记。

Mitigation: 安装前审阅此行为；如不希望保留标记，可在运行后检查并删除对应文件。

Risk: 安全证据指出财务一致性检查存在缺口，且本次扫描不完整。

Mitigation: 将检查结果作为辅助提示，并逐项对照被引用的报告原文；安装前审阅文件传输行为和检查器。

## Reference(s):

- [Cue data access setup](https://cuecue.cn/hub/mcp)
- [Cue document parsing service](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [七节结构化 Markdown 登记表，逐项附披露原句、定位锚点和来源编号]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [缺失信息明确标为未取到；仅记录披露，不提供估值、处置建议或投资评级。]

## Skill Version(s):

0.1.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
