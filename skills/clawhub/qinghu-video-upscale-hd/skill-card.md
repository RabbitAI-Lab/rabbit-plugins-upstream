## Description:

青虎AI 商品视频画质超清提升：一键完成视频高清放大与智能补帧，兼顾画质提升与音画同步，让模糊、低码率的商品视频重新变清晰流畅。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upscale, sharpen, and interpolate frames for short product or legacy videos through Qinghu AI. It guides qhkit setup, estimation, user approval, workflow submission, polling, and delivery of the completed video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses an external Qinghu service and uploads the user-provided video.

Mitigation: Confirm the user owns or is authorized to process the video, and upload only the intended file or URL.

Risk: The workflow can consume Qinghu credits after submission.

Mitigation: Run an estimate first, disclose the quoted credit impact, and wait for explicit user approval before running generate.

Risk: The skill may install qhkit and Node tooling in the execution environment.

Mitigation: Use the documented npm package and checksum-verified Node installation path, and surface installation or network errors to the user.

Risk: Inputs longer than the supported video duration may fail or need preprocessing.

Mitigation: Check that the source video is 60 seconds or shorter, or ask the user to trim it before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit log IDs, generated video URLs, status messages, and final Qinghu credit usage.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
