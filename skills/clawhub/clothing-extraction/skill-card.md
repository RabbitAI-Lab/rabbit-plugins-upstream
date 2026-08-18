## Description:

Extracts clothing items from model, street, buyer, or competitor images and renders clean e-commerce flat-lay product images with people, props, and backgrounds removed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agents use this skill to convert worn-clothing or reference photos into clean flat-lay product assets. It is also used to prepare cleaner inputs for downstream flat-lay, 3D, or fabric-on-body workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are uploaded to dLazy hosted services for inference.

Mitigation: Use only images approved for cloud processing and avoid submitting sensitive, confidential, or unauthorized third-party content.

Risk: dLazy credentials may be saved locally by the CLI.

Mitigation: Protect local CLI configuration, prefer scoped credentials where available, and rotate or revoke API keys if exposure is suspected.

Risk: Occluded garment regions are inferred rather than directly recovered from the source photo.

Mitigation: Review generated flat-lay images before commercial use, especially when key design areas were blocked in the input.

Risk: The workflow can be misused to process competitor, buyer, or model photos without proper rights.

Mitigation: Confirm usage rights for all input images and do not use the skill to remove branding or misrepresent ownership of a product.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Related flat-lay skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Related to-3d skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/to-3d/skill.md)
- [Related fabric-on-body skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with bash commands and JSON response examples; generated image URLs or saved image files from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a single source image per run, high-quality image generation settings, and optional batch fan-out for alternate outputs.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
