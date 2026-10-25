## Description:

当用户需要撰写或优化商品详情页、商品介绍和购买 FAQ 时使用；可根据商品资料起草文案，并按需参考抖音与小红书同类商品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要撰写或优化电商商品详情页的用户，根据用户提供的商品资料生成详情页结构、分段文案和购买 FAQ；资料不足时标出待补信息，也可按需查询抖音或小红书商品并参考少量同类商品。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional online lookups send product links, IDs, or keywords to SocialDataX and may consume paid credits.

Mitigation: Use supplied product information for offline drafting when possible; avoid confidential inputs and confirm online lookup is authorized.

Risk: The CLI dependency is unpinned.

Mitigation: Review and pin the CLI version before running in a restricted environment, and protect the SOCIALDATAX_API_KEY.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/ecommerce-detail-copywriter)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown with product-page copy, purchase FAQs, source notes, and missing-information checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copy-ready drafts distinguish supplied or retrieved product facts from suggestions and identify information that needs confirmation.]

## Skill Version(s):

0.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
