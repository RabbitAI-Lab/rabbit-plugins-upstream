## Description:

AI 提升视频分辨率与画质，修复模糊、噪点及压缩痕迹，输出最高 4K/60fps。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to upscale or repair user-selected videos through LinkPix/qhkit when the requested output is 1080p, 2K, or 4K at 30 or 60 fps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are uploaded to LinkPix/qhkit for cloud processing.

Mitigation: Use the skill only for videos approved for external cloud processing, and avoid submitting sensitive or restricted media.

Risk: Generate actions may consume credits and submitted tasks cannot be canceled.

Mitigation: Review the estimate, target resolution, frame rate, source videos, and other parameters before approving generation.

Risk: The skill requires an API key for qhkit.

Mitigation: Provide keys only through the documented qhkit configuration flow or environment variable and avoid exposing tokens in shared logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API Key Tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit installation, token configuration, estimate or status checks, video upscaling submission, polling, and final video URL delivery.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
