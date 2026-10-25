## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个抖音商品链接或商品 ID，输出注明价格口径、信息缺口和来源的商品差异表。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can compare 2–5 Douyin products they select, reviewing specifications, price conditions, visible selling points, missing information, and source details without unsupported rankings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product URLs or IDs are sent to SocialDataX, and lookups may consume paid credits.

Mitigation: Only submit product information the user is comfortable sharing, and consider credit usage before running lookups.

Risk: The example commands use the latest external package release, whose implementation is not bundled with this skill.

Mitigation: Protect the API key and consider using a reviewed, fixed package version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-comparison)
- [SocialDataX skill and API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown product-comparison table with source details, price terms, missing fields, and comparison notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares 2–5 user-selected products; separates promotional claims from evidence and avoids unsupported rankings.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
