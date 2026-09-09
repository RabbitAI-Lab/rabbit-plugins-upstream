## Description:

青虎AI 模特换装高一致性还原：上传模特图与要替换的衣物图，一键完成精准换装，保持人物姿态与光影高度一致、衣物细节还原到位，适配电商穿搭快速出图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce content teams use this skill to apply an authorized clothing image to an authorized model image while preserving pose, lighting, and garment detail for product or outfit imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires installing and running a mutable third-party CLI.

Mitigation: Review before installing, prefer a pinned local qhkit installation when possible, and upgrade only when needed for the workflow command.

Risk: The workflow uploads model and clothing images to Qinghu for paid processing.

Mitigation: Use only authorized images and confirm upload intent, subscription or credit status, and estimated cost before running generate.

Risk: Service tokens may be exposed if placed directly in shell commands.

Mitigation: Avoid putting API tokens directly in shell commands; prefer the qhkit config store, environment variables, or an existing config file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON parameters, status JSON, and result image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit setup, cost estimation, submission, polling, and final delivery of generated image URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
