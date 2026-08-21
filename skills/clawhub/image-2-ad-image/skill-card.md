## Description:

This skill helps performance marketers and ecommerce teams use AI Hive GPT Image 2 to generate single-variable, attributable ad image test cells while locking product facts, audience, placement, landing-page promises, and invariants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External performance marketers and ecommerce teams use this skill to create control and variant advertising image cells for A/B creative testing across platforms such as Meta Ads, Google Display, Amazon Ads, TikTok Ads, 巨量千川, and 小红书聚光. It supports prompt preview, AI Hive image generation, task status checks, and downloaded result files while requiring users to keep product claims, offers, landing-page messages, and platform policy review aligned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images provided with --product-source are uploaded to AI Hive.

Mitigation: Use brief mode to preview and validate prompts without upload, and only provide product images that are authorized to be sent to AI Hive.

Risk: The auth command stores an AI Hive API key locally.

Mitigation: Use a scoped API key where possible and protect the local AI Hive configuration file; the script sets restrictive file permissions when saving the key.

Risk: Generated ad images or prompts may contain claims, offers, or platform-specific presentation that require current advertising policy review.

Mitigation: Keep claims and offers tied to approved sources, preserve the landing-page message, and review final creative against the active rules of the target ad platform before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/image-2-ad-image)
- [AI Hive API](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [CLI output, generated prompt text, JSON task status, and downloaded PNG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses batchSize=1 for each ad test cell and can run in brief mode to preview the prompt without uploading product images.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
