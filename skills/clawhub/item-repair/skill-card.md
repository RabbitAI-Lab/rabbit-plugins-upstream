## Description:

商品精修、去褶皱。随手拍的商品图 → 可直接上架的精修图。当用户说「精修」「去褶皱」「修图」「拍得不好看」「整理一下」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and image-editing agents use this skill to retouch product photos by reducing random wrinkles, improving layout and lighting, and cleaning backgrounds while preserving product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are uploaded to a cloud image provider, and paid generation jobs may incur charges.

Mitigation: Use only images permitted for cloud upload, choose the provider explicitly, and run --dry-run to review the inputs and estimated cost before submitting jobs.

## Reference(s):

- [Provider and cloud image workflow](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Related material enhancement skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; edited product images saved as image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image output format, dimensions, and quality are configurable; JPEG is the documented default.]

## Skill Version(s):

1.0.29 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
