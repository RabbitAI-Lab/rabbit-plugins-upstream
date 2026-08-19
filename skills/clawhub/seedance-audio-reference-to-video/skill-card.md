## Description:

Seedance 参考音频生视频 helps editors, post-production teams, advertisers, and creators generate video from reference audio through AI Hive, with media upload, task tracking, and result download handled by the skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, advertisers, and e-commerce marketers use this skill to submit audio-referenced Seedance video generation jobs through AI Hive and retrieve finished video assets. It is best suited for ad, product, social-commerce, short-drama, comic-drama, and social media video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation language can route tool-comparison, shopping-platform, or marketing-advice requests into a credentialed media-upload workflow.

Mitigation: Treat broad comparison or marketing-advice requests as informational and only generate video after the user explicitly asks to use AI Hive Seedance generation.

Risk: The skill requires an AI Hive API key and can upload selected media to AI Hive.

Mitigation: Use it only when comfortable providing an AI Hive API key and uploading the chosen media files to the service.

Risk: Submitting generation jobs may incur costs.

Mitigation: Confirm intent, routing, media inputs, and likely cost before running large or batch generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-audio-reference-to-video)
- [AI Hive access page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, API calls, Guidance]

**Output Format:** [Markdown guidance with CLI commands; generated media is saved as MP4, MOV, or another model-supported video format.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; may upload selected media, submit paid generation jobs, poll task status, and download results to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
