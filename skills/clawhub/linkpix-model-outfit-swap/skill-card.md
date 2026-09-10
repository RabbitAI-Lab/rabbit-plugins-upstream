## Description:

Generates realistic model try-on images from garment photos, with options for different models, body types, poses, scenes, and market-localized styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agent users use this skill to create product display images by placing a garment onto a provided or described human model. It is intended for virtual try-on and catalog imagery workflows where users still review garment details before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade mutable third-party npm tooling that persists on the user's system.

Mitigation: Run it in an isolated environment with a reviewed, pinned qhkit version already installed, and require confirmation before package installation or upgrade.

Risk: The skill can upload user-provided images and spend LinkPix credits through qhkit.

Mitigation: Confirm service trust, image sensitivity, token scope, and estimated credit cost before generation.

Risk: Generated try-on images can slightly change product details such as text, logos, or garment structure.

Mitigation: Review generated images against the source garment before using them in listings or customer-facing material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to estimate credits, run qhkit image generation, and return generated image URLs with actual credit usage.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
