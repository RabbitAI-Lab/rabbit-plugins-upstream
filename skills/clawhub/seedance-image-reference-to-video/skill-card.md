## Description:

Seedance 参考图生视频 helps creators generate reference-image video through AI Hive by uploading source media, submitting a Seedance r2v task, polling status, and downloading the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, and advertising or e-commerce production teams use this skill to turn reference images and prompts into Seedance video generation jobs, then track and download the resulting media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends referenced media to AI Hive for video generation.

Mitigation: Use it only for media you intend to upload to AI Hive, and avoid submitting sensitive personal, commercial, or copyrighted content without appropriate rights and approval.

Risk: API keys may be exposed if pasted into command lines, transcripts, or shared logs.

Mitigation: Prefer environment variables or the local config file, keep configuration permissions restricted, and avoid sharing logs that contain credentials.

Risk: The security summary flags broad activation and privacy guidance for a credentialed media-upload workflow.

Mitigation: Review the skill before installing or running it, and confirm the requested task actually requires AI Hive video generation with the provided media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-image-reference-to-video)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API key portal](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; runtime commands can print JSON task status and download media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are downloaded to ~/Downloads/AiHive by default; --no-download prints task data without downloading results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
