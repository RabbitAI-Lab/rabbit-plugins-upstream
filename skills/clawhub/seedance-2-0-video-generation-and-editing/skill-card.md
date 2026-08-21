## Description:

Seedance2.0 视频生成与编辑 helps video editors, post-production teams, advertisers, e-commerce teams, and creators generate or re-create deliverable video from text prompts and optional image, video, or audio reference media through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, advertisers, and e-commerce operators use this skill to submit Seedance2.0 text-to-video, image-to-video, and reference-to-video jobs, track task status, and download generated videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to AI Hive during upload or generation.

Mitigation: Use only media and prompts intended for upload to AI Hive, and avoid sensitive local files unless upload is deliberate.

Risk: The skill stores an AI Hive API key locally when initialized.

Mitigation: Use the documented environment variable or the local config file with restrictive permissions, and rotate the key if it may have been exposed.

Risk: Submitted generation jobs may incur API charges.

Mitigation: Review routing, model, quantity, and real-time pricing before batch or high-cost generation runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-0-video-generation-and-editing)
- [AI Hive chat and API access](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can submit generation tasks, print JSON task responses, upload selected media, and download generated video files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
