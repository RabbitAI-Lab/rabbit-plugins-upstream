## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）AI 提升视频分辨率与画质，修复模糊、噪点及压缩痕迹，输出最高 4K/60fps。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local or public videos to LinkPix through qhkit for AI video super-resolution, denoising, compression artifact repair, and 1080p, 2K, or 4K output at 30 or 60 fps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the qhkit CLI before use.

Mitigation: Review the npm package and installation source before installation, and prefer a controlled environment for execution.

Risk: Local videos or public URLs may be sent to the third-party qhkit/LinkPix service.

Mitigation: Do not process sensitive or proprietary videos unless the service terms, retention practices, and user consent are acceptable.

Risk: Stored qhkit or OpenClaw credentials may be used and processing may consume paid credits.

Mitigation: Confirm the active account, estimate or disclose credits where supported, and get user approval before submitting paid processing jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit video-edit generate and status calls, target resolution and fps selection, task polling, credit reporting, and returned video URL delivery.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
