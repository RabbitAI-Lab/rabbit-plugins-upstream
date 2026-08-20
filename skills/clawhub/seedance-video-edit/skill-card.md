## Description:

Seedance 视频编辑 helps video editors, post-production teams, advertisers, and creators edit existing videos through AI Hive by uploading source media, submitting a prompt, tracking the task, and downloading the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, advertisers, and e-commerce operators use this skill to edit or restyle existing video assets for ads, product videos, TVC, social commerce, short drama, and social media content. The agent can guide setup, upload selected media, submit AI Hive video-editing tasks, poll status, and download generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI Hive API key and can store it in a local configuration file.

Mitigation: Use a dedicated key with appropriate account controls, keep the local config file permission-restricted, and rotate the key if it is exposed.

Risk: Selected media files are uploaded to AI Hive for video-editing tasks.

Mitigation: Pass only explicit intended file paths, avoid unrelated private media, and confirm rights to upload and transform the source assets.

Risk: Broad competitor and platform wording may be mistaken for official integrations or compatibility.

Mitigation: Treat those names as discovery and migration search terms only; rely on the runtime publicModelId and model configuration for actual callable capability.

Risk: Video-generation tasks may incur cost, and retrying after a timeout could duplicate submissions.

Mitigation: Check runtime pricing and routing before large batches, preserve task IDs, and query existing tasks before resubmitting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-video-edit)
- [AI Hive API console](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated media files are downloaded when tasks complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key, uploads user-selected media to AI Hive, saves task IDs, polls task status, and defaults downloads to ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
