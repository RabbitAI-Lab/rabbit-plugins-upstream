## Description:

青虎AI 爆款视频模仿（男装）上传参考视频和模特参考图，将参考视频中的人物动作迁移到新形象上，用于生成男装带货短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agent operators use this skill to prepare Qinghu menswear action-transfer jobs from a reference video and a model image. It guides setup, estimation, user confirmation, submission, polling, and delivery for paid video-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may submit paid Qinghu generation jobs and spend credits.

Mitigation: Run an estimate first, present the relevant parameters and estimated credits, and wait for explicit user approval before generation.

Risk: The workflow may upload task-specific reference video and model image files to Qinghu.

Mitigation: Use only media the user owns or is authorized to process, and avoid submitting unintended local files.

Risk: The skill depends on an external qhkit CLI and Qinghu API token configuration.

Mitigation: Install qhkit from the documented package source, configure only the required token, and report configuration failures without retrying paid submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Qinghu workflow parameters, setup commands, estimate and polling instructions, status summaries, and generated media URLs when available.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
