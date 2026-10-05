## Description:

Turns photos of worn clothing into clean, white-background product flat-lay images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product teams use the skill to make single-item flat-lay product images from model photos, street photos, or customer photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos and prompts are sent to the selected cloud image provider.

Mitigation: Send only images and prompts you are comfortable sharing with dLazy or the configured provider.

Risk: Covered or hidden garment details are inferred and may be inaccurate.

Mitigation: Review generated details against source images and manually check or correct occluded areas.

Risk: Edited product images could misrepresent another brand's products.

Mitigation: Do not remove another brand's identity to present its products as your own.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider and CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated JPEG or PNG flat-lay images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one selected item per image; covered details are inferred.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
