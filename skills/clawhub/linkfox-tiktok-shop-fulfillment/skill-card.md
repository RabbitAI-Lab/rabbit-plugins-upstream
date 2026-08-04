## Description: <br>
Helps agents query TikTok Shop ERP fulfillment split attributes through LinkFox, including authorized shop lookup and Get Order Split Attributes calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check TikTok Shop seller fulfillment split attributes, resolve shop ciphers, and prepare read-only fulfillment API calls through the LinkFox ERP gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic fulfillment proxy can forward broader seller-account API requests than the narrow split-attributes workflow describes. <br>
Mitigation: Prefer named API scripts for authorized shop lookup and order split attributes, or gateway-restrict proxy use to documented read-only fulfillment endpoints. <br>
Risk: The skill handles TikTok Shop operational identifiers such as openId, shop_cipher, shop IDs, and order IDs. <br>
Mitigation: Treat these values as sensitive operational data; avoid unnecessary logging, sharing, or persistence. <br>
Risk: The skill requires a LinkFox API key and depends on the separate TikTok Shop auth skill for seller authorization. <br>
Mitigation: Install only in environments where LinkFox access is intended, API keys are managed securely, and the auth dependency has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-fulfillment) <br>
- [TikTok Shop ERP Fulfillment API Reference](references/api.md) <br>
- [Get Authorized Shops](references/apis/get_authorized_shops.md) <br>
- [Get Order Split Attributes](references/apis/get_order_split_attributes.md) <br>
- [TikTok Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) <br>
- [TikTok Partner Center: Get Order Split Attributes](https://partner.tiktokshop.com/docv2/page/get-order-split-attributes-202309) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with JSON inputs and Python shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON responses from LinkFox developerProxy calls, including resolved path, query string, shop cipher, and upstream fulfillment data.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
