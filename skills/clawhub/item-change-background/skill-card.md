## Description:

Transforms white-background product images into photorealistic lifestyle scene images with matched lighting, grounded shadows, and environmental reflections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and developers use this skill to turn plain product photos into realistic commercial scene images. The skill helps preserve product shape, color, material, logo placement, and camera angle while replacing or compositing the background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts can fetch arbitrary image URLs before sending image content to a configured generation provider.

Mitigation: Use trusted local image files or known public image URLs, and avoid confidential product assets unless the selected provider is approved for that data.

Risk: Prompts, images, and provider credentials may be processed by cloud providers with weak scoping.

Mitigation: Use organization-approved providers, keep provider keys scoped and rotated where possible, and avoid entering credentials beyond the variables required for the chosen backend.

Risk: The ARK_BASE_URL setting can change the endpoint that receives requests.

Mitigation: Leave ARK_BASE_URL unset or set it only to a trusted endpoint controlled by the user or organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [model-flags.md](references/model-flags.md)
- [provider-cli.md](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [clothing-extraction related skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/clothing-extraction/skill.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, image files]

**Output Format:** [Markdown guidance with bash commands and optional JSON status; generated assets are saved as JPEG, PNG, or WebP files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one product image or a product image plus background image, provider selection through environment variables or flags, dry-run previews, and batch generation.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
