## Description:

Helps turn a photo of clothing into a clean, centered e-commerce flat-lay image on a white background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-content teams use this skill to create catalog images from model photos, customer photos, or street photography. They select a garment and generate a centered flat-lay image for product listings or downstream image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release suspicious because source photos and prompts may be sent to external image services without a clear user warning.

Mitigation: Tell users which provider will receive the images and prompts, obtain consent before upload, and avoid sending sensitive photos.

Risk: Some script contents were only partially analyzed, so the skill's broader generation behavior has not been fully assessed.

Mitigation: Review the scripts and provider settings before installation, and confirm that their capabilities and tool access are appropriate for the intended use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Model flags reference](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files, Shell commands]

**Output Format:** [JPEG or PNG image files, with optional shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated flat-lay images use a square 1024×1024 canvas by default; occluded garment details may be inferred.]

## Skill Version(s):

1.0.31 (source: frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
