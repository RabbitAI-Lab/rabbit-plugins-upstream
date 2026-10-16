## Description:

Guides agents in turning product photos into white-background ecommerce images, including batch processing through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and content teams use this skill to prepare single or batch product photos with clean white backgrounds for marketplace listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos are sent to the qhkit/iqinghu service for generation.

Mitigation: Obtain approval before submitting sensitive product images to the service.

Risk: Installing or upgrading the npm CLI introduces dependency and setup risks.

Mitigation: Review and pin the qhkit version where reproducibility matters; make shell startup changes only with the user's consent.

Risk: Generative editing can alter product lettering, logos, or physical details.

Mitigation: Check generated images against the originals before publishing; use a dedicated cutout tool if a true transparent background is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides delivery of generated white-background JPG/PNG image URLs and reports credits charged; does not produce transparent-background images.]

## Skill Version(s):

0.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
