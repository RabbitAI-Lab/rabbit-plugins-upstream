## Description:

Queries TikTok creator shop, showcase, and live-bag products through LinkFox so an agent can return product data and product_id values for shoppable video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, creators, and agent developers use this skill to search TikTok creator-bound shop products or list showcase and live-bag products. The returned product_id values support downstream shoppable video precheck and publishing workflows in a separate TikTok video skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes onboarding flows that can create or retrieve a LinkFox API key by SMS login.

Mitigation: Use the onboarding path only when intentionally registering or recovering access, verify the LinkFox destination first, and do not share SMS codes outside the trusted flow.

Risk: The skill can inspect paid plans, create payment orders, and render payment QR codes.

Mitigation: Run billing commands only after an explicit user request and review plan IDs, payment methods, and payment destinations before proceeding.

Risk: API keys and full API responses may be printed or saved locally.

Mitigation: Treat printed keys and saved response files as sensitive, store them only in trusted directories, and avoid pasting or sharing them unnecessarily.

Risk: Environment variables can redirect LinkFox endpoint traffic.

Mitigation: Before execution, verify LinkFox endpoint environment variables point to trusted LinkFox domains.

## Reference(s):

- [TikTok Video Products API Reference](artifact/references/api.md)
- [LinkFox Auth and Billing Onboarding](artifact/references/onboarding.md)
- [TikTok Shop Get Shop Products 202509](https://partner.tiktokshop.com/docv2/page/get-shop-products-202509)
- [TikTok Shop Get Showcase Products 202405](https://partner.tiktokshop.com/docv2/page/get-showcase-products-202405)
- [Shoppable Video Integration Solutions V2025.Q4.01](https://bytedance.sg.larkoffice.com/docx/Os8tdPkaVo2QFBxhSRIlQwBAg9f)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-products)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized TikTok creator openId; large responses may be saved locally for field extraction.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
