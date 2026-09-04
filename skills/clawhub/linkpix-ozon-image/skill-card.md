## Description:

Helps Ozon and Ozon Global sellers generate platform-oriented product visuals, including white-background product images, Russian selling-point graphics, practical scene images, multi-product collages, detail-page images, and campaign posters through LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and marketplace operators use this skill to prepare Ozon product listings and promotional images with Russian-language copy, Ozon-oriented composition, and qhkit-driven image generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to provide an API key for a billable image-generation service.

Mitigation: Prefer setting QHKIT_TOKEN or running the local qhkit config command instead of pasting a long-lived key into chat; rotate or revoke keys shared unnecessarily.

Risk: Image-generation requests can consume user credits.

Mitigation: Use the estimate flow and obtain explicit user approval for key generation parameters before submitting billable image tasks.

Risk: Product images are sent to Qinghu/LinkPix services for generation.

Mitigation: Install and use the skill only when the publisher, qhkit package, and service handling of product images are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ozon-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to upload product images, query model options, estimate credits, and request user approval before billable generation.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
