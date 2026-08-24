## Description:

Helps creators, marketing teams, e-commerce teams, and short-form video producers use AI Hive to submit Seedance video generation or editing jobs, upload optional media inputs, track task status, and download generated videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce operators, and production teams use this skill to generate, edit, extend, and manage Seedance video jobs through AI Hive without writing API code. It supports text-to-video, image-to-video, reference-to-video, video editing, video extension, media upload, task polling, and result download workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an AI Hive API key, so local credential exposure could allow unauthorized API use.

Mitigation: Use environment variables or the generated config file with restricted permissions, rotate keys if exposed, and avoid sharing command logs that contain secrets.

Risk: Selected images, videos, or audio files are uploaded to AI Hive or its object storage during generation workflows.

Mitigation: Review media inputs before upload and avoid submitting confidential or rights-restricted assets unless the user has permission to process them.

Risk: Generation jobs may incur charges and the advertised discount or current model price can change.

Mitigation: Check AI Hive pricing snapshots before large batches and use no-download task submission for small validation runs before scaling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-lowest-20-percent-off-channel)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown with inline bash commands, JSON task responses, and downloaded video files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive task IDs for asynchronous polling and saves generated media to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
