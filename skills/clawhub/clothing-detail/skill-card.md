## Description:

Guides the creation of photorealistic close-ups of garment fabric, stitching, and construction details from clothing photos for product listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to plan and generate close-up garment detail images showing visible fabric textures and construction features for product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images and prompts are sent to the selected cloud image provider.

Mitigation: Use only images and prompts permitted by the provider's terms; avoid confidential designs, faces, and regulated imagery unless authorized.

Risk: Provider routing and image generation may incur unexpected costs.

Mitigation: Check routing with an explicit provider setting and use dry-run before a paid request.

Risk: Generated close-ups may depict textile details absent from the source photo.

Mitigation: Use a clear source image and compare generated color, stitching, and construction details with the original before publishing.

## Reference(s):

- [Clothing Detail skill release](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider setup and image data handling](artifact/references/provider-cli.md)
- [Image generation model options](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image-generation prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the suggested commands can save generated garment detail images; review visual fidelity before publication.]

## Skill Version(s):

1.0.24 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
