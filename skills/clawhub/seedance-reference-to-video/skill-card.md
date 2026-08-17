## Description:

Helps creators generate Seedance reference-to-video clips through AI Hive by using reference images, videos, or audio to constrain subjects, products, motion, camera movement, and style, then tracking tasks and downloading the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, and advertising or ecommerce teams use this skill to turn prompts plus reference media into Seedance video-generation jobs through AI Hive. It supports ad, product, social commerce, short drama, comic drama, and social media video workflows where the user expects media upload, task tracking, and downloaded results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because activation language is broader than a paid media-upload generation workflow.

Mitigation: Use it only for explicit AI Hive Seedance reference-to-video generation requests; keep broad comparison or market-search queries informational unless the user confirms execution.

Risk: Running the workflow uploads selected local images, videos, or audio to AI Hive/object storage.

Mitigation: Confirm the exact files and user intent before running upload or generation commands.

Risk: Generation can incur AI Hive charges.

Mitigation: Check runtime pricing and routing, and confirm expected volume or batch size before submitting jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-reference-to-video)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON task/status responses, and downloaded video files when the commands are executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; uploads selected local media to AI Hive/object storage; saves generated outputs locally, by default under ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
