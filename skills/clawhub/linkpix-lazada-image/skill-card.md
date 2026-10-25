## Description:

Helps Lazada sellers create localized product image sets, detail-page graphics, and promotional posters using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Lazada sellers and e-commerce teams use the skill to create localized main images, product-detail graphics, and campaign visuals for Southeast Asian markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key requested in chat could be exposed.

Mitigation: Set QHKIT_TOKEN locally rather than sharing a key in chat.

Risk: Unpinned npm dependencies and image-compression tools may change unexpectedly.

Mitigation: Review and pin or preinstall trusted versions before use.

Risk: Product images and prompts are uploaded to the image-generation service, and generation spends credits.

Mitigation: Confirm the upload and estimated cost with the user before generating images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-lazada-image)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image links]

**Output Format:** [Markdown with command examples and generated-image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as URLs; generation consumes account credits.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
