## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个商品链接或商品资料，输出注明价格口径、信息缺口和来源的商品差异表。在线商品能力支持抖音与小红书，其他平台可基于用户提供的资料分析。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要比较已选商品的用户，整理 2–5 个商品的规格、价格口径、可见卖点和信息缺口，帮助准备可追溯的竞品对照表。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups share selected product links or IDs with SocialDataX and may consume service credits.

Mitigation: Limit lookups to products selected by the user; analyze supplied product information without an online lookup when appropriate.

Risk: Online CLI use relies on external software and an API key.

Mitigation: Use a reviewed, fixed CLI version and store the API key in the client's secret facility; keep local key configuration out of version control.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-comparison)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown product comparison table with sources, price basis, missing information, and follow-up checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 2–5 user-selected products; distinguishes unavailable fields and price conditions, and avoids unsupported rankings.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
