## Description:

当用户需要撰写或优化商品详情页、商品介绍和购买 FAQ 时使用；提供商品链接或商品资料，输出商品详情页结构、分段文案与购买 FAQ，并可按需参考同类商品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce content creators use this skill to draft or improve product detail pages and purchase FAQs from supplied product facts, with optional limited references to comparable Douyin or Xiaohongshu listings when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The floating socialdatax-skills@latest package can change between runs; a compromised upstream release could expose credentials available to the CLI.

Mitigation: Review and pin a specific package version before use, and run it with only the credentials and access needed for the requested product lookup.

Risk: The scan was partial because some local references could not be resolved, so its evidence is incomplete.

Mitigation: Resolve and review the referenced files, then reassess the skill before relying on the scan result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-detail-copywriter)
- [SocialDataX API key and product data access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with product page sections, purchase FAQs, source notes, and missing-information notes when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied product facts; online product lookup supports Douyin and Xiaohongshu, and comparable-product search is used only when requested.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
