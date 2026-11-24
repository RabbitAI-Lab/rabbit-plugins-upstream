## Description:

一张商品图裂变成整套素材。商品图 + 卖点 → 多角度多场景成套图，够铺满一屏。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家和内容创作者用它把一张商品图与商品卖点转化为多角度、多场景的商品或模特套图，并获得可执行的生成提示词与命令。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be transferred to an external image-generation provider.

Mitigation: Check which provider will receive the images and prompts, confirm that transfer is authorized, and avoid including sensitive information in the images.

Risk: The security analysis is incomplete, and the workflow includes commands that invoke provider tooling.

Mitigation: Review the commands and required permissions before running them, and verify the provider and CLI source/version you choose to use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with shell command examples; generated JPEG, PNG, or WebP images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A series of images depicting the same product across different angles or scenes; dimensions and image format are selectable.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
