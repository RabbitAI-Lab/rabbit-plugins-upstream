## Description:

帮助用户比较 2–5 个抖音商品的规格与卖点，并生成注明价格口径、信息缺口和来源的对比表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要进行抖音商品选品与竞品分析的商家和运营人员，比较用户选定的 2–5 个商品，并整理规格、价格条件、可见卖点及待核实信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 商品链接或 ID 会通过 SocialDataX 处理，并可能消耗服务额度。

Mitigation: 确认提交的商品对象和调用符合预期；将 API Key 保存在 Secret 管理工具中。

Risk: 外部下载的 CLI 和托管服务未经过审计。

Mitigation: 使用经过审查并固定版本的 CLI；输出中保留来源和价格口径，便于核对返回信息。

## Reference(s):

- [SocialDataX API access and key management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/douyin-product-comparison)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown comparison table with product sources, specifications, price terms, visible selling points, information gaps, and follow-up notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 2–5 user-selected products; marks unavailable information and distinguishes price conditions.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
