## Description:

Seedance 视频延长 helps creators upload an existing video to extend it forward or backward through AI Hive, then track the job and download the completed video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, advertising producers, and e-commerce teams use this skill to extend existing videos for ads, product showcases, social commerce, short drama, and social media content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selected private, client, or unreleased media to AI Hive for video extension.

Mitigation: Use it only when AI Hive is intended to receive the selected files, and review the media before submission.

Risk: The activation scope is broader than the sensitive media-upload purpose.

Mitigation: Confirm the user wants Seedance video extension before uploading media or submitting a generation task.

Risk: Automatic downloads can write generated result files to the local output directory.

Mitigation: Use --no-download or an explicit output directory when automatic local result files are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-video-extend)
- [AI Hive account and API key page](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples; generated jobs may produce downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided media and AI Hive credentials; submitted tasks return task IDs and may be polled later.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
