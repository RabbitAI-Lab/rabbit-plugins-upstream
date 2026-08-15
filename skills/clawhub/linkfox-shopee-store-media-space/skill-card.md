## Description:

Helps agents upload Shopee store images and videos through LinkFox's Shopee MediaSpace gateway, covering init_video_upload, upload_video_part, complete_video_upload, get_video_upload_result, cancel_video_upload, and upload_image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, sellers, and developers use this skill to upload images and chunked videos for authorized Shopee stores. It guides agents through the MediaSpace upload sequence and returns Shopee media URLs or upload status for downstream listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Shopee media upload requests through LinkFox services and stores complete API responses locally.

Mitigation: Use it only for intended stores and media, review saved response files for sensitive data, and delete local response logs when they are no longer needed.

Risk: The bundled onboarding flow can request phone/SMS login, create API keys, and initiate paid credit purchases.

Mitigation: Provide verification codes or create payment orders only when those account and billing actions are intentional, and verify plan and payment details before proceeding.

Risk: Custom endpoint environment variables can redirect gateway or login traffic.

Mitigation: Keep default endpoints unless you control and trust the destination service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media-space)
- [MediaSpace API reference](references/api.md)
- [Onboarding and billing guidance](references/onboarding.md)
- [Shopee init_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.init_video_upload?module=91&type=1)
- [Shopee upload_image documentation](https://open.shopee.com/documents/v2/v2.media_space.upload_image?module=91&type=1)
- [Shopee upload_video_part documentation](https://open.shopee.com/documents/v2/v2.media_space.upload_video_part?module=91&type=1)
- [Shopee complete_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.complete_video_upload?module=91&type=1)
- [Shopee get_video_upload_result documentation](https://open.shopee.com/documents/v2/v2.media_space.get_video_upload_result?module=91&type=1)
- [Shopee cancel_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.cancel_video_upload?module=91&type=1)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; full API responses are saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses print a summary while preserving the complete response under a linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
