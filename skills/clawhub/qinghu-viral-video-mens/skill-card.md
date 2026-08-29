## Description:

青虎AI 爆款视频模仿（男装）上传参考视频和模特参考图，将参考视频中的动作迁移到新男装模特形象上，用于生成男装带货短视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare and run Qinghu qhkit commands for menswear viral-video imitation. It helps generate a new short commerce video by applying motion from an authorized reference video to a supplied male model image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected videos and images to Qinghu's qhkit service.

Mitigation: Use only intended, owned, or authorized media and confirm the exact files before generation.

Risk: Generation is a paid action that consumes Qinghu credits.

Mitigation: Run an estimate first, report the quoted credits, and wait for explicit user confirmation before submitting generation.

Risk: The skill may rely on an existing qhkit API key or prompt the user to configure one.

Mitigation: Use the local qhkit configuration or a user-provided token only for this service, and avoid exposing the token in generated responses.

Risk: Missing local dependencies may cause the agent to install Node/npm packages or image-compression tools.

Mitigation: Install only the named dependencies needed for qhkit or local media compression, and report concrete installation failures to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit workflow commands, generated media URLs, and a final credit-consumption line after successful paid generation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
