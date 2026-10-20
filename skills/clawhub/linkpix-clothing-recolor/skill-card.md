## Description:

Helps agents create alternate clothing colors for e-commerce SKU images with LinkPix while aiming to preserve garment shape, texture, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and their agents use this skill to create color variations of an existing clothing photo for SKU listings without a separate photo shoot for every color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or update npm packages and Node without clear user confirmation.

Mitigation: Request approval before installation or upgrades, and pin versions where possible.

Risk: Source clothing images are uploaded to LinkPix/iqinghu for processing.

Mitigation: Confirm the user permits uploading the images before submitting them.

Risk: Setup may change qhkit tokens or site configuration.

Mitigation: Confirm the intended account and site before changes; keep API keys out of shared output.

Risk: Generative recoloring can alter logos, text, or garment construction.

Mitigation: Inspect each output against the source photo before using it in product listings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report actual credit usage and review generated garment details before publishing.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
