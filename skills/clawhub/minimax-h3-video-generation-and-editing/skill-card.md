## Description:

Minimax H3 视频生成与编辑 helps creators generate AI video from text or from image, video, and audio reference media through AI Hive, then track the task and download the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, advertising teams, ecommerce teams, and developers use this skill to submit Minimax H3 text-to-video and reference-guided video generation jobs through AI Hive. It is suited for ads, product videos, TVC concepts, social content, short drama, and workflows that need task tracking and automatic media download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to AI Hive for processing.

Mitigation: Use only media and prompts that the user is authorized to upload, and avoid confidential or regulated content unless the deployment has approved AI Hive for that data.

Risk: Video generation may incur API charges.

Mitigation: Confirm routing mode, estimated cost, and batch size before large or repeated submissions.

Risk: The AI Hive API key may be stored in a local configuration file.

Mitigation: Keep the local config file private, prefer environment or secret-managed credentials where appropriate, and rotate the key if exposure is suspected.

Risk: Generated media is downloaded to the chosen output folder.

Mitigation: Choose an output directory with appropriate access controls and review generated media before publication or distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/minimax-h3-video-generation-and-editing)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands; generated media is downloaded as video files when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, progress messages, pricing-related route information, and downloaded MP4/MOV files in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
