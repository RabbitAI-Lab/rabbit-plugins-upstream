## Description:

Provides agents with scripts and references to upload Shopee shop images and videos through LinkFox-mediated Shopee MediaSpace APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and commerce operators use this skill to upload images and chunked videos for authorized Shopee shops, using LinkFox gateway calls and saved JSON responses for follow-up listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled onboarding flow can collect SMS login codes, create API keys, list plans, and create payment orders beyond the core media upload task.

Mitigation: Use the onboarding flow only when you explicitly trust the publisher and session; otherwise obtain and configure the LinkFox API key outside the skill.

Risk: Full gateway responses are saved to a local linkfox session data directory and may contain shop, media, or upload metadata.

Mitigation: Review and remove saved response files after use, and avoid sharing workspaces that contain generated linkfox data.

Risk: The skill sends authorized Shopee shop media operations through the LinkFox gateway.

Mitigation: Confirm the intended shopId or merchantId before running commands and use only accounts authorized for the target Shopee shop.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media-space)
- [MediaSpace API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Shopee MediaSpace init_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.init_video_upload?module=91&type=1)
- [Shopee MediaSpace upload_image documentation](https://open.shopee.com/documents/v2/v2.media_space.upload_image?module=91&type=1)
- [Shopee MediaSpace upload_video_part documentation](https://open.shopee.com/documents/v2/v2.media_space.upload_video_part?module=91&type=1)
- [Shopee MediaSpace complete_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.complete_video_upload?module=91&type=1)
- [Shopee MediaSpace get_video_upload_result documentation](https://open.shopee.com/documents/v2/v2.media_space.get_video_upload_result?module=91&type=1)
- [Shopee MediaSpace cancel_video_upload documentation](https://open.shopee.com/documents/v2/v2.media_space.cancel_video_upload?module=91&type=1)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses saved to files, with stdout JSON or concise text summaries and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under a linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
