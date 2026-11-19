## Description:

根据商品图片和经核实的卖点生成带中文文案排版的电商转化主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce content creators use this skill to turn a product image and verified product and promotion points into a Chinese-language listing hero image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and marketing text are sent to an external image service, and the security review is incomplete.

Mitigation: Before sending inputs, check which provider will receive them and review its data-handling terms; inspect the skill's required access and any unreviewed scripts.

## Reference(s):

- [Provider CLI guide](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [Related item-detail skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/item-detail/skill.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Text, Shell commands]

**Output Format:** [Square or portrait ecommerce image file with Chinese promotional text, plus a generation prompt and CLI command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 1:1 at 2K resolution; the skill also supports 3:4 layouts.]

## Skill Version(s):

1.0.34 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
