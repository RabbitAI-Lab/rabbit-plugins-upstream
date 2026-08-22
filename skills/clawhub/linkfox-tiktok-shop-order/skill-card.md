## Description:

Helps agents query TikTok Shop ERP order lists, order details, and authorized shop metadata through LinkFox's TikTok Shop order workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External TikTok Shop operators and agents use this skill to inspect ERP shop authorization, filter order lists by status or time, and retrieve order details for authorized shops. It is limited to order lookup workflows and does not implement authorization, fulfillment, cancellation, refunds, or creator-side order handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive TikTok Shop buyer, shipping, tax, payment, and order data when order detail APIs are used.

Mitigation: Limit use to authorized shop operators, avoid displaying full addresses, phone numbers, tax identifiers, or payment details unless necessary, and redact sensitive fields in summaries.

Risk: The generic order proxy path can broaden access beyond the named order helper scripts.

Mitigation: Prefer named API scripts for routine use and tightly gate or remove order_proxy.py before production deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-order)
- [TikTok Shop ERP Order API Reference](references/api.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [Get Order List](references/apis/get_order_list.md)
- [Get Order Detail](references/apis/get_order_detail.md)
- [TikTok Shop Get Order List Documentation](https://partner.tiktokshop.com/docv2/page/get-order-list-202309)
- [TikTok Shop Get Authorized Shops Documentation](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Get Order Detail Documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include order status, order IDs, monetary fields, timestamps, shop metadata, and detailed buyer or shipping fields returned by authorized TikTok Shop APIs.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
