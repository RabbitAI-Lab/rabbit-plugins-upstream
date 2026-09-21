## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。当用户说「主图」「加卖点文案」「转化图」「促销图」「主图文案」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agent developers use this skill to turn a product image and concise selling points into prompt guidance and commands for generating a single Chinese marketplace hero image with readable promotional copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and supplied image URLs may be sent to the selected cloud generation provider.

Mitigation: Use dry-run and explicit provider selection where appropriate, and avoid private image URLs or confidential product material unless cloud processing is acceptable.

Risk: Generated promotional copy or visual claims may be inaccurate, unsupported, or unsuitable for marketplace compliance.

Mitigation: Verify product claims and promotion details before generation, avoid absolute claims, and review generated images before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with bash command examples and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and generation commands for 1:1 or 3:4 e-commerce main images; generated assets are written to local output paths when commands are executed.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
