## Description:

对比用户选定的 2–5 个商品，整理规格、卖点和价格差异，并标注价格口径、信息缺口与来源；在线查询支持抖音和小红书。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要评估已选商品的购物者和电商从业者，用于比较 2–5 个商品的规格、价格条件和可见卖点，并查看信息缺口、来源及后续核实项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 在线查询会将所选商品链接或 ID 分享给 SocialDataX，并可能消耗服务积分。

Mitigation: 可离线分析时优先使用用户提供的商品资料；需要在线查询时仅提交用户选定的商品，并使用经审查且固定版本的 CLI，以及不含无关密钥的环境。

## Reference(s):

- [商品竞品对比（ClawHub）](https://clawhub.ai/devinchen2014/skills/ecommerce-product-comparison)
- [SocialDataX AI 与 API Key 管理](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [带来源、价格口径、缺失信息和后续核实项的 Markdown 商品对比表]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [仅比较用户选定的商品；在线商品查询支持抖音和小红书，其他平台可依据用户提供的资料分析。]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
