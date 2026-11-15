## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个抖音商品链接或商品 ID，输出注明价格口径、信息缺口和来源的商品差异表。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

抖音商家、选品人员和市场分析人员可用它比较用户指定的 2–5 个商品，核对规格、价格条件和可见卖点，并整理带来源、缺失信息与适用场景的对比表。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a changeable latest package that could access credentials, and the security review was partial.

Mitigation: Review the package before installing, especially before entering an API key through its CLI; treat the partial scan as inconclusive.

Risk: Product URLs or IDs are sent to SocialDataX when retrieving product details.

Mitigation: Use the service only when comfortable sharing the selected product identifiers or URLs with SocialDataX.

## Reference(s):

- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown comparison table with source links, product details, price conditions, missing information, and usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 2–5 user-selected products; marks unavailable details and keeps price conditions explicit.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
