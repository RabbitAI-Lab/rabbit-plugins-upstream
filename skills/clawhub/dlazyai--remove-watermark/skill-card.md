## Description:

Removes text, watermarks, badges, and decorative overlays from images and reconstructs the obscured background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and commerce teams use the skill to prepare clean image inputs by removing unwanted promotional text and overlays from images they have the right to edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts are uploaded to dLazy or another configured cloud provider.

Mitigation: Confirm the selected provider and its credentials before sending sensitive images or prompts.

Risk: Removing watermarks or required markings can violate rights or misrepresent an image.

Mitigation: Only edit images you have the right to modify; do not remove others' copyright marks or legally required labels.

Risk: Reconstructed image regions can invent details or subtly change the scene.

Mitigation: Inspect edited areas and important product details; use a dedicated editor where pixel fidelity matters.

## Reference(s):

- [Provider CLI and data flow reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Guidance]

**Output Format:** [Edited JPEG, PNG, or WebP image with brief delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Obscured regions are reconstructed rather than pixel-perfect restorations; review the result before use.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
