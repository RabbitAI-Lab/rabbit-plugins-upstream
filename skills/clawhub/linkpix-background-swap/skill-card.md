## Description:

Helps an agent replace ecommerce product image backgrounds with LinkPix/qhkit while preserving the product subject and producing marketing scene variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn product photos, including white-background images, into styled marketing scene images through the qhkit image workflow. It is intended for ecommerce image editing tasks where the target background, model, image count, size, and expected credit use should be confirmed before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images are uploaded to the generation service.

Mitigation: Use only approved product images and confirm referenced files before running generation.

Risk: Generation actions consume credits.

Mitigation: Run an estimate where supported and obtain explicit user approval for model, image count, size, references, and estimated credits before submitting.

Risk: The workflow may install or upgrade the qhkit CLI globally.

Mitigation: Install in an approved environment and review permission or network failures before continuing.

Risk: Generated background replacement can slightly alter product details.

Mitigation: Review generated images for key product structure, text, and logo accuracy before using them commercially.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit command guidance for image generation, option lookup, estimate checks, and delivery of generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
