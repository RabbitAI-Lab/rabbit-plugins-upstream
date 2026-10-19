## Description:

Helps Amazon sellers and design teams create product main images, image sets, detail-page visuals, and promotional graphics with LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, cross-border commerce designers, and marketing teams use this skill to produce product listings, detail-page images, and promotional visuals tailored to their target storefront and language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI introduces software supply-chain exposure.

Mitigation: Review the package and installation steps before installing qhkit.

Risk: The service uses an API key and may upload product images.

Mitigation: Protect the API key and avoid submitting sensitive product images unnecessarily.

Risk: Image-generation requests spend credits and cannot be cancelled after submission.

Mitigation: Check the estimated credits and request explicit approval of the generation parameters before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-amazon-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Images, Text]

**Output Format:** [Generated image URLs with a brief completion message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual credits consumed for completed image generation.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
