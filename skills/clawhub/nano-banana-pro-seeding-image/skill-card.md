## Description:

This skill helps agents create continuous, platform-native lifestyle seeding image series with Nano Banana Pro through AI Hive while keeping people, products, spaces, and timelines consistent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and agent operators use this skill to plan and generate natural lifestyle product-seeding image sets for social commerce, UGC-style posts, carousels, and product diaries. It emphasizes continuity, approved reference materials, platform disclosure, and avoiding fabricated ratings, claims, screenshots, or user reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to AI Hive as a third-party service.

Mitigation: Use only prompts and images that are appropriate to share with AI Hive, and avoid private or sensitive references unless that matches the intended workflow.

Risk: The init flow stores an AI Hive API key in a local configuration file.

Mitigation: Protect the local configuration file, prefer environment variables in managed environments, and rotate the key if it may have been exposed.

Risk: Generated lifestyle imagery can imply real experience, endorsements, or product performance if used without disclosure.

Mitigation: Follow the skill's authenticity checks, disclose AI-generated or sponsored content where required, and avoid fabricated reviews, ratings, before-and-after effects, or unverifiable claims.

Risk: Security evidence notes unused generic client code as a hygiene risk.

Mitigation: Review the script before deployment and keep only the AI Hive image-generation paths needed for the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-seeding-image)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline bash commands and generated image files from the AI Hive workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit prompts, optional reference images, batch controls, routing parameters, and a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
