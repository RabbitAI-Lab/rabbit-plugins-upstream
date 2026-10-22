## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个商品链接或商品资料，输出注明价格口径、信息缺口和来源的商品差异表。在线商品能力支持抖音与小红书，其他平台可基于用户提供的资料分析。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要比较商品的用户，基于其提供的 2–5 个商品链接或资料，整理规格、价格条件、可见卖点、来源与信息缺口，帮助按关注维度评估差异。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups transmit selected product links or IDs to SocialDataX and may consume paid credits.

Mitigation: Use online lookup only when needed and with user-provided product selections; compare supplied product information without an online call when possible.

Risk: The SocialDataX API key is a secret used for online product lookups.

Mitigation: Keep SOCIALDATAX_API_KEY private and do not expose it in generated output or shared logs.

Risk: The CLI dependency runs with local permissions and can change when an unpinned latest version is used.

Mitigation: Review and pin the CLI version where practical, and run it with limited local permissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-comparison)
- [SocialDataX product and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown product-comparison table with source links and missing-information notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares only user-selected products; distinguishes price conditions and flags unavailable information instead of inventing values.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
