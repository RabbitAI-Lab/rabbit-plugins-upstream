## Description:

青虎AI 双人爆款视频模仿：上传一条双人参考视频和人物图，精准同步两个人物的动作与神态并优化画面画质，产出双人带货视频，适配童装、直播带货等多种创作场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and commerce teams use this skill to generate two-person imitation videos from an authorized two-person reference video and optional character image. It is intended for scenarios such as duo product videos, parent-child scenes, partner appearances, and synchronized two-person motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install local CLI or image tooling.

Mitigation: Review the qhkit installation path and package source before installation, and install only in an environment where that tooling is permitted.

Risk: The workflow uploads user-provided media files to Qinghu AI.

Mitigation: Use only media that the user owns or is authorized to process, and avoid submitting sensitive, unauthorized, or minor-related content without the required consent.

Risk: Generation can spend Qinghu credits.

Mitigation: Run an estimate first and require explicit user approval of the quoted job before submitting a paid generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Qinghu media URLs after job completion; qhkit command responses are single-line JSON.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
