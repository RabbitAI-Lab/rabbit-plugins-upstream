## Description:

Creates on-model apparel images from garment flat lays and pose references for e-commerce photography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to compose product photos showing a model wearing a garment or outfit while following a chosen pose and scene reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, reference, and optional face images are sent to a selected image-generation provider.

Mitigation: Review the request with --dry-run, explicitly select the provider, and upload personal likenesses or proprietary images only with appropriate rights and consent.

Risk: Generated apparel details or anatomy may differ from the source images.

Mitigation: Inspect colors, fabric texture, logos, fit, and anatomy before using images in product listings.

## Reference(s):

- [Flat Lay release on ClawHub](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider setup and image data flow](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown instructions and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally; an optional JSON response reports output paths and generation status.]

## Skill Version(s):

1.0.19 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
