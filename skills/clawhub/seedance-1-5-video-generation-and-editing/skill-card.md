## Description:

Seedance1.5 视频生成与编辑 helps creators generate or edit videos from text prompts and optional image, video, or audio references through AI Hive, then track tasks and download finished media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, and advertising or e-commerce producers use this skill to create Seedance 1.5 video assets from text and reference media without writing API code. It supports text-to-video, image-to-video, reference-to-video, video editing, task lookup, media upload, and download workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation scope is broad for a skill that uploads local media and can use paid API credits.

Mitigation: Review the skill before installation, use explicit commands with known file paths and output directories, and confirm paid jobs before submitting.

Risk: Prompts and selected media may be sent to AI Hive or its upload storage.

Mitigation: Use the skill only with media you intend to upload, and avoid private product footage or customer assets unless that transfer is approved.

Risk: A local timeout may not mean the remote generation task failed, which can lead to duplicate paid submissions.

Mitigation: Keep the returned taskId and query the existing task before retrying a generation request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/seedance-1-5-video-generation-and-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials, may upload selected local media, and saves completed videos to the configured output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
