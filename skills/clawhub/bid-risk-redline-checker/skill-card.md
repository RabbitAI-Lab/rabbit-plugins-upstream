## Description:

结合招中标历史数据识别招标项目的废标风险与限制性信号，并提供竞争分析、报价参考和投标建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队可用具体招标项目查询历史招中标数据，评估资格限制、采购方与潜在竞争者、报价区间及参与风险，形成投标决策参考。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 首次使用可能向服务商注册账户并保存 API 凭证。

Mitigation: 仅在用户同意后注册；妥善保护本地凭证，不在对话或报告中公开。

Risk: HTML 报告可能包含可直接访问相关页面的签名链接。

Mitigation: 分享前检查报告及链接，仅发送给预期可访问这些页面的收件人。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker)
- [分析工作流](artifact/references/workflow.md)
- [API 工具速查](artifact/references/api-quick.md)
- [报告模板](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Markdown 决策报告；完整分析默认另存为 HTML 报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [报告包含风险清单、报价参考、数据缺口与免责声明；HTML 中的签名访问链接应谨慎分享。]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
