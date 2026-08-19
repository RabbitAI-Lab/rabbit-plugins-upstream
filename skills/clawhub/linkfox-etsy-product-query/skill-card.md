## Description:

按多维度筛选 Etsy 商品，包括关键词或 URL、价格、销量、收藏、评论、上架时间、类目、商品类型和 Pick/Bestsell/Raving 标签。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce analysts use this skill to query and filter Etsy listings by product attributes, performance signals, listing state, and marketplace tags while managing LinkFox authentication and billing when required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key, and onboarding can expose account or API-key details.

Mitigation: Use only accounts intended for this workflow, avoid sharing secrets, configure credentials through environment variables, and rotate or remove keys if exposed.

Risk: The skill can consume paid LinkFox credits and includes payment-order creation.

Mitigation: Confirm query page size, expected returned item count, plan selection, and payment method before running chargeable or order commands.

Risk: The query script can write complete API responses and cache files to a local linkfox directory.

Mitigation: Review and clean local linkfox output and cache directories after use, especially when queries or response data are sensitive.

## Reference(s):

- [_ehunt_productQuery API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-product-query)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses may be saved under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.9 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
