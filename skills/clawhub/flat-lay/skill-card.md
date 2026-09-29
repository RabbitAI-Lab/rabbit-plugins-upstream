## Description:

Turns garment flat-lay and pose-reference images into on-model e-commerce photos using an image-generation provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to create on-model catalog imagery from garment photos and pose references, including coordinated outfits and repeatable model styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to the chosen image-generation provider.

Mitigation: Choose the provider deliberately, preview with dry-run, and only supply images you are comfortable uploading; exclude private photos, internal URLs, and unrelated local files.

Risk: Generated photos may alter garment details or model features.

Mitigation: Review color, texture, print placement, fit, face, and anatomy before using the results in a listing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Image model options](artifact/references/model-flags.md)
- [Provider setup and outputs](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and CLI examples; generated JPEG images when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single garments or outfits, pose references, optional fixed model images, and batch generation; review generated images for garment accuracy.]

## Skill Version(s):

1.0.14 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
