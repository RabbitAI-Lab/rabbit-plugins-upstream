## Description:

Helps create social-media-style outfit images that preserve the clothing while changing the model, pose, setting, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use the skill to turn an outfit photo into lifestyle promotional images across different scenes while retaining the pictured garments and accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied clothing or model photos are sent to the selected cloud image provider.

Mitigation: Use only images you have permission to share, avoid sensitive personal photos without consent, and confirm the provider before generation.

Risk: Synthetic lifestyle images could be mistaken for a real person's endorsement or actual product experience.

Mitigation: Do not use the skill to impersonate a real person or fabricate endorsements or usage claims; review images before publishing.

Risk: Generated images can alter garment details or introduce visual defects.

Mitigation: Compare each output against the source outfit and inspect accessories, fit, and anatomy before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider and authentication guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Text guidance and commands; generated JPEG images saved to a chosen path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference images or scene descriptions and multiple image variants.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
