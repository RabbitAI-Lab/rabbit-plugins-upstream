## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个抖音商品链接或商品 ID，输出注明价格口径、信息缺口和来源的商品差异表。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can compare 2–5 Douyin products they select, reviewing specifications, selling points, price conditions, missing information, and source links in a traceable comparison table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted product links or IDs are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Submit only product details the user intends to share; confirm expected credit use before making requests.

Risk: The documented commands execute the latest external CLI package, so its behavior can change between runs.

Mitigation: Review and pin a specific CLI version before routine use, and provide only the access needed for the comparison.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-comparison)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Guidance]

**Output Format:** [Markdown comparison table with source links, price conditions, missing information, and follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 2–5 user-selected products; reports only returned or user-provided details and separates non-comparable price conditions.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
