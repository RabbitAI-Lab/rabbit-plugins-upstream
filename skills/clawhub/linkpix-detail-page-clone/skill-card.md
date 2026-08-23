## Description:

智能分析优秀商品详情页设计，用你的商品快速生成同类型布局及视觉风格的详情图，提高详情页制作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill with an agent to analyze a reference product detail page and generate product-detail images with a similar layout and visual style for their own product assets and copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if pasted directly into chat.

Mitigation: Configure qhkit tokens through a local secret or environment variable flow, and avoid sending the token in chat.

Risk: The skill may ask the agent to install or upgrade qhkit, Node, Pillow, or sharp-cli locally.

Mitigation: Require user review and approval before running package installation, curl, npm, or image-processing setup commands.

Risk: Image generation can consume account credits.

Mitigation: Use estimate or clearly disclose that actual charges apply, then wait for explicit user approval before running credit-consuming generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs or local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit configuration and user approval before credit-consuming image generation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
