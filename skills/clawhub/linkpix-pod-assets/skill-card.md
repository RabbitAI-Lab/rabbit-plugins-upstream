## Description:

This skill helps POD sellers generate product design assets with LinkPix and qhkit, including print extraction, design variations, product mockups, and listing-ready visual concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers and commerce operators use this skill to prepare print designs, generate variations, and create mockup-style product images for apparel, home goods, accessories, and other print-on-demand categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead users to share API keys in chat.

Mitigation: Configure qhkit tokens locally through the CLI or QHKIT_TOKEN environment variable, and do not paste secrets into chat.

Risk: The skill uses broad auto-triggering language around POD, mockups, and image generation.

Mitigation: Review the intended action before running commands, especially when generation would upload images or consume credits.

Risk: Reference images and generated POD assets may involve copyrighted, branded, or otherwise restricted artwork.

Mitigation: Use only artwork and brand elements for which the user has appropriate rights, and review outputs before commercial use.

Risk: The workflow can upload local reference images to an external service and run credit-consuming generation after confirmation.

Mitigation: Confirm source images, model settings, image counts, and estimated credits before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides qhkit image generation flows that can upload reference images, estimate or spend credits, and return generated image URLs.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
