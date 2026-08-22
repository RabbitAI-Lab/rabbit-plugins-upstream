## Description:

Create and edit Instagram Shop product posts, carousel stories, Reels covers, Stories, creator seeding assets and cohesive social-commerce grids.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, and social-commerce teams use this skill to generate and edit Instagram Shop feed posts, carousel systems, Stories, Reels covers, creator seeding assets, and cohesive product grids from approved product references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and may store it in ~/.ai-hive/config.json on the local machine.

Mitigation: Use the AI_HIVE_API_KEY environment variable or restrict local config file access on shared systems, and rotate the key if exposure is suspected.

Risk: Selected product or reference files are uploaded to AI Hive for generation.

Mitigation: Upload only files that are approved for external processing, and avoid private non-image files or unlicensed product references.

Risk: Generated commerce imagery could accidentally imply fabricated platform UI, pricing, claims, engagement, endorsements, or availability.

Mitigation: Keep tags, prices, handles, stickers, claims, and platform UI in downstream design tools, then review final assets against current Instagram commerce and advertising rules before posting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/instagram-ins-ecommerce-image-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image file outputs from the AI Hive CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images, batch generation, live parameters, routing options, output directory selection, submit-only task mode, polling, and downloaded image results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
