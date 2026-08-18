## Description:

Shopee store media skill for uploading images and chunked videos through LinkFox's Shopee developer proxy for the Shopee Open API Media module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and developers use this skill to upload Shopee store images and manage chunked video upload flows after selecting a shop through the companion LinkFox authentication skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes LinkFox account onboarding, API-key creation, and payment-order workflows in addition to media upload.

Mitigation: Install it only when those onboarding and billing helpers are expected; prefer the self-service LinkFox key flow when possible and treat API keys and SMS codes as secrets.

Risk: LINKFOX_* base URL environment variables can affect which hosts receive requests.

Mitigation: Verify these environment variables point to trusted LinkFox hosts before running the skill.

Risk: Generated linkfox response directories can retain API responses and account or payment workflow artifacts.

Mitigation: Keep generated response directories out of shared repositories and backups unless retaining that data is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media)
- [Media API reference](references/api.md)
- [Onboarding reference](references/onboarding.md)
- [Shopee upload_image documentation](https://open.shopee.com/documents/v2/v2.media.upload_image?module=130&type=1)
- [Shopee init_video_upload documentation](https://open.shopee.com/documents/v2/v2.media.init_video_upload?module=130&type=1)
- [Shopee upload_video_part documentation](https://open.shopee.com/documents/v2/v2.media.upload_video_part?module=130&type=1)
- [Shopee complete_video_upload documentation](https://open.shopee.com/documents/v2/v2.media.complete_video_upload?module=130&type=1)
- [Shopee get_video_upload_result documentation](https://open.shopee.com/documents/v2/v2.media.get_video_upload_result?module=130&type=1)
- [Shopee cancel_video_upload documentation](https://open.shopee.com/documents/v2/v2.media.cancel_video_upload?module=130&type=1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete responses are written under linkfox/<date>/<session>/data; small responses can print inline, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
