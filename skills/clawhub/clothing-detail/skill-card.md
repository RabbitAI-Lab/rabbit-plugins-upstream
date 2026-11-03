## Description:

Creates macro close-up images of garment details, emphasizing visible fabric texture, stitching, and weave for e-commerce pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and content teams use the skill to create close-up product images of garment features such as collars, cuffs, seams, and fabric texture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment images are sent to the chosen cloud provider for generation.

Mitigation: Choose the provider explicitly and upload only images you are permitted to share with it.

Risk: Fine details may be inaccurate when the source is low-resolution or the target feature is obscured.

Mitigation: Use a clear, high-resolution source and compare each generated detail against the original.

Risk: Batch image generation can incur metered costs.

Mitigation: Use dry-run to review the selected inputs and estimated cost before generating.

## Reference(s):

- [Provider CLI guide](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG image files and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a selected garment detail per image; aspect ratio, provider, and output path can be chosen.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
