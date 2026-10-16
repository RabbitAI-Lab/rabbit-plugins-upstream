## Description:

Retouches product photos for catalog use by reducing incidental wrinkles, correcting layout and lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and product-content teams use this skill to prepare cleaner listing photos from casual product shots, including flat-lay garments, without changing the item's design or hiding defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and image URLs may be sent to dLazy or the selected cloud provider.

Mitigation: Use local image paths or trusted URLs and send material only if its cloud processing is acceptable.

Risk: Automated retouching can alter garment structure or conceal damage and misrepresent a product.

Mitigation: Confirm ambiguous editing requests and compare the result with the original, preserving structural folds, design details, and visible defects.

## Reference(s):

- [ClawHub item-repair release](https://clawhub.ai/dlazyai/skills/item-repair)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown instructions and locally saved JPEG, PNG, or WebP images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one to four views of the same product; review edited images against the originals.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
