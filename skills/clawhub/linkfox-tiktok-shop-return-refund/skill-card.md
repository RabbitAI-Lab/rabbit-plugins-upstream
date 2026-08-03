## Description: <br>
Provides TikTok Shop ERP return/refund helpers through LinkFox for listing authorized shops and retrieving valid reject reasons for a return or cancellation request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, support operators, and developers use this skill to inspect TikTok Shop return or cancellation requests and retrieve the allowed reject-reason list before taking follow-up action. It depends on an authenticated LinkFox TikTok Shop ERP context and a valid return_or_cancel_id. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an authenticated TikTok Shop ERP context to list authorized shops and proxy allowed authorization or return_refund API paths, which is broader than a narrow reject-reason lookup. <br>
Mitigation: Install it only in trusted gateway environments where that broader authenticated shop and return/refund access is acceptable. <br>
Risk: Reject-reason lookup requires a valid return_or_cancel_id and shop context, so using the wrong shop or request identifier can return irrelevant operational data. <br>
Mitigation: Confirm the selected openId, shop_cipher or shop_id, and return_or_cancel_id before presenting reasons or advising follow-up actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-return-refund) <br>
- [TikTok Shop ERP Return & Refund API Reference](references/api.md) <br>
- [Get Reject Reasons](references/apis/get_reject_reasons.md) <br>
- [Get Authorized Shops](references/apis/get_authorized_shops.md) <br>
- [TikTok Shop Partner Center: Get Reject Reasons](https://partner.tiktokshop.com/docv2/page/get-reject-reasons-202309) <br>
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses with Markdown and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires openId from linkfox-tiktok-shop-auth and may require shop_cipher or shop_id for shop-scoped return/refund calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
