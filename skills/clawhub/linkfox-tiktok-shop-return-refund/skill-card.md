## Description:

Helps agents retrieve TikTok Shop return and cancellation reject reasons, with supporting shop authorization lookup, for ERP seller after-sales workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agent developers use this skill to obtain valid TikTok Shop reject reasons before refusing a return or cancellation request. It requires a selected ERP shop through linkfox-tiktok-shop-auth and can also retrieve authorized shop information needed to resolve shop_cipher values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented mainly as reject-reason lookup but also exposes shop authorization lookup and a generic ERP proxy for TikTok Shop return_refund and authorization paths.

Mitigation: Install only where broad TikTok Shop ERP return/refund and shop-discovery access is intended; review or ask the publisher to remove or tightly allowlist the generic proxy and authorization-facing scripts if only reject-reason lookup is needed.

Risk: The skill depends on a selected authorized shop and uses server-side token resolution through linkfox-tiktok-shop-auth.

Mitigation: Confirm linkfox-tiktok-shop-auth is installed and pass only the required openId and return_or_cancel_id; do not provide or expose full ERP tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-return-refund)
- [TikTok Shop ERP Return & Refund API Reference](references/api.md)
- [Get Reject Reasons](references/apis/get_reject_reasons.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [TikTok Shop Get Reject Reasons documentation](https://partner.tiktokshop.com/docv2/page/get-reject-reasons-202309)
- [TikTok Shop Get Authorized Shops documentation](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Seller authorization guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY and an ERP openId from linkfox-tiktok-shop-auth.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
