## Description:

Helps apparel sellers generate model try-on images from garment photos, with optional reference models and customizable appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel sellers and their agents use this skill to turn garment photos into product-display images showing a model wearing the item, optionally using a supplied model photo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment and model photos are uploaded to the qhkit/LinkPix service, which requires an API token.

Mitigation: Confirm the user accepts the service and image uploads before use, and protect the API token.

Risk: Dependency installation or environment setup can change Node or PATH configuration.

Mitigation: Prefer a vetted qhkit installation and explicitly approve Node or PATH changes before setup.

Risk: Generated images may alter garment text, logos, or structural details.

Mitigation: Review key product details against the original photos before using the images commercially.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown guidance and JSON image-generation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image URLs and credits used; review garment details before publishing.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
