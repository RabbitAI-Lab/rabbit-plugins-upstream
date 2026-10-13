## Description:

Guides an agent in extracting a single garment from a photo as a clean, white-background product flat-lay using a cloud image-generation provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, designers, and content creators use this skill to turn model photos, streetwear images, or product screenshots into isolated clothing flat-lays for listings or downstream creative work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted photos and prompts are shared with the selected cloud image provider.

Mitigation: Use images you have permission to upload and review the chosen provider's data handling before submitting sensitive photos.

Risk: An unexpected provider or API-key configuration can expose images to another service or incur charges.

Mitigation: Review the configured provider and credentials, then use a dry run before making a paid request.

Risk: Generated details hidden in the source photo are inferred and may be inaccurate.

Mitigation: Inspect the flat-lay against the source and manually verify any obscured design features.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider configuration and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image-generation prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save PNG or JPEG flat-lay images; visually check reconstructed garment details.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
