## Description:

用一份可复用的 brand.yaml 统一店铺商品图中的模特、色温、构图、留白与文案语气。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营者和商品内容创作者可用它维护可复用的店铺视觉规范，并将规范应用到商品图提示词及批量生图流程中。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security review marks the skill suspicious and notes that some components were only partially analyzed; credential handling and image-generation behavior need review.

Mitigation: Review the skill's capabilities before installing, decide whether to use provider credentials and external image services, and account for possible paid requests.

## Reference(s):

- [Brand Kit on ClawHub](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml field reference](references/brand-schema.md)
- [Image generation provider reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands, Images]

**Output Format:** [YAML brand configuration, prompt text, shell commands, and optionally generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires a configured provider and may send prompts and reference images to that provider; provider requests may incur charges.]

## Skill Version(s):

1.0.32 (source: frontmatter; release evidence agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
