## Description:

Guides agents in retouching product photos for catalog use by reducing incidental wrinkles, balancing lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and e-commerce content teams use this skill to prepare product photos for catalog listings, including straightening flat-lay garments, removing incidental wrinkles, and improving lighting and backgrounds without changing the product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and selected reference images may be sent to the configured cloud provider.

Mitigation: Confirm the provider with --doctor or --dry-run and share only images approved for that provider.

Risk: Generated edits may change product details or conceal defects.

Mitigation: Compare the output with the source and reject changes to structure, color, hardware, or visible defects.

Risk: Saving generated images to an unintended path can overwrite or misplace local files.

Mitigation: Choose an explicit, separate output path and review it before running --save.

## Reference(s):

- [ClawHub item-repair release](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands may save retouched product images locally.]

## Skill Version(s):

1.0.21 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
