## Description:

Generates multiple e-commerce product-image variations with different backgrounds, layouts, or marketing styles from a supplied image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and online sellers use this skill to create product-image variants for ad campaigns and A/B testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install Node or qhkit and change local tool or shell configuration.

Mitigation: Get explicit approval before installation, token setup, site changes, or persistent PATH updates; review existing qhkit settings first.

Risk: Product images are uploaded to the LinkPix/IQingHu service for generation.

Mitigation: Only submit images the user is comfortable sharing with that service.

Risk: The suggested domestic-site configuration can overwrite an existing international AutoAGC setup.

Mitigation: Check the selected site and obtain the user's approval before replacing tokens or site settings.

Risk: Generated variants may change product structure, text, or logos.

Mitigation: Review each image for product accuracy and brand consistency before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Image links, Shell commands, Guidance]

**Output Format:** [Markdown with generated-image URLs and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generative redraws; verify product details, text, and logos before use.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
