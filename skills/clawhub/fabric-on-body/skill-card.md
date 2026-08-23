## Description:

This skill helps agents replace the fabric appearance of a garment reference with a target fabric swatch while preserving the original cut, construction, layout, and camera angle for visual sample previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel teams, fabric suppliers, and garment developers use this skill to preview how a fixed garment pattern may look in different fabrics before physical sampling or SKU expansion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment references, fabric swatches, prompts, and generated outputs are sent to dLazy cloud services for inference and storage.

Mitigation: Confirm authorization before uploading confidential designs, proprietary samples, customer imagery, or regulated data, and review dLazy terms and retention practices.

Risk: The workflow uses a dLazy API key for hosted image generation.

Mitigation: Use the pinned npx command when avoiding a persistent global install, and rotate or revoke the API key when it is no longer needed.

Risk: Generated sample images are visual previews and may not reflect real material hand feel, weight, or manufacturability.

Mitigation: Treat outputs as pre-sampling concept previews and confirm final fabric behavior through physical sampling or expert review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image file or URL outputs from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a garment reference image and fabric swatch as inputs; generated results are visual previews and not physical fabric or construction guarantees.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
