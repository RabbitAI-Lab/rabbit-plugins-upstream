## Description:

Extracts a clean e-commerce flat-lay product image from a clothing photo, removing the person, props, and background while preserving garment color, material, and shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, and content teams use this skill to turn model photos, buyer-show images, or competitor screenshots into clean clothing flat-lay assets for product listings and downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos and prompts may be sent to dLazy or another configured cloud image provider.

Mitigation: Use only approved images and prompts, and install the skill only when that provider data flow is acceptable.

Risk: The generator can fetch arbitrary image URLs before forwarding image data to the selected provider.

Mitigation: Prefer local image files, avoid private or internal URLs, and restrict network access for the agent process before running commands.

Risk: Occluded garment areas are inferred and may not exactly match the real product.

Mitigation: Manually review generated flat-lay images, especially occluded design details, before using them in product listings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [Example source photo](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-extraction/source-photo.jpg)
- [Example flat-lay output](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/clothing-extraction/example-output.jpg)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples; generated image files are saved when the commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default generated assets are square clothing flat-lay images, typically 1024x1024 JPEG or PNG files.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
