## Description:

AI 提升视频分辨率与画质，修复模糊、噪点及压缩痕迹，输出最高 4K/60fps。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit video super-resolution and repair jobs through qhkit when they need clearer 1080p, 2K, or 4K output at 30 or 60 fps. The workflow helps confirm target resolution and frame rate, configure qhkit, submit the job, poll status, and deliver the resulting video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload local videos to an external service.

Mitigation: Review source videos for sensitivity and use only approved media before submitting qhkit jobs.

Risk: The skill can consume account credits when generation jobs are submitted.

Mitigation: Require explicit user confirmation of parameters and estimated or actual billing before running generate actions.

Risk: The skill may install or upgrade qhkit globally and handle persistent API tokens.

Mitigation: Prefer preinstalled dependencies, scoped execution environments, and managed secrets instead of giving the agent raw keys or broad system modification permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return qhkit task identifiers, polling status, credit estimates or charges, and final video URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
