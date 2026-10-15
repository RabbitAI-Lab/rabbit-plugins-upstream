## Description:

Turns a photo of a worn garment into a clean, white-background flat-lay product image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use this skill to make individual flat-lay garment images from model photos, street-style images, or buyer photos for product listings and related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected photos and prompts are sent to the configured cloud image provider.

Mitigation: Use only photos approved for that provider and check its account terms; verify the installed CLI or API credentials before running generation commands.

Risk: Occluded garment features may be reconstructed inaccurately.

Mitigation: Compare generated images with the source and manually review obscured design details before use.

## Reference(s):

- [Clothing Extraction on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and PNG or JPEG flat-lay images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One image per selected item; obscured garment details are inferred.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
