## Description:

Enhances clothing texture in a product image using a high-resolution reference photo while aiming to preserve the original composition, color, and silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion commerce teams and image editors use this skill to refine visible fabric texture in generated or photographed product imagery with a reference photo of the same item.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product images may be sent to an external image provider, and the security scan reports incomplete analysis coverage.

Mitigation: Check which provider receives the images and prompts before use, avoid uploading sensitive images unless that transfer is acceptable, and review the skill content because the scan does not cover everything.

## Reference(s):

- [Provider and CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Prompts, Shell commands]

**Output Format:** [Enhanced image files (JPEG by default), with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original image and a high-resolution reference of the same product; enhancement targets surface texture and microdetail while aiming to preserve composition, color, and silhouette.]

## Skill Version(s):

1.0.29 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
