## Description:

帮助电商运营者和创意团队将场景图中的旧商品替换为新商品，同时尽量保留原场景、构图和光影。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and creative teams use this skill to plan product-swap image jobs from scene references and a new product image. It guides setup, cost estimation, confirmation before generation, and delivery review for generated product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may upload selected product and scene images to an external provider.

Mitigation: Review the image files and confirm they are appropriate to send before running generation.

Risk: Generation can spend account credits.

Mitigation: Run an estimate first and obtain explicit user approval before submitting a generate request.

Risk: Generated product images may alter product details such as logos, text, structure, perspective, or reflections.

Mitigation: Inspect outputs before use and verify key product details against the original product image.

Risk: Scene images from third parties may carry rights or reuse restrictions.

Mitigation: Confirm the user has permission to reuse reference scene assets for ecommerce material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [@iqinghu/qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include setup guidance, estimate and generate commands, confirmation prompts before spending credits, and delivery notes for generated image URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
