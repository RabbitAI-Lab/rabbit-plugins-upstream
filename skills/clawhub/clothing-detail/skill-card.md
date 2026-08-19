## Description:

Generates macro clothing detail images from a source garment image, focusing on visible areas such as collars, cuffs, hems, buttons, zippers, embroidery, prints, knit structures, and fabric fibers while preserving the original color, weave, and construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, merchandisers, and content teams use this skill to generate close-up detail images for product pages when they need macro views of visible garment construction, fabric texture, or finishing details. It supports SKU detail image production using a user-selected garment image, optional reference image, and prompt guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-selected garment images to dLazy for hosted image generation.

Mitigation: Use only images that are appropriate to share with dLazy and avoid confidential product imagery unless the account and data-handling requirements permit it.

Risk: The dLazy API key may be saved locally or supplied through an environment variable.

Mitigation: Store the key using the documented dLazy authentication flow, restrict local access to the user account, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Low-quality or obstructed input images can lead to inaccurate or invented garment details.

Mitigation: Use high-resolution source images where the target detail is visible, generate one detail area per prompt, and review outputs for color, texture, and construction fidelity before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy API Key Dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Example Input Image](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/clothing-detail/garment-flatlay.jpg)
- [Example Output Image](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/clothing-detail/example-output.jpg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call dLazy gpt-image-2, commonly saving generated JPEG image assets to a local path.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
