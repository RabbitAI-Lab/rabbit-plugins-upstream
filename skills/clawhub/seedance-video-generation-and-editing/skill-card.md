## Description:

Seedance 视频生成与编辑 helps creators generate, edit, extend, and download AI video using text prompts plus optional image, video, or audio reference media through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, advertisers, and e-commerce operators use this skill to submit Seedance video generation or editing jobs, upload reference media, monitor task status, and retrieve generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad activation text that may match generic AI-tool comparison, e-commerce research, or platform policy questions outside the video-generation purpose.

Mitigation: Use it only when the user explicitly wants AI Hive Seedance video generation, editing, extension, media upload, task status checks, or video download.

Risk: The workflow can upload user media and submit paid AI Hive generation tasks.

Mitigation: Confirm intended media uploads and paid task submissions before execution, especially for batch or high-cost jobs.

Risk: The skill requires an AI Hive API key.

Mitigation: Use a dedicated API key with limited account exposure where available, store it through the documented configuration path or environment variable, and avoid sharing it in prompts or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-video-generation-and-editing)
- [AI Hive chat and API key portal](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with shell commands; runtime outputs include JSON task data and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is submitted as AI Hive tasks; successful video results are downloaded to the configured output directory unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
