## Description:

Extracts clothing from person-worn, street-style, buyer-show, or competitor images and turns it into clean white-background e-commerce flat-lay product imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, merchandisers, and creative operators use this skill to convert available clothing photos into flat product images for listings or downstream product-image workflows. It is especially suited to cases where the source material includes a model, props, accessories, or background that should be removed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos and prompts may be sent to dLazy or another configured image provider.

Mitigation: Use only source photos approved for external processing, configure the intended provider deliberately, and avoid uploading sensitive or unauthorized images.

Risk: Occluded clothing areas are reconstructed by inference rather than directly recovered from the source image.

Mitigation: Review generated outputs before commercial use, especially when hands, bags, hair, or props cover critical garment details.

Risk: The workflow could be misused to remove branding or misrepresent another seller's product as original merchandise.

Mitigation: Use the skill only with appropriate rights and retain legitimate product branding or design provenance where required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [Example source image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-extraction/source-photo.jpg)
- [Example output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-extraction/example-output.jpg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with prompt templates, command examples, and generated image files saved by provider tooling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one flat-lay image per requested item; occluded garment areas may be inferred and should be reviewed.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
