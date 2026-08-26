## Description:

Processes one uploaded image to reduce AI-like artifacts, sharpen details, improve visual consistency, and return realistic high-definition image variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and image-production teams use this skill to make AI-generated or AI-styled non-portrait images look more realistic, detailed, and visually unified before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads the selected image to Qinghu for processing.

Mitigation: Confirm the exact image with the user and proceed only when they are comfortable uploading it to Qinghu.

Risk: Generate actions can consume paid Qinghu credits.

Mitigation: Run an estimate first, report the expected credit use, and wait for explicit user approval before submitting.

Risk: The skill depends on qhkit and may require Node package installation or upgrades.

Mitigation: Prefer official npm and Node sources, verify official Node SHA256 checksums when bootstrapping Node, and surface installation failures to the user.

Risk: Requests may overlap with other image-editing skills or workflows.

Mitigation: Confirm the selected Qinghu workflow, input image, and key parameters before any generate action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON CLI command examples and generated image URLs when the workflow completes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return multiple image variants; requires one user-selected image and Qinghu/qhkit credentials.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
