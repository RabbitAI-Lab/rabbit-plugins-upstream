## Description:

LinkPix Ecom Image helps an agent route ecommerce product-image requests to qhkit modes for product image sets, detail-page images, and custom text- or reference-image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agents use this skill to turn product-image requests into the correct qhkit workflow for marketplace main images, carousel image sets, detail-page images, and commercial scene images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill asks users to paste an API key into chat.

Mitigation: Configure QHKIT_TOKEN or qhkit config locally through a secure channel instead of pasting API keys into chat.

Risk: The skill can upload product reference images to the qhkit/LinkPix service.

Mitigation: Install and use the skill only when the user is comfortable sending the selected product images to that service.

Risk: Generation tasks can consume credits.

Mitigation: Confirm the model, image count, quality, references, and qhkit estimate before submitting a generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with qhkit command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit image-generation tasks through qhkit, upload product reference images, and return generated image URLs with credit usage.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
