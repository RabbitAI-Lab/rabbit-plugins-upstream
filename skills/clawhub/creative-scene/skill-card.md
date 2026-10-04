## Description:

Creates images from scene descriptions and edits models, poses, or outfits using optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use this skill to draft scene images and adjust a model, pose, or outfit from a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to an external image provider.

Mitigation: Confirm the selected provider before use and avoid supplying private prompts or images unless intended.

Risk: Generation may incur unexpected usage charges or save images to an unintended location.

Mitigation: Use --dry-run to check routing and estimated cost, and review the output path before generating.

Risk: Photorealistic generated images could misrepresent a real person or product.

Mitigation: Review images before publication; do not use them to impersonate people or fabricate product photography or user experiences.

## Reference(s):

- [Creative Scene release](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Prompt guidance, Shell commands]

**Output Format:** [Image files or hosted image URLs, with Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image creation and reference-image edits; images can be saved locally.]

## Skill Version(s):

1.0.17 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
