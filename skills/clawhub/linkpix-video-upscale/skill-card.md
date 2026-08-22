## Description:

AI 提升视频分辨率与画质，修复模糊、噪点及压缩痕迹，输出最高 4K/60fps。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare qhkit video-edit video_super_resolve jobs for video upscaling, denoising, compression-artifact cleanup, and 1080p/2K/4K output at 30 or 60 fps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/qhkit packages and therefore modify the host environment.

Mitigation: Review setup commands before execution and install only in environments where global package changes are acceptable.

Risk: The skill may reuse an existing OpenClaw qhkit token or request a qhkit API token.

Mitigation: Confirm credential use before setup or generation, and use scoped credentials where available.

Risk: Video generation may upload local media and consume account credits.

Mitigation: Require explicit user approval for upload, resolution, frame rate, and expected cost before submitting a paid generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline JSON and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit task submission, status polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
