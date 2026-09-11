## Description:

按文字描述生成商业级电商图片，并可使用参考图进行图生图或改图，支持智慧模型、图片5.0 Pro、图片5.0 Lite 和专图模式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate ecommerce product images, scene images, concept images, and reference-image-guided variations through Qinghu AI/qhkit when a user asks for text-to-image or image-to-image output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install or upgrade an unpinned global npm CLI that handles API tokens and uploaded images.

Mitigation: Use a pinned, reviewed qhkit version in an isolated environment, avoid admin privileges for global installs, and install only when the package is trusted.

Risk: Prompts, product images, reference images, and a QHKIT token may be sent to the Qinghu/qhkit service.

Mitigation: Confirm the user is comfortable sending those inputs to the service and provide the token only as narrowly as practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Image URLs]

**Output Format:** [Markdown with inline bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit cost returned by qhkit image generate.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
