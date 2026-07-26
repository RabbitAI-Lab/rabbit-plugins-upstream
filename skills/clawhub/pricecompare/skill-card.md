## Description: <br>
This skill helps agents search Taobao, JD, and Pinduoduo products, compare prices, find coupons, parse e-commerce share text, and convert product links into discount purchase links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangjiun1](https://clawhub.ai/user/zhangjiun1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shopping assistants and personal agents use this skill to answer price comparison, coupon lookup, share-code parsing, and discount-link conversion requests for Taobao, JD, and Pinduoduo. It is intended for users who provide product keywords, product links, or e-commerce share text and want concise purchase options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping queries, product links, and pasted e-commerce share text are sent to op.squirrel2.cn for processing. <br>
Mitigation: Install only when this data sharing is acceptable, and avoid pasting unrelated personal text into the skill. <br>
Risk: The skill performs an automatic ClawHub update check that is under-disclosed in the artifact. <br>
Mitigation: Set PRICECOMPARE_NO_VERSION_CHECK when automatic version checks are not desired. <br>
Risk: Product prices, coupons, and generated purchase links depend on external shopping API data and may change or become unavailable. <br>
Mitigation: Have the agent present results as current offers and advise users to verify price and coupon details before purchase. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhangjiun1/skills/pricecompare) <br>
- [Publisher Profile](https://clawhub.ai/user/zhangjiun1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-formatted text with product details, prices, coupon information, and purchase links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns formatted strings for direct presentation by the agent; external shopping API responses determine product availability and pricing.] <br>

## Skill Version(s): <br>
1.5.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
