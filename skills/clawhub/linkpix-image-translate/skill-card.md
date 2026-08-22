## Description:

Translates text in ecommerce product images into target languages while preserving the original layout and design style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and agent operators use this skill to localize product images for cross-border storefronts, including main images and detail images, while keeping visual layout and style close to the source image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are uploaded to the Qinghu/LinkPix service during generation.

Mitigation: Confirm the user is comfortable with uploading the selected images before running generation.

Risk: Image generation consumes service credits.

Mitigation: Run an estimate first and obtain explicit approval for the model, language, image list, size, count, and estimated credit cost before submitting generation.

Risk: Generated image text or product details may be inaccurate because the workflow redraws images rather than performing pixel-level text replacement.

Mitigation: Require post-generation review of translations, spelling, prices, specifications, brand names, logos, and product structure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and generated image URLs when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit CLI access; generation consumes service credits after explicit user approval.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
