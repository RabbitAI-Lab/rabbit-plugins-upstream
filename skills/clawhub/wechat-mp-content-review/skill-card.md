## Description:

当用户提供公众号文章链接、账号 ID 或明确的文章名单，需要公众号内容复盘、近期推文对比、题材表现分析或读者反馈整理时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

公众号运营人员可用此技能复盘指定文章或账号近期文章，比较可见互动数据、整理读者反馈，并提出下一轮选题建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 技能会运行未固定版本的 CLI 包；若后续发布版本遭到篡改，可能暴露 API 凭证或使用调用账户的访问权限。

Mitigation: 运行前审查并固定到已核验的包版本；只通过技能说明的本地隐藏提示录入 API Key，不要将密钥放入聊天或日志。

## Reference(s):

- [ClawHub 技能发布页](https://clawhub.ai/devinchen2014/skills/wechat-mp-content-review)
- [SocialDataX AI 服务与 API Key 管理](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [包含文章对照表、证据摘要和建议的 Markdown 复盘报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [最多覆盖 10 篇文章；未取得的数据明确标注，不补造数值。]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
