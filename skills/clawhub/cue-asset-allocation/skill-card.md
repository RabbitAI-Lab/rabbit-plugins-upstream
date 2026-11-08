## Description:

用 Cue 生成月度大类资产配置报告，整合全球 CPI、利率、国内宏观及资金流向，并推导股、债、商品的配置比例。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向投资者、投顾及投委会使用者，整理全球与国内宏观信息，形成月度股、债、商品配置逻辑和比例建议，供决策讨论或客户建议材料参考。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API 密钥处理说明存在矛盾，并要求用户在聊天中粘贴密钥。

Mitigation: 不要在聊天中发送 API 密钥；通过可信方式在本地配置凭据，并轮换已经分享过的密钥。

Risk: 查询和报告会使用 Cue 远程服务，客户信息可能随请求或报告内容共享。

Mitigation: 在加入客户信息前检查数据共享权限，并避免发送不必要的敏感信息。

Risk: 运行器需要单独下载，未随技能文件提供。

Mitigation: 执行前检查并固定所下载运行器的版本。

Risk: 运行会消耗 Cue 积分，低余额时技能会引导用户选择积分获取或购买方式。

Mitigation: 运行前核对余额及组织的积分和购买政策；不需要时可不继续积分补充流程。

## Reference(s):

- [Cue platform](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [结构化 Markdown 月报，包含宏观环境、配置逻辑与比例建议、风险提示和来源链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [报告经 Cue 云端服务生成并保存为 Markdown；文档说明可另行转换为 Word 或 PDF。]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter states 1.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
