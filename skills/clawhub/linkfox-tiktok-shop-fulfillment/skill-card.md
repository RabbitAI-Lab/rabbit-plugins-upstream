## Description:

Helps agents use LinkFox's TikTok Shop ERP fulfillment integration to retrieve authorized shop ciphers and check whether orders can or must be split before fulfillment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations agents use this skill to prepare TikTok Shop ERP fulfillment workflows by resolving authorized shops and checking order split attributes before package handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reports suspicious risk because the generic fulfillment proxy can reach broader seller-account operations than the split-attribute lookup emphasized by the description.

Mitigation: Install only if broader fulfillment proxy access is intended; otherwise restrict use to get_authorized_shops and get_order_split_attributes or remove the generic proxy entry point.

Risk: The skill needs LinkFox/TikTok Shop seller-account access.

Mitigation: Use only with authorized seller accounts, avoid exposing access tokens, and review returned shop and order data before acting on fulfillment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-fulfillment)
- [TikTok Shop ERP Fulfillment API Reference](references/api.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [Get Order Split Attributes](references/apis/get_order_split_attributes.md)
- [TikTok Shop Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Get Order Split Attributes](https://partner.tiktokshop.com/docv2/page/get-order-split-attributes-202309)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include shop_cipher values, order split attributes, upstream API status, and gateway response bodies.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
