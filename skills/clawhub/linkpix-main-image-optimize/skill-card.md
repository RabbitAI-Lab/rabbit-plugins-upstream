## Description:

Helps agents use LinkPix/qhkit to optimize ecommerce main product images by improving composition, lighting, texture, and visual detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketplace teams, and developers use this skill to guide an agent through LinkPix/qhkit image optimization workflows for refreshing product hero images and improving commercial presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes broad local setup actions, including package installation, Node installation, PATH changes, and shell-profile changes.

Mitigation: Require explicit user approval before installing packages, installing Node, changing PATH or shell profiles, or retrying setup with alternate registries.

Risk: The skill includes token configuration flows for qhkit access.

Mitigation: Prefer secure local configuration through QHKIT_TOKEN or qhkit config; avoid sending API keys in chat and confirm displayed configuration is redacted.

Risk: Image optimization can upload product images to the LinkPix/qhkit service.

Mitigation: Confirm the user intends to use LinkPix/qhkit and is authorized to upload the referenced product images before generation.

Risk: Generated image rewrites may change product details such as text, logos, materials, or structure.

Mitigation: Review generated outputs for product accuracy and brand-critical details before commercial use.

Risk: Generation can consume service credits.

Mitigation: Run an estimate when supported and obtain explicit user confirmation of model, size, image count, references, and expected credits before submitting a generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [iQingHu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide image generation after user confirmation; qhkit responses can include generated image URLs and credit usage.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
