## Description:

Create and edit Shopify PDP videos, homepage hero loops, DTC product stories, collection clips, and paid-social adaptations using AI Hive video generation, reference, editing, extension, upload, and delivery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, Shopify operators, DTC marketers, and developers use this skill to plan and run product video generation or editing workflows for PDP demos, hero loops, collection clips, paid social variants, and email landing assets while preserving product facts and brand voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and may store it in a local configuration file.

Mitigation: Use a dedicated AI Hive key with appropriate account limits, keep the config file private, and rotate the key if it is exposed.

Risk: Selected product images, videos, or audio can be uploaded to AI Hive during generation, editing, upload, or reference workflows.

Mitigation: Upload only media that is approved for the intended channel and provider, and avoid sensitive or unlicensed assets.

Risk: Rendering channel variants can incur AI Hive usage charges.

Mitigation: Review current AI Hive pricing and routing choices before submitting batches or variants.

Risk: Generated ecommerce videos may introduce unsupported claims, prices, testimonials, certifications, warranties, or performance results.

Mitigation: Review outputs against approved product facts, brand claims, storefront constraints, and advertising requirements before publication.

Risk: The security review notes extra dormant generic client code beyond the stated Shopify video helper behavior.

Mitigation: Prefer the documented generate, task, upload, and init commands and review future changes before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/shopify-ecommerce-video-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, code]

**Output Format:** [Markdown guidance with inline bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive video tasks, upload user-selected media, poll task JSON, and download generated video files when executed with credentials.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
