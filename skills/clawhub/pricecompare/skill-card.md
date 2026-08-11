## Description:

购物省钱宝 helps agents search Taobao, JD, and Pinduoduo products, compare prices, find coupons, parse shopping share text, and convert product links into discount links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangjiun1](https://clawhub.ai/user/zhangjiun1)

### License/Terms of Use:

MIT-0

## Use Case:

External shoppers and shopping assistants use this skill to compare prices, discover coupons, parse e-commerce share messages, and generate discount purchase links across JD, Taobao, and Pinduoduo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping messages, product links, and share text may be sent to op.squirrel2.cn for processing.

Mitigation: Install and use the skill only when users and operators are comfortable sending that shopping content to the remote service; avoid submitting unrelated sensitive text.

Risk: The skill automatically checks ClawHub for updates unless PRICECOMPARE_NO_VERSION_CHECK is set.

Mitigation: Set PRICECOMPARE_NO_VERSION_CHECK in environments where automatic update checks or extra outbound contact are not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhangjiun1/skills/pricecompare)
- [Publisher Profile](https://clawhub.ai/user/zhangjiun1)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted text with product summaries, coupon details, comparison results, and purchase links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include product names, prices, coupon information, sales text, platform labels, and promotion links returned by the remote shopping service.]

## Skill Version(s):

1.5.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
