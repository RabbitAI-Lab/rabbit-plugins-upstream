## Description:

LinkPix helps agents generate ecommerce images from text prompts or optional reference images through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to create commercial product imagery, scene images, concept images, and prompt-guided image variations. It is intended for free-form text-to-image and reference-image workflows that are not covered by more specialized LinkPix editing skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced images may be sent to the LinkPix/Qinghu service.

Mitigation: Ask the user before submitting sensitive prompts or images, and avoid sending confidential product, customer, or unreleased campaign material unless approved.

Risk: Setup may involve npm installs, Node installation, upgrades, and API token configuration.

Mitigation: Require explicit approval before installation or token setup, prefer a scoped user-level install, and avoid placing secrets directly in shell commands or logs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit JSON command examples and generated image URLs when the CLI is run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requests use prompt text, optional uploaded image paths or URLs, model labels, size presets, and image counts; successful qhkit calls return image URLs and actual credits used.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
