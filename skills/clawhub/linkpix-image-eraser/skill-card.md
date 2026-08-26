## Description:

Helps an agent use qhkit/LinkPix to remove specified people, watermarks, text, or clutter from product images and generate a background-filled edited result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through image element removal for product photos, including model selection, image upload, cost estimation, confirmation, generation, and result delivery through qhkit/LinkPix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to the qhkit/LinkPix service for editing.

Mitigation: Install and use the skill only when the user is comfortable with that service and with uploading the selected images.

Risk: Watermark, text, or element removal can raise rights, ownership, or policy concerns.

Mitigation: Review removal requests for rights and policy concerns before generation.

Risk: Generation can consume paid credits and cannot be canceled after submission.

Mitigation: Confirm the model, image count, size, selected images, and estimated credits before running generation.

Risk: Generative inpainting may subtly alter product details, logos, or text.

Mitigation: Inspect the edited result and ask the user to verify critical product details before treating it as final.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit Service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a configured API token, live model and size option lookup, and explicit user confirmation before paid generation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
