## Description:

对比用户选定的商品，整理可追溯的规格、价格和卖点差异表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和商品分析人员可比较已选定的 2–5 个商品，核对规格、价格条件及可见卖点。抖音和小红书商品可按需在线查询；其他平台依赖用户提供的商品资料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 在线查询会运行未固定版本的第三方 npm 包，可能增加供应链及凭据暴露风险。

Mitigation: 使用前审核并固定可信版本，仅提供必需的 SOCIALDATAX_API_KEY，避免开放其他密钥或广泛的文件访问权限。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-comparison)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown table and brief analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [标注商品来源、观察时间、价格口径和信息缺口；证据不足时不作强制排名。]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
