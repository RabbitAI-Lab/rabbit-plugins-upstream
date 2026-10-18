## Description:

Helps cross-border sellers translate text in product images into other languages while aiming to preserve the original layout and visual style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border ecommerce sellers and content teams use this skill to create translated product listing images for multiple markets, including batches of main and detail images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to the LinkPix/iqinghu service for processing.

Mitigation: Avoid submitting sensitive images unless the service terms and data handling fit your needs.

Risk: The skill requires a qhkit installation and a service token.

Mitigation: Review global install and PATH changes, prefer a pinned package version where possible, and configure the token through the supported setup.

Risk: Generative redraws can alter translated text, prices, branding, or product details.

Mitigation: Inspect each generated image and verify spelling, numbers, logos, and product features before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key setup](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Image URLs, Guidance]

**Output Format:** [Markdown with links to translated images and usage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-image results and credits charged; translated text and product details require human review.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
