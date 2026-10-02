## Description:

Guides ecommerce teams in replacing the model, background, or both in an existing product photo while aiming to preserve the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce marketers and designers use this skill to make audience- and setting-specific versions of an existing model or mannequin photo without intentionally changing the clothing or other product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source and reference images, prompts, and related metadata may be sent to a cloud image provider.

Mitigation: Use dry-run first and send only images and prompts you are comfortable sharing with the selected provider.

Risk: Use of personal images or generated likenesses without appropriate rights or consent.

Mitigation: Use authorized images and obtain consent where needed; do not create deceptive endorsements of real people.

Risk: Generated images may alter garment details, anatomy, or lighting despite preservation instructions.

Mitigation: Review each image against the original product and reject outputs with incorrect details or artifacts.

Risk: Saving outputs to an unintended path may overwrite or misplace files.

Mitigation: Confirm the destination path before running a generation command.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text with image-editing prompts and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the suggested commands can produce cloud-generated image files; check product fidelity and image rights before use.]

## Skill Version(s):

1.0.15 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
