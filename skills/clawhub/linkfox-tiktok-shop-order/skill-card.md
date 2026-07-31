## Description: <br>
Routes TikTok Shop ERP order workflows through LinkFox tooling so an agent can list authorized shops, search order lists, and retrieve order details after shop authorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents supporting TikTok Shop ERP sellers and operators use this skill to obtain a shop cipher, search orders by status or time window, and retrieve order details for operational review. It depends on the companion authorization skill for seller shop selection and does not handle fulfillment, cancellation, refund, or creator-side orders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic order_proxy.py path can reach broader authorization/order API paths and methods than the named list/detail helpers. <br>
Mitigation: Prefer the named scripts for routine use, restrict access to order_proxy.py, and review path, method, query string, and body before execution. <br>
Risk: Order detail responses can contain buyer, shipping, payment, price, tax, and package information. <br>
Mitigation: Avoid logging raw responses, redact customer PII in shared outputs, and request only the order fields needed for the task. <br>
Risk: The skill depends on the LinkFox gateway and the separate authorization skill for seller access. <br>
Mitigation: Install only in environments that trust LinkFox services, limit use to authorized operators, and verify shop selection before querying orders. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-order) <br>
- [TikTok Shop ERP Order API Reference](artifact/references/api.md) <br>
- [Get Authorized Shops reference](artifact/references/apis/get_authorized_shops.md) <br>
- [Get Order List reference](artifact/references/apis/get_order_list.md) <br>
- [Get Order Detail 202507 reference](artifact/references/apis/get_order_detail.md) <br>
- [Get Order Detail 202309 reference](artifact/references/apis/get_order_detail_202309.md) <br>
- [TikTok Shop Get Authorized Shops documentation](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) <br>
- [TikTok Shop Get Order List documentation](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) <br>
- [TikTok Shop Get Order Detail 202507 documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) <br>
- [TikTok Shop Get Order Detail 202309 documentation](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May surface JSON responses from TikTok Shop order APIs through LinkFox scripts; responses can include customer and order data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
