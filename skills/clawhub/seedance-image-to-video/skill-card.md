## Description:

Seedance 图生视频 helps creators and marketing, ecommerce, short-drama, and comic-drama teams turn a first-frame image plus an action prompt into an AI Hive video generation task that can be tracked and downloaded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, advertisers, ecommerce teams, and video production teams use this skill to submit Seedance image-to-video jobs through AI Hive from local media and prompts. It is intended for product videos, ads, TVC-style content, social media clips, short drama, and comic-drama production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation and search scope is broader than the actual Seedance image-to-video purpose.

Mitigation: Use the skill only for deliberate AI Hive Seedance image-to-video generation, not as a general competitor, ecommerce, pricing, or API research assistant.

Risk: The skill can upload selected local media to AI Hive for processing.

Mitigation: Do not upload private, customer, regulated, or otherwise sensitive media unless AI Hive processing is acceptable for that asset.

Risk: The skill uses an AI Hive API key from command-line input, environment variables, or ~/.ai-hive/config.json.

Mitigation: Keep the API key protected, preserve restrictive permissions on ~/.ai-hive/config.json, and rotate the key if it may have been exposed.

Risk: Video generation can incur costs, especially for repeated or batch submissions.

Mitigation: Review model pricing at submission time, confirm quantity before large runs, and keep task IDs to avoid duplicate paid submissions after local timeouts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-image-to-video)
- [AI Hive chat and API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files, JSON]

**Output Format:** [Markdown guidance with bash commands; CLI output includes JSON task data and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results are saved as MP4, MOV, or the format supported by the current model, with task IDs available for later polling.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
