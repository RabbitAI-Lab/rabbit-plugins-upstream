## Description:

Seedance 2.0 视频生成 helps creators, marketing teams, e-commerce teams, and short-form production teams generate videos from text prompts or reference media through AI Hive, then track tasks and download finished outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, advertising and marketing teams, e-commerce operators, and production teams use this skill to submit Seedance 2.0 text-to-video, image-to-video, reference-to-video, video-to-video, and audio-to-video jobs through AI Hive. The skill is intended for generating ads, product videos, social content, short drama, comic drama, and related AIGC video assets while handling media upload, task polling, and download steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to the AI Hive service for generation.

Mitigation: Use this skill only for media and prompts that are approved for AI Hive processing, especially when working with customer, personal, unreleased, or sensitive product material.

Risk: The skill stores or reads an AI Hive API key from local configuration, environment variables, or command-line input.

Mitigation: Prefer environment or per-user configuration, keep the local config file restricted to the current user, and rotate the key if it is exposed.

Risk: The bundled API helper is broader than a Seedance-only video workflow and can query models, upload media, and call other AI Hive endpoints.

Mitigation: Review the script before installation and use the documented Seedance generation commands and fixed publicModelId mappings for normal operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-0)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, files]

**Output Format:** [Markdown guidance with bash commands, JSON status output, and downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally by default under ~/Downloads/AiHive; task status can also be returned as JSON when download is skipped.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
