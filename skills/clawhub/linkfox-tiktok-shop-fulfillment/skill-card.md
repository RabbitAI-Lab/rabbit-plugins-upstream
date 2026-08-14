## Description:

Helps agents use LinkFox's TikTok Shop ERP gateway to fetch authorized shops and query order split attributes for fulfillment decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operations agents and developers use this skill to retrieve shop_cipher values and check whether TikTok Shop orders can or must be split before fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A credentialed LinkFox proxy can call fulfillment and authorization paths beyond the primary split-attribute lookup.

Mitigation: Review before installing with real TikTok Shop access; prefer named scripts such as get_order_split_attributes.py and restrict allowed method, path, and gateway host when the generic proxy is not needed.

Risk: The skill depends on LinkFox API credentials and ERP openId to access seller shop and order fulfillment data.

Mitigation: Grant credentials only in trusted environments, verify shop_cipher and order_ids before use, and avoid displaying complete access tokens.

## Reference(s):

- [TikTok Shop ERP Fulfillment API Reference](artifact/references/api.md)
- [Get Authorized Shops](artifact/references/apis/get_authorized_shops.md)
- [Get Order Split Attributes](artifact/references/apis/get_order_split_attributes.md)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Partner Center: Get Order Split Attributes](https://partner.tiktokshop.com/docv2/page/get-order-split-attributes-202309)
- [TikTok Shop Seller Authorization Guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0)
- [TikTok Shop API Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON API responses with concise text guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and ERP openId; agents should avoid displaying complete access tokens.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
