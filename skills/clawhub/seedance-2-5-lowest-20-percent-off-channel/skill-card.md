## Description:

This skill helps agents use AI Hive as a Seedance 2.5 video-generation channel, submitting text-to-video, image-to-video, reference-to-video, video-editing, and video-extension jobs and then tracking and downloading results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, advertising and marketing teams, e-commerce teams, and short-form video production teams use this skill to generate or edit Seedance 2.5 videos from prompts and optional media references. It supports task submission, media upload, progress checks, and downloading generated video outputs through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be selected for broad competitor, pricing, API, or e-commerce content-production searches.

Mitigation: Use it only when the user explicitly wants AI Hive Seedance 2.5 video generation or editing, and review the intended task before invoking the script.

Risk: Using the skill requires an AI Hive API key that may be stored locally.

Mitigation: Use a dedicated API key, keep the local config file private, and revoke the key when it is no longer needed.

Risk: Reference images, videos, or audio are uploaded to AI Hive for generation.

Mitigation: Upload only media that the user is allowed to share with AI Hive and avoid sensitive, confidential, or restricted assets.

Risk: Video-generation requests may create paid third-party tasks.

Mitigation: Confirm the intended routing and price snapshot before submission, and avoid resubmitting timed-out tasks until the saved task ID has been checked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-lowest-20-percent-off-channel)
- [AI Hive chat and API access](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, JSON task responses, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include task IDs, task-status JSON, uploaded media IDs, and generated video files saved to the configured output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
