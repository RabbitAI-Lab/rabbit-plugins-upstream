## Description:

Turns garment flat-lay photos and pose references into on-model e-commerce images while aiming to preserve the garment's appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and merchants use this skill to turn garment photos and pose references into model-worn product images, including single garments or coordinated outfits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos, model references, and prompts are sent to the configured cloud provider.

Mitigation: Avoid sensitive private images and untrusted internal image URLs; confirm the selected provider before uploading.

Risk: Image-generation calls may consume paid credits and require API credentials.

Mitigation: Use dry-run to inspect requests and estimated cost; use scoped, revocable API keys.

Risk: Generated images may alter garment details or produce inaccurate anatomy.

Mitigation: Review color, fabric texture, fit, logos, and anatomy before publishing.

## Reference(s):

- [Flat Lay skill listing](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Model flags](references/model-flags.md)
- [Provider setup and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text instructions and locally saved generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image quality and garment fidelity require visual review.]

## Skill Version(s):

1.0.17 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
