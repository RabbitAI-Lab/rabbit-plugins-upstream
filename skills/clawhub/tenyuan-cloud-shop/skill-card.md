## Description:

TenYuan Cloud Shop turns one sentence or product photo into a shareable mini shop page with product images, AI voiceover, sharing copy, and phone or WeChat contact details for offline sales lead generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnnyruan](https://clawhub.ai/user/johnnyruan)

### License/Terms of Use:

MIT

## Use Case:

External sellers and small merchants use this skill to create a public product showcase page from a short description or product photo, then share the generated link, copy, and voiceover with prospective buyers. The skill is for display and lead generation only; sales, payment, fulfillment, and disputes happen outside the platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, descriptions, prices, phone or WeChat details, and optional QR codes are sent to ruancyai.com and may be shown on a public shareable page.

Mitigation: Only submit information intended for public display, and verify contact details and QR codes before creating or sharing a shop page.

Risk: Generated shop content, sharing copy, and AI voiceover may be inaccurate or overstate product claims.

Mitigation: Review generated names, slogans, prices, origin claims, share copy, and voiceover text before sharing, especially for food, alcohol, and health-related products.

Risk: The release charges for successful shop-page creation and depends on payment and refund handling.

Mitigation: Confirm the fee, payment prompt, refund conditions, and created page link before authorizing payment.

Risk: The hosted backend may be unavailable or missing model or TTS configuration.

Mitigation: If the API is unavailable or returns service errors, tell the user the cloud shop service is temporarily unavailable and do not fabricate links or shop data.

## Reference(s):

- [API contract](references/api.md)
- [Hosted cloud shop service](https://ruancyai.com/cloud)
- [ClawHub skill listing](https://clawhub.ai/johnnyruan/skills/tenyuan-cloud-shop)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text containing the generated shop link, sharing copy, voiceover URL, and user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include URLs for the hosted shop page, generated audio, and optional QR-code-backed contact material.]

## Skill Version(s):

0.3.2 (source: frontmatter and changelog, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
