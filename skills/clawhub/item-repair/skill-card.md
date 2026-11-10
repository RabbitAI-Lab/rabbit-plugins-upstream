## Description:

精修商品照片以减少随机褶皱、改善摆放与光照，并净化背景，让图片适合商品目录展示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product photographers use this skill to prepare single-product photos for catalog listings by refining random wrinkles, layout, lighting, and backgrounds while aiming to preserve intended product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is suspicious with medium confidence and says inspection was partial, so it does not establish that all files are safe.

Mitigation: Review the package and remaining files before installing or running it; consider the suspicious verdict before use.

Risk: Product images may be sent to external image-processing services, and the security guidance says disclosure and authorization may be unclear.

Mitigation: Confirm that external processing is permitted, disclose the transfer, and avoid sending sensitive or unauthorized images.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [Related skill: Material Enhancement](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Retouched product images (JPEG by default), with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts 1–4 views of one product; compare edited images with the originals to check product details and defects.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
