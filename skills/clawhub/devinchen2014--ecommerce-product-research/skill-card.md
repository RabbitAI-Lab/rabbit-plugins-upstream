## Description:

提供商品类目或已有商品资料，整理电商选品候选清单，列出可见价格、匹配条件、入选理由和待核实事项。预算与受众有则提供；已有资料可直接分析，无需 API Key。在线商品查询支持抖音与小红书。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要筛选电商商品的用户，依据提供的类目、预算和受众整理候选商品、可见价格、匹配理由及待核实事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI is invoked through a changeable latest release and may access the API key.

Mitigation: Review and pin a CLI release before allowing it to read credentials.

Risk: Online lookup sends search terms and product identifiers to SocialDataX.

Mitigation: Use online lookup only when that data sharing is acceptable; supplied product data can be analyzed without online lookup.

Risk: The security scan was partial because some referenced paths could not be resolved.

Mitigation: Review the complete release and unresolved references before deployment.

## Reference(s):

- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/ecommerce-product-research)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown table with concise notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A first-pass list of up to five candidates with visible price context, selection reasons, sources, and verification items; includes suggested products for follow-up review.]

## Skill Version(s):

0.1.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
