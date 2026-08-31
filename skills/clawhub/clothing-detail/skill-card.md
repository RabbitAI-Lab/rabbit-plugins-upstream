## Description:

Generates macro e-commerce detail shots from garment photos, focusing on fabric texture, stitching, weave structure, collars, cuffs, hems, buttons, zippers, embroidery, and prints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, creative operators, and agent workflows use this skill to turn regular garment photos into close-up detail images for product listing pages. It helps specify target garment areas, prompt constraints, provider options, and quality checks for realistic textile macro outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment photos, reference images, and prompts may be sent to the configured cloud image provider.

Mitigation: Use dry-run and provider controls to confirm the destination before execution, and avoid confidential designs or internal-only image URLs unless the provider is approved.

Risk: Low-resolution, compressed, or obstructed source images can lead to inaccurate or invented textile details.

Mitigation: Use clear source images above the documented resolution and size thresholds, focus on one visible garment area per run, and review outputs for fabricated construction details.

Risk: The bundled example brand profile can influence generated prompts if reused without changes.

Mitigation: Edit or replace the example brand profile before using brand controls in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy provider information](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with bash command examples, Node.js helper scripts, optional JSON command output, and saved JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run checks, provider selection, batch generation, and user-specified save paths.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
