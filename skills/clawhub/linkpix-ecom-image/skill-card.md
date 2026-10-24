## Description:

Guides agents to create ecommerce product image sets, detail-page graphics, and promotional images from text prompts or reference images using LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, marketers, and their agents use this skill to select a LinkPix image-generation mode and create ecommerce listing images, detail-page graphics, or promotional visuals from product photos or descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or reference images are uploaded to the qhkit service.

Mitigation: Only submit images approved for upload to the external service.

Risk: Image generation can consume paid service credits.

Mitigation: Estimate credit usage with the same parameters before generation and confirm the spend.

Risk: Setup may install or update an external CLI and requires an API token.

Mitigation: Review or pin the package version before installation, protect the token, and avoid permanent PATH changes unless intended.

## Reference(s):

- [LinkPix skill release on ClawHub](https://clawhub.ai/autoagc/skills/linkpix-ecom-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may use product or reference images and paid service credits.]

## Skill Version(s):

0.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
