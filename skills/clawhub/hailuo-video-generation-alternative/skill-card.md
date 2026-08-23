## Description:

This skill helps agents migrate Hailuo, MiniMax, and similar narrative video-generation workflows to AI Hive Seedance 2.5 for text-to-video, image-to-video, reference-based generation, performance editing, and shot extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to guide an agent through AI Hive Seedance 2.5 video tasks that resemble Hailuo or MiniMax narrative workflows. It focuses prompts and commands around character motivation, single visible actions, emotional continuity, authorized references, performance edits, and shot extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected image, video, or audio files may be uploaded to AI Hive or storage URLs returned by AI Hive.

Mitigation: Use only media that the user is authorized to upload and avoid confidential or sensitive content unless AI Hive handling is approved.

Risk: The AI Hive API key may be stored locally in ~/.ai-hive/config.json.

Mitigation: Prefer environment or CLI-provided credentials when appropriate, restrict local config permissions, and rotate the key if it may have been exposed.

Risk: Generated video output may not preserve identity, clothing, timing, or continuity exactly across edits and extensions.

Mitigation: Review generated results frame by frame against the source material, verify continuity, and retain task IDs and authorization records for referenced assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/hailuo-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with inline bash commands and JSON task responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive video jobs, upload selected media, poll task status, and download generated video or last-frame files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
