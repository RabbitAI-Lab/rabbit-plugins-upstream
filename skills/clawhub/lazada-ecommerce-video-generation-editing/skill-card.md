## Description:

Create and edit Lazada product listing videos, localized demonstrations, LazMall brand clips and campaign-ready seller assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, content operators, and agent users use this skill to create accurate Lazada product demonstration videos, localize them across markets, and prepare campaign-ready seller assets while preserving SKU, package, language, and claim accuracy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, videos, audio, prompts, and task metadata are sent to AI Hive.

Mitigation: Upload only files needed for the task and avoid private or sensitive media unless sharing with AI Hive is acceptable.

Risk: The skill stores or reads an AI Hive API key for authenticated requests.

Mitigation: Protect the local API key configuration, prefer environment-based secrets where appropriate, and avoid committing credential files.

Risk: Generated ecommerce videos can accidentally introduce unsupported claims, offers, badges, prices, warranties, ratings, or incorrect package details.

Mitigation: Review each market version against merchant-approved copy, SKU facts, package contents, and current Lazada marketplace requirements before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/lazada-ecommerce-video-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash commands; CLI task responses as JSON; generated media downloaded as video or image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, uploads selected media, polls generation tasks, and can skip downloads for submit-only workflows.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
