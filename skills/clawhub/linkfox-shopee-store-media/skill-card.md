## Description:

Shopee-店铺媒体 lets agents upload images and manage chunked video uploads through the Shopee Open Platform Media APIs via LinkFox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and commerce operators use this skill to call Shopee Media endpoints for image upload and chunked video upload workflows, including initialization, part upload, completion, result checking, and cancellation. It is intended for LinkFox-mediated Shopee store media operations after the related store-auth skill has selected a shop or merchant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Shopee store media operations through LinkFox using a configured API key.

Mitigation: Install and run it only when you trust LinkFox for the relevant Shopee store, and review the intended shop or merchant ID before upload or cancellation commands.

Risk: Onboarding helpers support phone-number login, API key generation, and payment-order creation.

Mitigation: Use onboarding and order commands only after explicit user intent to register, log in, retrieve an API key, or purchase credits.

Risk: LINKFOX_* URL environment variables can redirect requests away from the default LinkFox hosts.

Mitigation: Keep LINKFOX_* URL variables pointed only at trusted LinkFox endpoints before executing media or onboarding scripts.

Risk: Full API responses are saved locally and may include store, account, media, or transaction data.

Mitigation: Periodically review and delete local linkfox response files when they may contain sensitive information.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Media API reference](artifact/references/api.md)
- [Onboarding and billing reference](artifact/references/onboarding.md)
- [Shopee v2.media.upload_image documentation](https://open.shopee.com/documents/v2/v2.media.upload_image?module=130&type=1)
- [LinkFox skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to files or printed to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a linkfox session data directory; small responses can print inline, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
