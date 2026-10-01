## Description:

Creates images from text prompts or selectively edits reference images to change models, poses, and outfits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to generate scene imagery from descriptions or revise a reference image's model, pose, or styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to a configured cloud image-generation provider.

Mitigation: Avoid confidential photos and internal reference URLs; choose an explicit provider and account for sensitive work.

Risk: Image-generation requests may incur provider charges.

Mitigation: Use dry-run to review the request and estimated cost before generating images.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider setup and data flow](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Locally saved image files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference-image edits; image size, aspect ratio, and batch settings can be selected.]

## Skill Version(s):

1.0.15 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
