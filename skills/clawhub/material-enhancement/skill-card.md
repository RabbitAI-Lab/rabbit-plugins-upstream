## Description:

Reconstructs garment fabric texture in a fashion image using a high-resolution product reference while aiming to preserve the composition and other visual details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External fashion and ecommerce teams use this skill to refine fabric texture in generated product imagery by pairing an on-model image with a high-resolution photo of the same garment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an undisclosed external image-processing workflow and incomplete inspection of some components, leaving uncertainty about how submitted images are handled.

Mitigation: Before installing or submitting images, review the external processing and package source; consider privacy implications for identifiable people and unreleased products.

## Reference(s):

- [Provider CLI guide](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Text prompts]

**Output Format:** [JPEG image file with Markdown instructions and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an on-model image and a high-resolution reference photo of the same garment to guide texture reconstruction.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
