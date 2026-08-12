## Description:

Helps agents retrieve TikTok Shop ERP authorized shops, order lists, and order details through LinkFox's TikTok Shop order tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and agents use this skill to query TikTok Shop ERP order data, including authorized shops, filtered order lists, and order details. It depends on the LinkFox TikTok Shop authorization skill for ERP openId selection and does not implement authorization, fulfillment, cancellation, refunds, or creator-side orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags broader authenticated proxy and shop-discovery capabilities than the order-only description clearly scopes.

Mitigation: Prefer the named order scripts and use order_proxy.py only when an intentional broader order or authorization path is required.

Risk: The skill processes TikTok Shop ERP order data, which can include sensitive customer and business information.

Mitigation: Minimize, mask, and avoid unnecessary retention of returned order data.

Risk: The skill depends on LinkFox authorization and gateway handling for TikTok Shop ERP access.

Mitigation: Install and run it only in environments where LinkFox is trusted with TikTok Shop ERP order data and required credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-order)
- [LinkFox TikTok Shop ERP Order API Reference](references/api.md)
- [Get Authorized Shops Reference](references/apis/get_authorized_shops.md)
- [Get Order List Reference](references/apis/get_order_list.md)
- [Get Order Detail Reference](references/apis/get_order_detail.md)
- [Get Order Detail 202309 Reference](references/apis/get_order_detail_202309.md)
- [TikTok Shop Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309)
- [TikTok Shop Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Get Order Detail 202507](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507)
- [TikTok Shop Get Order Detail 202309](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns LinkFox developerProxy responses and parsed TikTok Shop order data when calls succeed.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
