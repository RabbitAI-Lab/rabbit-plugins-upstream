## Description:

Extracts a single garment or accessory from a photo into a clean, white-background product flat-lay image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use the skill to turn modeled or lifestyle product photos into isolated flat-lay images for listings or subsequent image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Photos and prompts sent to an image-generation provider may include sensitive model or buyer images.

Mitigation: Use only images you have rights to process and share with the configured provider.

Risk: Generated flat-lays may infer or alter obscured garment details.

Mitigation: Review the output against the source, especially occluded design features, before publication.

Risk: Removing branding or repurposing a competitor's photo could misrepresent a product.

Mitigation: Do not remove another seller's branding or present their product as your own.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider and CLI guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [PNG or JPEG flat-lay images with Markdown instructions and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one selected item per image; obscured garment details may be inferred.]

## Skill Version(s):

1.0.16 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
