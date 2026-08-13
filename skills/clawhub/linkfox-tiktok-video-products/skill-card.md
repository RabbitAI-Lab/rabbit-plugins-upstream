## Description:

Looks up TikTok creator shop, showcase, and live-bag products through LinkFox so an agent can return product IDs for downstream shoppable video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to search TikTok creator-bound shop products and list showcase or live-bag products. The main output is product data, especially product_id values, for later shoppable video precheck or publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes LinkFox account onboarding, API key generation, and payment-order flows in addition to TikTok product lookup.

Mitigation: Review the package before installation and provide SMS codes or create payment orders only when that flow was intentionally initiated.

Risk: Configurable LinkFox base URL environment variables can redirect requests away from the default LinkFox services.

Mitigation: Keep LinkFox base URL variables unset or set them only to trusted LinkFox endpoints.

Risk: The product lookup flow depends on authorized TikTok creator account selection.

Mitigation: Use the companion auth skill to select an openId and avoid requesting, displaying, or passing raw creator tokens in this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-products)
- [TikTok Video Products API reference](references/api.md)
- [LinkFox onboarding and billing guidance](references/onboarding.md)
- [TikTok Shop Get Shop Products 202509](https://partner.tiktokshop.com/docv2/page/get-shop-products-202509)
- [TikTok Shop Get Showcase Products 202405](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405)
- [Shoppable video Integration Solutions V2025.Q4.01](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with concise markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist large API responses to local JSON files for later field extraction.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
