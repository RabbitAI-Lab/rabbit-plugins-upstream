## Description:

Translates text in ecommerce product images in batches while preserving the original layout and visual style for multilingual marketplace listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and supporting agents use this skill to localize product main and detail images into target languages while keeping layout and style consistent. It helps prepare multilingual listing assets and guides users to estimate paid generation before submitting jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid external CLI/API for image translation.

Mitigation: Run estimate first and require explicit user confirmation before any generation that may consume credits.

Risk: Provided product images are uploaded to an external service.

Mitigation: Avoid submitting sensitive images unless the user accepts that service exposure.

Risk: The workflow stores or uses a qhkit API token.

Mitigation: Configure the token only through qhkit or QHKIT_TOKEN and avoid exposing it in prompts, logs, or shared files.

Risk: Generated image text or product details may be inaccurate.

Mitigation: Review translated outputs for spelling, prices, specifications, brand names, logos, and product structure before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit image-batch estimate and generate command guidance; chargeable generation requires estimate and explicit user confirmation.]

## Skill Version(s):

0.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
