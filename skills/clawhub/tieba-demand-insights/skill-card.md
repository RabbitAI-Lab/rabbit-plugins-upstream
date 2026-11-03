## Description:

当用户需要做百度贴吧用户需求研究、产品痛点归纳、购买顾虑整理或常见问题分析时使用。输入产品关键词、吧名或帖子链接，基于帖子与楼层讨论输出带原话依据的需求报告。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要分析百度贴吧讨论的产品与市场研究人员，帮助他们从关键词、吧名或帖子链接中整理用户需求、使用场景、痛点、购买顾虑和常见问题，并以帖子与楼层证据支持结论。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 研究输入会发送给 SocialDataX，调用会消耗账户积分。

Mitigation: 避免在搜索词中包含机密信息；扩大采样前先确认服务的费用和账户额度。

Risk: 直接 CLI 示例会下载可能随时间变化的软件包版本。

Mitigation: 重复或敏感工作流使用经过审查并固定版本的 CLI。

Risk: CLI 鉴权依赖 API Key，凭证可能因不当配置而暴露。

Mitigation: 通过客户端支持的 Secret 或环境变量保存 Key；不要将其写入聊天、日志或技能文件。

## Reference(s):

- [SocialDataX 服务与 API Key 管理](https://socialdatax.com/ai?from=clawhub)
- [ClawHub 技能发布页](https://clawhub.ai/devinchen2014/skills/tieba-demand-insights)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown 报告，附简短原话、帖子链接或 ID，以及楼层或评论 ID（如有）]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [列出样本量、观察范围、缺失信息、证据强弱和可继续追问的问题。]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
