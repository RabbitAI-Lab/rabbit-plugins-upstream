## Description:

一键替换图片中的商品主体，自动保留场景、构图及光影效果，大幅提升商品素材复用效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent operators use this skill to replace a product in an existing e-commerce scene image with a new product while preserving scene composition, perspective, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade a global npm CLI that persists after the immediate task.

Mitigation: Preinstall and review a pinned qhkit version where possible, and avoid automatic @latest upgrades unless the environment owner approves them.

Risk: Selected product or scene images are sent to Qinghu's service for generation.

Mitigation: Use the skill only with images that are approved for third-party processing and avoid submitting sensitive or restricted assets.

Risk: A qhkit API token is required for image generation.

Mitigation: Use a scoped token with only the needed image-generation access and avoid embedding credentials in prompts, files, or logs.

Risk: Generated product swaps may alter product details, text, logos, proportions, perspective, or reflections.

Mitigation: Review outputs before publication, especially brand marks, text, product structure, scale, shadows, and reflections.

Risk: Reusing scene imagery from another party may create copyright or rights-clearance issues.

Mitigation: Confirm that source scene images are licensed or authorized for reuse before generating replacement product assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-product-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs and credit-usage details through qhkit after a successful image generation request.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
