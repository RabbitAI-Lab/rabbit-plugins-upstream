## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 → 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce image creators use this skill to rebuild visible fabric texture in an apparel photo using a high-resolution photo of the same item. It guides the image edit to preserve the source composition, garment shape, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input photos may be sent to an external image service, and the security scan reports that some files were only partially inspected.

Mitigation: Before use, check which provider receives the photos and what data is sent; avoid photos you cannot share with that service, and review the components left partially analyzed.

## Reference(s):

- [Provider and data-flow guide](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)
- [Related fabric-on-body skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG, PNG, or WebP image files; shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a text prompt and reference photos; image dimensions, format, provider, and batch size are configurable.]

## Skill Version(s):

1.0.30 (source: release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
