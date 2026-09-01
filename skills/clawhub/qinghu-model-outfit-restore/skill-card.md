## Description:

Qinghu AI virtual try-on skill that uploads a model image and a garment image, then generates a high-consistency outfit replacement image while preserving pose, lighting, and clothing detail for ecommerce styling workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate product styling or virtual try-on images by submitting authorized model and clothing images through Qinghu AI. It is intended for one-outfit-at-a-time image generation where preserving pose, lighting, and garment detail matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-selected model and clothing images to the Qinghu service.

Mitigation: Use only self-owned or authorized imagery and disclose external upload before processing sensitive or commercial assets.

Risk: The workflow can spend Qinghu credits when a generation task is submitted.

Mitigation: Run an estimate first, present the expected credit cost and key parameters, and submit only after explicit user confirmation.

Risk: Oversized or incorrectly ordered images can cause failed or incorrect generations.

Mitigation: Validate image order, keep images within service limits or compress locally, and rely on live workflow options for current field names.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-outfit-restore)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Image URLs]

**Output Format:** [Markdown guidance with bash commands and JSON command inputs; final delivery includes generated image URLs when the Qinghu workflow completes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit CLI actions for options, estimate, generate, and status; command stdout is expected to be one-line JSON.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
