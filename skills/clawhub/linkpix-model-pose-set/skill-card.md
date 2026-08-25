## Description:

根据一张服装模特图自动生成多种姿势及展示角度的套图，丰富商品展示效果，适用于服装详情页及社交媒体营销。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce, marketing, and creative-production users use this skill to turn one clothing model image into a set of pose and angle variants for product detail pages and social media assets. Agents use it to prepare qhkit image-batch estimate and generate commands, confirm paid generation parameters, and deliver resulting image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run local qhkit tooling.

Mitigation: Install only when the qhkit provider is trusted, and review install commands before allowing them to run.

Risk: The skill may handle a LinkPix/Qinghu API token.

Mitigation: Use a platform-managed secret store or enter credentials outside chat where possible.

Risk: Generated pose-set images may differ slightly from the source model, garment, text, logos, or product structure.

Mitigation: Review generated images for important visual details before publishing or using them commercially.

Risk: Generation consumes credits and can create paid tasks.

Mitigation: Run estimate first and require explicit user approval before submitting generate commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu homepage](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses and generated image URLs after user-approved paid generation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
