## Description:

将脱敏退款或退货原因和商品信息整理为可追溯的原因分类、按原始记录核算的计数与商品页改进建议，适合中文小店、小说作者和自媒体创作者复盘售后；缺少关键字段时明确列出缺口，不编造事实、不作财务结论或代替客服回复。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Chinese-speaking small-shop operators, fiction authors, and self-media creators use the skill to review de-identified return or refund records, count traceable reason categories, and prepare verifiable product-page improvement suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Original record fields, including customer identifiers or sensitive notes, may be reproduced in the report.

Mitigation: Remove customer identifiers and sensitive notes before supplying records.

Risk: Suggested product-page changes may be inaccurate if applied without checking the underlying product details.

Mitigation: Verify each proposed change against the product before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xxjrq/skills/shop-returns-reason-summary-cn)
- [Saleor public e-commerce domain context](https://github.com/saleor/saleor)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown with tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves supplied record values, reports missing fields, and separates observed facts from recommendations.]

## Skill Version(s):

1.0.0 (source: manifest and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
