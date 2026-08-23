## Description:

基于一个印花快速生成多个设计版本，支持不同风格、颜色及元素组合，提高 POD 设计效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, POD shop operators, and commerce agents use this skill to turn one uploaded print pattern into multiple related design variations with changed colors, themes, elements, and layout density.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose qhkit API keys by pasting credentials into chat.

Mitigation: Configure credentials locally with QHKIT_TOKEN or another secure secret mechanism instead of sharing API keys in conversation.

Risk: Reference images submitted through qhkit may be uploaded to the qhkit service.

Mitigation: Review images for sensitive content before use and confirm that upload to the service is acceptable.

Risk: Image generation can consume service credits after a task is submitted.

Mitigation: Run an estimate when available and require explicit user confirmation of model, image count, inputs, and expected credits before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit image-generation commands that upload local images and consume service credits after user confirmation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
