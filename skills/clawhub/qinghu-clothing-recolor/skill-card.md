## Description:

Generates alternate color versions of clothing product images while preserving garment shape, material texture, and lighting for SKU color-card production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to create recolored clothing variants and SKU color-card images from an existing product photo. It is intended for clothing recolor requests, alternate color versions, SKU palette images, and related product listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and upgrade guidance can install or update Node/npm tooling and execute mutable third-party package code.

Mitigation: Preinstall and pin a reviewed qhkit version where possible, review install and upgrade commands before execution, and avoid blindly running upgrade commands copied from CLI response messages.

Risk: Image inputs and paths may be uploaded to the external Qinghu AI service during generation.

Mitigation: Use only images and directories that are approved for external processing, and keep the QHKIT_TOKEN or configured API token scoped to this service.

Risk: Generated recolors may change product details such as text, logos, garment structure, or patterns.

Mitigation: Review generated images before publication and explicitly prompt the model to preserve logos, printed patterns, material texture, shape, and lighting when those details must remain unchanged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters; successful generation returns image URLs and credit usage from the qhkit CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu AI API token, and local or hosted clothing image inputs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
