## Description:

Helps agents working with TikTok Shop ERP after-sales workflows retrieve valid rejection reasons for return or cancellation requests through LinkFox-authorized shop access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents managing TikTok Shop after-sales workflows use this skill to retrieve valid rejection reasons before refusing a return or cancellation request. It also supports authorized-shop lookup so the agent can supply the required shop cipher for the reject-reasons request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants authenticated TikTok Shop ERP gateway access beyond the narrow reject-reasons lookup.

Mitigation: Install it only for agents trusted with LinkFox TikTok Shop ERP access, and prefer the named get_reject_reasons workflow over the generic proxy unless broader access is required.

Risk: The generic proxy can call whitelisted return_refund and authorization paths using the selected shop authorization.

Mitigation: Limit use to authorized shops and expected after-sales tasks; ask the publisher to remove the generic proxy if the deployment should be restricted to the documented read-only endpoint.

Risk: The skill depends on LinkFox authorization and shop selection data.

Mitigation: Use server-managed tokens via openId and avoid exposing full credentials, access tokens, or sensitive shop identifiers in prompts, logs, and shared outputs.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-return-refund)
- [TikTok Shop ERP Return & Refund API Reference](artifact/references/api.md)
- [Get Reject Reasons](artifact/references/apis/get_reject_reasons.md)
- [Get Authorized Shops](artifact/references/apis/get_authorized_shops.md)
- [TikTok Shop Partner Center: Get Reject Reasons](https://partner.tiktokshop.com/docv2/page/get-reject-reasons-202309)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox agent API credentials, an authorized TikTok Shop ERP openId, and a return_or_cancel_id for the reject-reasons lookup.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
