## Description:

Helps agents migrate Vidu-style video generation and editing workflows to AI Hive Seedance 2.5, with prompts and commands for multi-reference subjects, scene edits, continuity checks, and video extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to run AI Hive Seedance 2.5 video workflows that replace Vidu-style text-to-video, image-to-video, reference-video, editing, and extension tasks while preserving subject relationships and continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected prompts and media are sent to AI Hive for video generation.

Mitigation: Use only media that is authorized for upload, and avoid private or regulated files unless the user explicitly intends to process them with AI Hive.

Risk: The helper can store an AI Hive API key locally for reuse.

Mitigation: Use a dedicated AI Hive API key, keep the local config file protected, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/vidu-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, files]

**Output Format:** [Markdown guidance with bash commands, JSON task output, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key and may upload user-selected image, video, or audio media to AI Hive.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
